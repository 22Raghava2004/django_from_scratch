from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','user','created_at']
    exclude=['slug']
admin.site.register(Post,PostAdmin)
admin.site.register(Follow)

# Register your models here.
