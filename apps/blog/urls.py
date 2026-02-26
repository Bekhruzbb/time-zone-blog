from . import views
from django.urls import path
app_name = 'blog'

urlpatterns = [
    path('', views.show_blog_page, name='blog'),
    path('articles/<slug:slug>', views.show_article_page, name='detail'),
    path('search/', views.get_search, name='search'),
    path('category/<slug:category_slug>/', views.show_blogs_by_category, name='category'),
    path('tags/<slug:tag_slug>', views.show_blog_by_tag, name='tag')
]
