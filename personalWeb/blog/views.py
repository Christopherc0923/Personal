from django.shortcuts import render, get_object_or_404
from .models import Blogpage
# Create your views here.
def blog(request):
    # Only assigns project with the 5 most recent post
    blogs = Blogpage.objects.order_by('-date')[:5]

    return render(request, 'blog/home.html', {'blogs' : blogs})

# Function to view the specific blog post
def detail(request, blog_id):
    # Grabs the pk-th blog from blogpage, otherwise return error 404 if not found
    blog = get_object_or_404(Blogpage, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})