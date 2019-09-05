from django.contrib import admin
from napp.models import Author, Notes, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Notes)
admin.site.register(Comment)