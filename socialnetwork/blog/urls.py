from . import views
from django.urls import path
import socialnetwork.views as scviews

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('hello/', scviews.HelloView.as_view(), name='hello'),
]