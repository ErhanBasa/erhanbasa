# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category,Post,Contact

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Contact)