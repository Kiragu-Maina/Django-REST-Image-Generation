from django.urls import path
from . import views

urlpatterns = [
    path('generate-image/', views.GenerateImageView.as_view(), name='generate-image'),
]
