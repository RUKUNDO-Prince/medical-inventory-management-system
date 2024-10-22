from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
]