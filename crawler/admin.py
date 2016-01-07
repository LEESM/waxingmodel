from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
	list_display = admin.ModelAdmin.list_display + (
		'id',
		'title',
		'content',
		'link',
		'pub_date',
		'cafe_blog',
	)


# Register your models here.
