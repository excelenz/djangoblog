from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'author','content', 'status,' ]

	def	save(self):
		author = serializers.SlugRelatedField(
			username='author',
			queryset=User.objects.all()
		)
		title = self.validated_data['title']
		content = self.validated_data['content']

		post.save()
		return post