from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
     model = models.Article
     template_name = 'article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
     model = models.Article
     template_name = 'article_new.html'
     fields = ['title', 'body', ]
     login_url = 'login'

     def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class CommentCreateView(LoginRequiredMixin, CreateView):
     model = models.Comment
     template_name = 'comment_new.html'
     fields = ['comment', ]
     login_url = 'login'

     def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = models.Article.objects.get(id=1)
        print(self.get_initial())
        return super().form_valid(form)
