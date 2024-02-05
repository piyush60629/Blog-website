from django.contrib import admin
from .models import Blog_Category,contact_info,subscription_info, blog_post, blog_comment

# Register your models here.
admin.site.register(Blog_Category)
admin.site.register(contact_info)
admin.site.register(subscription_info)
admin.site.register(blog_post)
admin.site.register(blog_comment)