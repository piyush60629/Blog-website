from.models import Blog_Category, blog_post
from django.forms import ModelForm
 
class Blog_Form(ModelForm):
    class Meta:
         model = Blog_Category
         fields = "__all__"

class BlogPost_Form(ModelForm):
    class Meta:
         model = blog_post
         fields = "__all__"