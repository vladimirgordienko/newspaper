from rest_framework import serializers
from articles.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'date', 'author', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'article', 'author', 'comment', )
