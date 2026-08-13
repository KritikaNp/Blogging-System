from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogs.models import Category, blog
from About_section.models import About
from .forms import RegistrationForm

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)