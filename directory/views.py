from django.shortcuts import render, get_object_or_404
from .models import Category, Link

def home(request):
    categories = Category.objects.all()
    recent_links = Link.objects.order_by('-created_at')[:10]
    return render(request, 'directory/home.html', {
        'categories': categories,
        'recent_links': recent_links
    })

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    links = Link.objects.filter(category=category).order_by('-created_at')
    return render(request, 'directory/category.html', {
        'category': category,
        'links': links
    })

def search(request):
    query = request.GET.get('q', '')
    links = []
    if query:
        links = Link.objects.filter(
            title__icontains=query
        ).order_by('-created_at')
    return render(request, 'directory/search.html', {
        'links': links,
        'query': query
    })