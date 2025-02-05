from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/', views.book, name='book'),
     path('login/', views.loginPage, name="login"),
     path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name='register'),
    path('success/<int:booking_id>/', views.success, name='success'),  # Ensure this line is correct
    path('contact/', views.contact, name='contact'),
    path('contact/success/<int:contact_id>/', views.contact_success, name='contact_success'), # Ensure this line is correct
]
