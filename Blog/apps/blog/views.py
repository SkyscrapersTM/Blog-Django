from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.db.models import Q

from apps.blog.models import Category, Post


def home(request):
    '''
        display the main page
    '''
    # Get value from request
    queryset = request.GET.get('search')
    # Filter all post where status is active
    posts = Post.objects.filter(status=True)

    # exist queryset
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(extract__icontains=queryset)
        ).distinct()

    return render(request, 'index.html', {'posts': posts})


def detailPost(request, slug):
    '''
        display detail Post by slug
    '''

    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, 'post.html', {'detailPost': post})


def general(request):
    '''
        display posts by catogories
    '''
    # Get value from request
    queryset = request.GET.get('search')

    # Filter all post where status is active and the type category is General
    posts = Post.objects.filter(
        status=True,
        category=Category.objects.get(name__iexact='general')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(extract__icontains=queryset),
            status=True,
            category=Category.objects.get(name__iexact='general')
        ).distinct()
    return render(request, 'general.html', {'posts': posts})


def programming(request):
    '''
        display posts by programming
    '''
    # Get value from request
    queryset = request.GET.get('search')

    # Filter all post where status is active and the type category is Programming
    posts = Post.objects.filter(
        status=True,
        category=Category.objects.get(name__iexact='Programming')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(extract__icontains=queryset),
            status=True,
            category=Category.objects.get(name__iexact='Programming')
        ).distinct()
    return render(request, 'programming.html', {'posts': posts})


def tutorials(request):
    '''
        display posts by tutorials
    '''
    # Get value from request
    queryset = request.GET.get('search')

    # Filter all post where status is active and the type category is Tutorials
    posts = Post.objects.filter(
        status=True,
        category=Category.objects.get(name__iexact='Tutorials')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(extract__icontains=queryset),
            status=True,
            category=Category.objects.get(name__iexact='Tutorials')
        ).distinct()

    return render(request, 'tutorials.html', {'posts': posts})


def tecnology(request):
    '''
        display posts by tecnology
    '''
    # Get value from request
    queryset = request.GET.get('search')

    # Filter all post where status is active and the type category is Tecnology
    posts = Post.objects.filter(
        status=True,
        category=Category.objects.get(name__iexact='Tecnology')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(extract__icontains=queryset),
            status=True,
            category=Category.objects.get(name__iexact='Tecnology')
        ).distinct()

    return render(request, 'tecnology.html', {'posts': posts})


def videogames(request):
    '''
        display posts by videogames
    '''
    # Get value from request
    queryset = request.GET.get('search')

    # Filter all post where status is active and the type category is VideoGames
    posts = Post.objects.filter(
        status=True,
        category=Category.objects.get(name__iexact='VideoGames')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(extract__icontains=queryset),
            status=True,
            category=Category.objects.get(name__iexact='VideoGames')
        ).distinct()

    return render(request, 'videogames.html', {'posts': posts})

# Vocabulary:

# Q:            If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.
# __iexact:     case-insensitive exact match.
