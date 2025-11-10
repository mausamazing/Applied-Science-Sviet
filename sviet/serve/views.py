from django.shortcuts import render, get_object_or_404
from upload.models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")
    return render(request, 'serve/blog_list.html', {'blogs':blogs})

def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'serve/blog_detail.html', {'blog':blog})

def faculty(request):
    return render(request, "faculty.html")
def branch(request):
    return render(request, "branch.html")
def infrastructure(request):
    return render(request,"infrastrucre.html")
def committee(request):
    return render(request, "committee.html")
def workshop(request):
    return render(request,"workshop.html")
def aboutus(request):
    return render(request,"aboutus.html")
def classroom(request):
    return render(request,"classroom.html")