from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from blog.models import Post
from rest_framework import serializers, viewsets


class BlogMixin:
    model = Post
    fields = ["title", "content", "hidden"]
    success_url = reverse_lazy('blog:all')


class OwnerMixin():
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class AllPostsView(BlogMixin, ListView):
    def get_queryset(self):
        return super().get_queryset().filter(hidden=False)


class SinglePostView(BlogMixin, DetailView):
    pass


class DeletePostView(LoginRequiredMixin, BlogMixin, OwnerMixin, DeleteView):
    pass


class CreatePostView(LoginRequiredMixin, BlogMixin, CreateView):
    model = Post
    fields = ["title", "content", "hidden"]

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, BlogMixin, OwnerMixin, UpdateView):
    pass


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        depth = 1
        fields = ["id", "title", "content", "hidden", "author_id"]


class PostViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Post.objects.all()
    serializer_class = PostSerializer