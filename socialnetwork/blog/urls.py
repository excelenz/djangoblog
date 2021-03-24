from . import views
import socialnetwork.views as api_view
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('api/token/register/', api_view.registration_view, name='auth_register'),
    path('api/token/post/', views.create_post, name="create_post"),
]
