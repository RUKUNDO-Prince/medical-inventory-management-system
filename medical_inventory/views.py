from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from medical_inventory_management_system.medical_inventory.forms import UserRegisterForm

class Index(TemplateView):
    template_name = 'medical_inventory/index.html'

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
                password=form.cleaned_data['password']
            )

            login(request, user)
            return redirect('index')
        return render(request, 'medical_inventory/signup.html', {'form': form})