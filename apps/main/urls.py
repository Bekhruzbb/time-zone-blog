from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('contacts/', views.show_contacts_page, name='contacts')
]