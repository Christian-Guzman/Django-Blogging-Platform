from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.home, name="home"),
    path("new_post", app.views.new_post, name="new_post"),
]
