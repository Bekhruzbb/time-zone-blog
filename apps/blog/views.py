from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.


def show_blog_page(request):
    articles = models.Blog.objects.all()
    categories = models.Category.objects.all()
    tags = models.Tag.objects.all()
    photos = models.InstagramPhoto.objects.all()
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles': articles,
        'categories': categories,
        'tags': tags,
        'photos': photos
    }

    return render(request, 'blog/blog.html', context)


def show_blogs_by_category(request, category_slug):
    category = models.Category.objects.get(slug=category_slug)
    articles = models.Blog.objects.filter(category=category)
    categories = models.Category.objects.all()
    context = {
        'articles': articles,
        'category': category,
        'categories': categories
    }
    return render(request, 'blog/blog.html', context)


def show_blog_by_tag(request, tag_slug):
    tag = models.Tag.objects.get(slug=tag_slug)
    articles = models.Blog.objects.filter(tag=tag)
    tags = models.Tag.objects.all()
    categories = models.Category.objects.all()
    context = {
        'articles': articles,
        'tags': tags,
        'tag': tag,
        'categories': categories
    }
    return render(request, 'blog/blog.html', context)


def show_article_page(request, slug):
    blog = models.Blog.objects.get(slug=slug)
    blogs = list(models.Blog.objects.all())
    all_blogs = models.Blog.objects.all()
    blog_index = blogs.index(blog)
    prev_blog = blogs[blog_index-1]
    if len(blogs) == blog_index+1:
        next_blog = blogs[0]
    else:
        next_blog = blogs[blog_index+1]

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = blog
            comment.name = request.user
            comment.save()
            return redirect('blog:detail', slug)
    else:
        form = CommentForm

    categories = models.Category.objects.all()
    tags = models.Tag.objects.all()
    instagram_photos = models.InstagramPhoto.objects.all()
    context = {
        'blog': blog,
        'form': form,
        'next_blog': next_blog,
        'prev_blog': prev_blog,
        'categories': categories,
        'tags': tags,
        'all_blogs': all_blogs,
        'instagram_photos': instagram_photos
    }
    return render(request, 'blog/articles.html', context)


from django.db.models import Q


def get_search(request):
    query = request.GET.get('q')
    if not query:
        articles = models.Blog.objects.all()
    else:
        articles = models.Blog.objects.filter(Q(title__iregex=query)|Q(short_description__iregex=query))
    context = {
        'articles': articles,
        'query': query
    }
    return render(request, 'blog/search.html', context)
