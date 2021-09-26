from django.urls import path

from blog import views


urlpatterns = [
    path("", views.AllPostsView.as_view(), name = 'all-posts'),
    path("<int:pk>/", views.SinglePostView.as_view(), name = 'single-post'),
    path("<int:pk>/delete/", views.DeletePostView.as_view(), name = 'delete-post'),
    path("new/", views.CreatePostView.as_view(), name = 'new-post'),
    path("<int:pk>/update/", views.UpdatePostView.as_view(), name = 'update-post'),
]