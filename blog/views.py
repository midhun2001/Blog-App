from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'home.html', {'posts': posts})


def add_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form': form})


def update_post(request, pk):
    current_post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=current_post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_post.html', {'form': form})

def view_post(request, pk):
    current_post = Post.objects.get(pk=pk)
    return render(request, 'view_post.html', {'post': current_post})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')