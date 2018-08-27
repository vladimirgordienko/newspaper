from rest_framework import generics
from articles.models import Article, Comment
from articles.api.serializers import ArticleSerializer, CommentSerializer
from articles.api.permissions import IsAuthorOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    """
    Endpoint to list all Articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint to retrieve, delete and change Article
    """
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentList(generics.ListAPIView):
    """
    Endpoint to list all Comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListByArticleID(generics.ListAPIView):
    """
    Endpoint to list all Comments by Article ID
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(article__id=self.kwargs['pk'])
        return qs


class CommentDetail(generics.RetrieveAPIView):
    """
    Endpoint to retrieve Comment by ID
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
