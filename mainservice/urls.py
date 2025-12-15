from django.urls import path, include
from . import views

urlpatterns = [
    path('service/', views.service_view, name='service_view')
    


]