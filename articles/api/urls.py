from django.urls import path
from articles.api.endpoints import (
    ArticleList,
    ArticleDetail,
    CommentList,
    CommentDetail,
    CommentListByArticleID,
)


urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
    path('articles/comments/', CommentList.as_view()),
    path('articles/<int:pk>/comments/', CommentListByArticleID.as_view()),
    path('articles/comments/<int:pk>/', CommentDetail.as_view()),
]
