from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from blog.models import Post


class AllPostsView(ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(hidden=False)


class SinglePostView(DetailView):
    model = Post


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('all-posts')


class CreatePostView(CreateView):
    model = Post
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    fields = '__all__'