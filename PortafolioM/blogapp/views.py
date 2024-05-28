from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/blog.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})
