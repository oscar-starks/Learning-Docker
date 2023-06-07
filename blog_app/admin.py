from django.contrib import admin
from blog_app.models import Category, Recipe

admin.site.register([Category, Recipe])