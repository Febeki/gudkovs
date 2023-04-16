from django.contrib.auth.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('register/', views.Register.as_view(), name='register'),
    path('table/<str:table_name>/', views.table_view, name='table-name'),
    path('admin/', views.admin_table, name='admin-table'),
    # path('admin/', views.ModelList.as_view(), name='model_list'),
    # path('<str:model_name>/<int:pk>/', views.ModelEdit.as_view(), name='model_edit'),
    path('accountant/', views.accountant_table, name='accountant-table'),
    path('security/', views.security_table, name='security-table'),
    path('', include('django.contrib.auth.urls')),
]