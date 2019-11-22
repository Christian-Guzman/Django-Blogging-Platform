from django.contrib import admin
from django.urls import path
import app.views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.home, name="home"),
    path("new_post", app.views.new_post, name="new_post"),path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("sign-up/", app.views.SignUpView.as_view(), name="sign-up"),
    path("user-post/", app.views.user_post, name="user_post")
]
