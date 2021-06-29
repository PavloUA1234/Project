from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_home, name="news_home"),
    path('news/', views.post_new, name='post_new'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
]