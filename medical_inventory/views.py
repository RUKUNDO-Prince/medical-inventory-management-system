from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category

class Index(TemplateView):
    template_name = 'medical_inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
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

class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'medical_inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'medical_inventory/item_form.html'
    success_url = reverse_lazy('dashboard')