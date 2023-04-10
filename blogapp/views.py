from django.shortcuts import render
from .models import Blog, Contact

# Create your views here.
def index(request):
    return render(request, "index.html")

def blogs(request):
    blogs = Blog.objects.all().order_by("-date_added")
    context = {"blogs": blogs}
    return render(request, "blogs.html", context)

def blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)[0]
    context = {"blog": blog}
    return render(request, "blog.html", context)

def contact(request):
    parameters = {"submitted": False}
    if request.method == "POST":
        name = request.POST["user_name"]
        email = request.POST["user_email"]
        message = request.POST["user_message"]
        newContact = Contact(name=name, email=email, message=message)
        newContact.save()
        parameters["submitted"] = True
    return render(request, "contact.html", parameters)