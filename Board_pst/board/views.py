from django.shortcuts import redirect

from .forms import PostForm, RespondForm
from .models import Authors, Posts, Responds
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsList(ListView):
    model = Posts
    ordering = '-date_create'
    template_name = 'board.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PostDetail(DetailView):
    model = Posts
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responds'] = Responds.objects.filter(post=self.object.id)
        return context


class PostCreate(CreateView):
    model = Posts
    form = PostForm
    template_name = 'post_create.html'
    success_url = '/board/'

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.author = Authors.objects.get(user=self.request.user)
    #     return super().form_valid(form)


class RespondCreate(FormView):
    model = Responds
    form = RespondForm
    template_name = 'post_respond.html'
    context_object_name = 'respond'











