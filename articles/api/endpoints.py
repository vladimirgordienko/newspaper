from rest_framework import generics
from articles.models import Article
from articles.api.serializers import ArticleSerializer
from articles.api.permissions import IsAuthorOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
