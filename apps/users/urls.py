from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('auth/', views.show_auth_page, name='auth'),
    path('auth/login/', views.login_user, name='login'),
    path('register/', views.show_register_page, name='register'),
    path('register/user/', views.register_user, name='reg-user'),
    path('logout/', views.logout_page, name='logout'),
    path('wishlist/', views.show_wishlist_page, name='wishlist'),
    path('wishlist/<str:product_id>/', views.add_delete_fav, name='wishlist-action')
]
