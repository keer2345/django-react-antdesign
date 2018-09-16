from django.urls import path

from .views import (ArticleCreateView, ArticleDeleteView, ArticleDetailView,
                    ArticleListView, ArticleUpdateView)

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('<pk>/update', ArticleUpdateView.as_view()),
    path('<pk>/delete', ArticleDeleteView.as_view()),
]
