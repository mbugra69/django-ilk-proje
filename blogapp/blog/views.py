from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from blog.models import Category

data = {
    "blogs": [
    {
        "id": 1,
        "title": "komple",
        "image": "yazilim.png",
        "is_active": True,
        "is_home": True,
        "description": "çok iyi bir kurs"
    },
    {
        "id": 2,
        "title": "komple 2",
        "image": "yazilim.png",
        "is_active": True,
        "is_home": False,
        "description": "çok iyi bir kurs"
    },
    {
        "id": 3,
        "title": "komple 23",
        "image": "django.jpeg",
        "is_active": False,
        "is_home": True,
        "description": "çok iyi bir kurs"
    },



    ]


}



# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True,is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html",context)

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
def blogs_by_category(request, slug):
    c = Category.objects.get(slug=slug)
    context = {
        "blogs": c.blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html",context)
