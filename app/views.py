from django.shortcuts import render, redirect
from app.models import Post
from app.forms import PostForm
from datetime import datetime

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def new_post(request):
    if request.method == "GET":
        return render(request, "new_post.html")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            author = form.cleaned_data["author"]
            published = form.cleaned_data["published"]
            new_post = Post.objects.create(
                author=request.user, content=content, published=datetime.now()
            )
            return redirect("home")
        else:
            return render(request, "new_post.html", {"form": form})

