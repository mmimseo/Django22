from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
admin.site.register(Post)          ## Model 추가 (앱이름) ##

class CategoryAdmin(admin.ModelAdmin):    ## slug ##
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_field = {'slug' : ('name',)}
admin.site.register(Tag, admin)
