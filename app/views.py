from django.shortcuts import render, redirect
from app.models import Post
from app.forms import PostForm
from datetime import datetime
from django.contrib.auth import login
from django.urls import reverse_lazy
from app import forms
from django.views.generic import FormView
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "base.html", {"posts": posts})

class SignUpView(FormView):
    form_class = forms.SignUpForm
    template_name = "auth/user_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.signup()
        login(self.request, user)
        return super().form_valid(form)

def new_post(request):
    if request.method == "GET":
        return render(request, "new_post.html")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            published = form.cleaned_data["published"]
            new_post = Post.objects.create(
                author=request.user, content=content, published=published
            )
            return redirect("home")
        else:
            return render(request, "new_post.html", {"form": form})

def user_post(request):
    current_user = Post.objects.filter(author=request.user)
    return render(request, "user_post.html", {"current_user":  current_user})
