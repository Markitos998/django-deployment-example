from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('basic_app/other/', views.other, name='other'),
    path('basic_app/relative/', views.relative, name='relative'),
]