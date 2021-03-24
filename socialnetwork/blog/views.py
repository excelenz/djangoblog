from django.views import generic
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from socialnetwork.models import Account
from socialnetwork.models import User
from . serializer import BlogPostSerializer
from rest_framework.decorators import api_view

class PostList(generic.ListView,APIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView,APIView):
    #permission_classes = (IsAuthenticated,)
    model = Post
    template_name = 'post_detail.html'


@api_view(['POST'])
def create_post(request):
	if request.method == 'POST':
		user = User.objects.get(pk=1)
		blog_post = Post(author=user)
		if request.method == 'POST':
			serializer = BlogPostSerializer(blog_post, data=request.data)
			data = {}
			if serializer.is_valid():
				post = serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors)
