# from rest_framework.generics import (CreateAPIView, DestroyAPIView,
#                                      ListAPIView, RetrieveAPIView,
#                                      UpdateAPIView)

from rest_framework import viewsets

from articles.models import Article

from .serializes import ArticleSerializer


class ArticleViewSet (viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
