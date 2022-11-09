from django.shortcuts import render, HttpResponse
from Blogg.models import Post

# Create your views here.

def bloghome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/bloghome.html", context)

def blogpost(request, slug):
    return render(request, f'blog/blogpost.html')

