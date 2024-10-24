from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import UserRegisterForm
from .models import InventoryItem

class Index(TemplateView):
    template_name = 'medical_inventory/index.html'

class Dashboard(View):
    def get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        return render(request, 'medical_inventory/dashboard.html', {'items': items})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'medical_inventory/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')
        return render(request, 'medical_inventory/signup.html', {'form': form})