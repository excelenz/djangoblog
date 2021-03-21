from django.views import generic
from .models import Post, Likes

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    try:
        likes = Likes.objects.get(id_post=Post.id_post,like_status=1).blog_likes.count()
        unlikes = Likes.objects.get(id_post=Post.id_post,like_status=2).blog_likes.count()
    except:
        likes = 0
        unlikes = 0
    template_name = 'post_detail.html'
