from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blogs.models import blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the category id
    posts = blog.objects.filter(status='Published', category=category_id)
    # use try/except when we want to do some custom actionif the category does not exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect to the home page
        return redirect('home')
    # use get_object_or_404 when you want to show 404 error page if category does not exist
    # category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts':posts,
        'category': category,
    } 
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(blog, slug=slug, status= 'Published')
    context={
        'single_blog':single_blog,
    }
    return render(request, 'blogs.html', context)

