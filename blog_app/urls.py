from django.urls import path
from blog_app.views import indexView

urlpatterns = [
    path("", indexView, name="index"),
]
