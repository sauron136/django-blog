from django.shortcuts import render, get_object_or_404
from apps.blogs.models import Post

def post_list(request):
    post = Post.objects.all()
    return render(request, 'blogs/post/list.html', {'post':post})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day)
    return render(request, 'blog/post/detail.html', {post: 'post'})