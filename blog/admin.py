from django.contrib import admin

# Register your models here.
from .models import Post

# to make ouyr model visible on the admin page
admin.site.register(Post)
