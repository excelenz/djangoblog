from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(
	queryset=User.objects.all(), slug_field='username'
	)

	class Meta:
		model = Post
		fields = ('title', 'author', 'content','status')
