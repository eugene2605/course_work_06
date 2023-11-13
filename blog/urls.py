from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(BlogListView.as_view()), name='list_blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete_blog'),
]
