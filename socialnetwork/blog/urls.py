from . import views
import socialnetwork.views as vsviews
from django.urls import path

urlpatterns = [
    path('hello/', vsviews.HelloView.as_view(), name='hello'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
