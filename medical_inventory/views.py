from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category
from django.contrib import messages
# from ..medical_inventory_management_system.settings import LOW_QUANTITY
from django.conf import settings

class Index(TemplateView):
    template_name = 'medical_inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        low_inventory = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=settings.LOW_QUANTITY
        )
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request, f'{low_inventory.count()} items have low inventory!')
            else:
                messages.error(request, f'{low_inventory.count()} item has low inventory')
        low_inventory_ids = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=settings.LOW_QUANTITY
        ).values_list('id', flat=True)
        return render(request, 'medical_inventory/dashboard.html', {'items': items, 'low_inventory_ids': low_inventory_ids})

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
        context['action'] = "Add" if self.__class__.__name__ == "AddItem" else "Update"
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Item added successfully!")
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'medical_inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Add" if self.__class__.__name__ == "AddItem" else "Update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Item updated successfully!")
        return super().form_valid(form)

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'medical_inventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Item deleted successfully!")
        return super().delete(request, *args, **kwargs)