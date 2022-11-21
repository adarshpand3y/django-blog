from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    return render(request, "index.html")

def blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blogs.html", context)

def blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)[0]
    context = {"blog": blog}
    return render(request, "blog.html", context)

def contact(request):
    return render(request, "contact.html")