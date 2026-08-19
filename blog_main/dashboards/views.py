from django.shortcuts import render
from blogs.models import Category, blog
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blog_count': blog_count,
    }
    return render(request, 'dashboard/dashboard.html', context)
