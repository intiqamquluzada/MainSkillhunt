from django.urls import path

from blog.views import bl_detail, BlogListView

app_name = 'Blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('blog-single/<slug:slug>', bl_detail, name='blog-single'),
]
