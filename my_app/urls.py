from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('register/', views.Register.as_view(), name='register'),
    path('table/<str:table_name>/', views.table_view, name='table_view'),
    path('create/<str:table_name>/', views.create_view, name='create_view'),
    path('admin/', views.admin_table, name='admin-table'),

    path('accountant/', views.accountant_table, name='accountant-table'),
    path('security/', views.security_table, name='security-table'),
    path('', include('django.contrib.auth.urls')),
]