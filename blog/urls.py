from django.urls import path
from blog.views import PostListView, PublishedView, post_share

# app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    # path('post-detail/<int:pk>/', PublishedView.as_view(), name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PublishedView.as_view(), name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),

]
