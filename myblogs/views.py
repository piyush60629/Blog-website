from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog_Category,contact_info,subscription_info,blog_post,blog_comment
from.forms import Blog_Form, BlogPost_Form
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
# Create your views here.
def home(request):
    x=Blog_Category.objects.all()
    print(x)
    if request.method == 'GET':
        return render(request,'myblogs/home.html', {"category":x})
    elif request.method == 'POST':
        email = request.POST.get('subscription_email')
        y = subscription_info(s_email=email)
        y.save()
        return render(request,'myblogs/home.html',{"category":x , "feedback": "Thank you for subscription"})   

def searching(request):
    if request.method=="POST":
        x=request.POST.get('prodsearch')
        mydata=Blog_Category.objects.filter(Q(blog_cat__icontains=x) | Q(blogcat_description__icontains=x))
        if mydata:
            return render(request,'myblogs/home.html',{'category':mydata})
        else:
            return render(request,'myblogs/home.html',{'warning':'data not found'})

def contact(request):
    if request.method == 'GET':
        return render(request, 'myblogs/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        return render(request,'myblogs/contact.html',{'feedback':'Your message has been received'})

def blog(request):
    # Extract the category from the request parameters
    category_name = request.GET.get('category')

    # If a category is provided, filter blog posts by that category, otherwise, get all blog posts
    if category_name:
        blogs = blog_post.objects.filter(blog_cat__blog_cat=category_name)
    else:
        blogs = blog_post.objects.all()
        

    return render(request, 'myblogs/blog.html', {"blogs": blogs, "category": category_name})
        
def ck(request):
    x = BlogPost_Form()
    return render(request,'myblogs/ck.html',{"x":x})

def allblogs(request):
    y=blog_post.objects.all()
    p = Paginator(y, 2)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    return render(request,'myblogs/allblogs.html',{ "y":page_obj})

def blog_details(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    z=obj.view_count
    z=z+1
    obj.view_count=z
    obj.save()
    print(obj)
    print(blog_id)
    _comments=blog_comment.objects.filter(blog_id=blog_id)

    return render(request,'myblogs/blog_details.html', {"obj":obj,"comments":_comments})
    # return render(request,'myblogs/blog_details.html', {"obj":obj})
    # return HttpResponse('blog_details')

def loginuser(request):
    if request.method == 'GET':
        return render(request,'myblogs/loginuser.html',{"form":AuthenticationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password')
        user=authenticate(request,username=a,password=b)
        if user is None:
            return render(request,'myblogs/loginuser.html',{"form":AuthenticationForm, 'error':"Invalid Credentials"})
        else:
            login(request,user)
            return redirect('home')

    
def signupuser(request):
    if request.method == 'GET':
        return render(request,'myblogs/signupuser.html',{'form':UserCreationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if b==c:
            # check whether user name is unique
            if(User.objects.filter(username=a)):
                return render(request,'myblogs/signupuser.html',{'form':UserCreationForm(),'error':'Username already exists Try again with a different username'})
            else:
                user=User.objects.create_user(username=a,password=b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            #password 1 and 2 do not match
            return render(request,'myblogs/signupuser.html',{'form':UserCreationForm(),'error':'Password Mismatch Try Again'})

def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
    
def add_like(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    print (obj.like_count)
    y=obj.like_count
    y=y+1
    obj.like_count=y
    obj.save()
    return redirect('blog_details', obj.id)

def comments(request,blog_id):
    com = request.POST.get('comment1')
    x = blog_comment(u_comment=com, blog_id=blog_id)
    x.save()

    return redirect('blog_details', blog_id=blog_id)

def edit_comment(request, comment_id):
    comment = get_object_or_404(blog_comment, id=comment_id)

    if request.method == 'POST':
        comment.u_comment = request.POST.get('edited_comment')
        comment.edited_at = timezone.now()  
        comment.save()
        return redirect('blog_details', blog_id=comment.blog_id)
    context = {
        'comment': comment,
    }
    return render(request, 'myblogs/edit_comment.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(blog_comment, id=comment_id)
    blog_id = comment.blog_id
    comment.delete()
    return redirect('blog_details', blog_id=blog_id)