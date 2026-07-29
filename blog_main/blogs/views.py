from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the category id
    posts = blog.objects.filter(status='Published', category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts':posts,
        'category': category,
    } 
    return render(request, 'posts_by_category.html', context)
