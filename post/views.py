from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post.models import CreatePostForm, Post

# Create your views here.

@login_required(login_url='/account/login/')
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            post = Post.objects.order_by('-id')
            # return redirect('/account/', {'post': post})
            return redirect('/account/', {'post': post})
        else:
            form = CreatePostForm()
            post = Post.objects.order_by('-id')
            return render(request, 'post/create.html', {'form': form})
    else:
        form = CreatePostForm()
        post = Post.objects.order_by('-id')
        return render(request, 'post/create.html', {'form': form})