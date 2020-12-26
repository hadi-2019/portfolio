from django.shortcuts import render
from .models import Post,  Category, Comment
from .forms import CommentForm


def blog_index(request):
    context = {
        "posts": Post.objects.all().order_by('-created_at')
    }
    return render(request, 'blog/index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_at')

    context = {
        "category": category,
        "posts": posts
    }

    return render(request, 'blog/category.html', context)


def blog_detail(request, id):
    post = Post.objects.get(pk=id)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, 'blog/detail.html', context)
