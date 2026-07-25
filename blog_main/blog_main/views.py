from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, blog

def home(request):
    categories = Category.objects.all()
    featured_posts = blog.objects.filter(is_featured= True).order_by('updated_at')
    print(featured_posts)
    context = {        
        'categories': categories,
        'featured_posts': featured_posts,
        }

    return render(request, 'home.html', context)