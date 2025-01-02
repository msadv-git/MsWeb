from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('Q&A', views.qna, name='qna'),
    path('lead-form/', views.lead_form_view, name='lead_form'),
]
