from . import views
import socialnetwork.views as api_view
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('hello/', include('blog.urls')),
    path('api/token/register/', api_view.registration_view, name='auth_register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
