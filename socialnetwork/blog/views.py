from django.views import generic
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PostList(generic.ListView,APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView,APIView):
    permission_classes = (IsAuthenticated,)
    model = Post
    template_name = 'post_detail.html'
