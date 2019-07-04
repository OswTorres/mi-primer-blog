from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    try:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    except Exception as ex:
        print("\nExcepcion en views Post: {0}".format(type(ex).__name__))
    return render(request, 'blog/post_list.html',{'posts': posts})
    
