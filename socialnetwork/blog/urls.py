from . import views
import socialnetwork.views as api_view
from django.urls import path, include

urlpatterns = [
    path('api/token/register/', api_view.registration_view, name='auth_register'),
    path('api/token/post/', views.create_post, name="create_post"),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]
