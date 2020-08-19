from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post.models import CreatePostForm, Post

# Create your views here.

@login_required(login_url='/account/login/')
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            post = Post.objects.order_by('-created_on')[:50]
            return redirect('/account/', {'post': post})
        else:
            form = CreatePostForm()
            return render(request, 'post/create.html', {'form': form})
    else:
        form = CreatePostForm()
        return render(request, 'post/create.html', {'form': form})

# pass id attribute from urls 
def post_datail(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["data"] = Post.objects.get(id = id)

    return render(request, "post/post_datail.html", context,) 