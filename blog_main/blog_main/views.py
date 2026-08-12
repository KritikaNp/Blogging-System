from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, blog
from About_section.models import About

def home(request):
    featured_posts = blog.objects.filter(is_featured=True ,status='Published').order_by('updated_at')
    posts = blog.objects.filter(is_featured=False ,status='Published').order_by('updated_at')
    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None


    context = {        
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        }

    return render(request, 'home.html', context)