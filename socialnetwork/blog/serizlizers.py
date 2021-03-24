from rest_framework import serializers

from blog.models import Post
from . socialnetwork.models import Account
from blog.serializers import BlogPostSerializer

class BlogPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'author', 'updated_on','content',]
