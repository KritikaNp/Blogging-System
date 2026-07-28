from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, blog

def home(request):
    categories = Category.objects.all()
    featured_posts = blog.objects.filter(is_featured=True ,status='Published').order_by('updated_at')
    posts = blog.objects.filter(is_featured=False ,status='Published').order_by('updated_at')
    print(posts)
    context = {        
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        }

    return render(request, 'home.html', context)