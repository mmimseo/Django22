from django.contrib import admin
from .models import Post, Category ## Model 추가 / import 앱이름 ##

# Register your models here.
admin.site.register(Post)          ## Model 추가 (앱이름) ##

class CategoryAdmin(admin.ModelAdmin):    ## slug ##
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)

