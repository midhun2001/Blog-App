from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post
from .forms import PostForm, SignUpForm


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'posts': posts})


def add_post(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.creator = request.user
                new_post.save()
                messages.success(request, "Blog Post Created Successfully!")
                return redirect('home')
        return render(request, 'blog/add_post.html', {'form': form})
    return redirect('signin')
    
    
def update_post(request, pk):
    current_post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=current_post)
    if form.is_valid():
        form.save()
        messages.success(request, "Blog Post Updated Successfully!")
        return redirect('home')
    return render(request, 'blog/update_post.html', {'form': form, 'post':current_post})


def view_post(request, pk):
    current_post = Post.objects.get(pk=pk)
    return render(request, 'blog/view_post.html', {'post': current_post})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, "Blog Post Deleted Successfully!")
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account Created Successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('signin')
    
    return render(request, 'blog/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
