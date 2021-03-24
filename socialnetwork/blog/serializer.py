from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class BlogPostSerializer(serializers.ModelSerializer):

	author = serializers.SerializerMethodField(source='User')
	class Meta:
		model = Post
		fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(
	queryset=User.objects.all(), slug_field='username'
	)

	class Meta:
		model = Post
		fields = ('title', 'author', 'content','status')
