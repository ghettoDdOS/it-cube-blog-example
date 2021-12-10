from django.urls import path

from .views import NewsDetailView, NewsListView

urlpatterns = [
    path("list/", NewsListView.as_view(), name="news-list"),
    path("<slug:pk>/", NewsDetailView.as_view(), name="news-detail"),
]
