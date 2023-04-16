from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_month),
    # path('edit/<str:name>/<str:date>/', views.edit_workday, name='edit_workday')
]