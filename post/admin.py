# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from post.models import Post

from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','publishing_date','slug']
    list_display_links = ["publishing_date"]
    list_filter=["publishing_date"]
    search_fields = ["title","content"]
    list_editable = ["title"]
    #prepopulated_fields = {'slug':('title',)}
    class Meta:
        model=Post



# Register your models here.
admin.site.register(Post,PostAdmin)