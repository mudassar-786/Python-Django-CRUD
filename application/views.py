from django.shortcuts import render,redirect ,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blog
# Create your views here.
def index(request): 
    blog=Blog.objects.all()
    return render(request,'index.html',{'blogs':blog})
def sign(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request,' Wellcome !!')
            return render(request,'dashbord.html')
        else:
        # Return an 'invalid login' error message.
            messages.info(request,' invalid login ')
            return render(request,'signin.html')

    return render(request,'signin.html')
    
def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,' username is already registerd !')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()
                messages.success(request,' You Account has been created !!')
                return redirect('login_')
    return render(request,'signup.html')
def logout_(request):
    logout(request)
    return render(request,'login_')  
def dashbord(request):
    if request.method=="POST":
        title = request.POST.get("title")
        image = request.POST.get('image')
        desc = request.POST.get('desc')
        blog = Blog(user_id=request.user,title=title,desc=desc,image=image)
        blog.save()
        messages.success(request," Your data is successfully send to database")

    return render(request,'dashbord.html')
def blogdetail(request, id):
    blog =Blog.objects.get(id=id)
    print(blog)
    return render(request, 'blog_detail.html',{'blog': blog})

def delete_post(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request," YOUR DATA is deleted sucessfully ")
    return redirect('/')
def edit_post(request,id):
    blog = Blog.objects.get(id=id)
    if request.method=="POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        image = request.POST.get('image')
        blog.title = title
        blog.desc = desc
        blog.image = image
        blog.save()
        messages.success(request,' Your data is successfully edit')
        return redirect('/')
    return render(request,'edit.html',{'blog':blog})
        