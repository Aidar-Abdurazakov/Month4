from django.shortcuts import render
from django.http.response import  HttpResponse
# Create your views here.

def post_list(r):
    posts = Post.objects.filter(is_published=True)

    return render(r, "list_posts.html", {"posts": posts})