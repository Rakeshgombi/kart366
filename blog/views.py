from django.shortcuts import render, HttpResponse
from .models import Blogpost
# Create your views here.


def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)

    return render(request, 'blog/index.html', {'myposts': myposts})


def blogposts(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    max_id = Blogpost.objects.values('post_id').order_by('-post_id').first()
    min_id = Blogpost.objects.values('post_id').order_by('post_id').first()
    max_id = max_id['post_id']
    min_id = min_id['post_id']
    return render(request, 'blog/blogposts.html', {'post': post, 'max_id': max_id, "min_id": min_id})
