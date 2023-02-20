from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),

    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),

    path('about/', views.about_page, name='about'),
    path('products/', views.products_page, name='products'),
    path('contact_us/', views.contact_page, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'), 
]