from django.urls import path
from articles.api.endpoints import ArticleList, ArticleDetail


urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
]
