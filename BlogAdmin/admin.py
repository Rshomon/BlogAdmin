from django.contrib import admin

# Register your models here.

from .models import Blog,Tag,Category,HeadImage

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(HeadImage)
