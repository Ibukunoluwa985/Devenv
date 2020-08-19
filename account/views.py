from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import Github, Master_repo, ProfileImg
from django.core.exceptions import ObjectDoesNotExist
from post.models import Post
from django.db.models import Q

# Create your views here.

# post search
def search(request):
    # search query
    query = request.GET.get('q')
    result = Post.objects.filter(
                Q(user__username__icontains=query) |
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(language__icontains=query) |
                Q(created_on__icontains=query)
            )
    return render(request, 'auth_pages/index.html',{'result': result,})

# home navbar
@login_required(login_url='/account/login/')
def navbar(request):
    # profile image
    profile_img = ProfileImg.objects.filter(id = request.user.id)
    return render(request, 'includes/authNavbar.html', {'profile_img': profile_img,})

# home
@login_required(login_url='/account/login/')
def index(request):
    # profile image
    profile_img = ProfileImg.objects.all()
    post = Post.objects.order_by('-created_on')[:50]
    return render(request, 'auth_pages/index.html',
        {
            'post': post,
            'profile_img': profile_img,
        })

# profile
@login_required(login_url='/account/login/')
def profile(request, username):

    try:
        if User.objects.get(username=username):
            return render(request, 'registration/index.html')
        else:
            messages.error(request, 'Have no permission to page')
            return redirect('/account/')
    except ObjectDoesNotExist:
        messages.error(request, 'User does not exist')
        return redirect('/account/')

# register
def registerUser(request):
    if request.user.is_authenticated:
            return redirect('/account/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "New user just Created")
            return redirect('/account/')
        return render(request, 'registration/register.html', {'form': form})

    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# login
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/account/')
    # checking if post
    if request.method == 'POST':
        # get the values from post
        username = request.POST['username']
        password = request.POST['password']

        # making some validations
        user = auth.authenticate(username=username,password=password)

        # logging user, if logged out 
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, "User just logged IN")
                return redirect('/account/')
        messages.error(request, "Invalid Credentials")
        return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')

# logout
@login_required(login_url='/account/login/')
def logout(request):
    auth.logout(request)
    return redirect('/')

# extra fields optional addition
@login_required(login_url='/account/login/')
def username_update(request):
     # checking if post
    if request.method == 'POST':
        # get the value from post
        username_update = request.POST['username']

        if User.objects.filter(username=username_update).exists():
            messages.error(request, 'User already exists.')
            return redirect('/account/')

        else:
            # get user's data from DB and updating them
            username = User.objects.get(username=request.user.username)
            username.username = username_update

            # saving the changes
            username.save()

            messages.success(request, "Username Added")
            return redirect('/account/')
    else:
        return render(request, 'registration/index.html')

@login_required(login_url='/account/login/')
def first_name_update(request):
     # checking if post
    if request.method == 'POST':
        # get the value from post
        change_first_name = request.POST['first_name']

        if User.objects.filter(first_name=change_first_name).exists():
            messages.error(request, 'User already exists.')
            return redirect('/account/')

        else:
            # get user's data from DB and updating them
            first_name = User.objects.get(username=request.user.username)
            first_name.first_name = change_first_name

            # saving the changes
            first_name.save()

            messages.success(request, "First Name Added")
            return redirect('/account/')
    else:
        return render(request, 'registration/index.html')

@login_required(login_url='/account/login/')
def last_name_update(request):
     # checking if post
    if request.method == 'POST':
        # get the value from post
        change_last_name = request.POST['last_name']

        if User.objects.filter(last_name=change_last_name).exists():
            messages.error(request, 'User already exists.')
            return redirect('/account/')

        else:
            # get user's data from DB and updating them
            last_name = User.objects.get(username=request.user.username)
            last_name.last_name = change_last_name

            # saving the changes
            last_name.save()

            messages.success(request, "Last Name Added")
            return redirect('/account/')
    else:
        return render(request, 'registration/index.html')

@login_required(login_url='/account/login/')
def email_update(request):
    # checking if post
    if request.method == 'POST':
        # get the value from post
        change_email = request.POST['email']

        if User.objects.filter(email=change_email).exists():
            messages.error(request, 'User already exists.')
            return redirect('/account/')

        else:
            # get user's data from DB and updating them
            email = User.objects.get(username=request.user.username)
            email.email = change_email

            # saving the changes
            email.save()

            messages.success(request, "Email Added")
            return redirect('/account/')
    else:
        return render(request, 'registration/index.html')

@login_required(login_url='/account/login/')
def github_update(request):
    # checking if post
    if request.method == 'POST':
        # get the value from post
        change_github = request.POST['github']

        if User.objects.filter(username=change_github).exists():
            messages.error(request, 'User github exists.')
            return redirect('/account/')

        else:
            # get user's data from DB and updating them
            user = User.objects.get(username=request.user.username)
            try:
                github = user.github.github
            except ObjectDoesNotExist:
                github = Github(user=request.user)
            github.github = change_github

            # saving the changes
            github.save()

            messages.success(request, "Github Link Added")
            return redirect('/account/')
    else:
        return render(request, 'registration/index.html')

# add master repo
@login_required(login_url='/account/login/')
def add_repo(request):
    # checking if post
    if request.method == 'POST':
        # get the value from post
        add_new_repo = request.POST['add_repo']

        if User.objects.filter(username=add_new_repo).exists():
            messages.error(request, 'User repo exists.')
            return redirect('/account/')

        else:
            # get user's data from DB and updating them
            user = User.objects.get(username=request.user.username)
            try:
                repo = user.master_repo.repo
            except ObjectDoesNotExist:
                repo = Master_repo(user=request.user)
            repo.repo = add_new_repo

            # saving the changes
            repo.save()

            messages.success(request, "Master repo Added")
            return redirect('/account/')
    else:
        return render(request, 'registration/index.html')

# activate account
def activate_account(request):
    # checking if post
    if request.method == 'POST':
        # get the value from post
        email = request.POST['email']

        # activating user
        if User.objects.filter(email=email).exists():
            activate_account = User.objects.get(email=email)
            if activate_account.is_active == False:
                activate_account.is_active = True
                activate_account.save()
            else:
                messages.success(request, "Account activated already")
                return redirect('activate_account')
            messages.success(request, "Account activated")
            return redirect('/')
        else:
            messages.success(request, "Email invalid")
            return redirect('activate_account')
        
    else:
        return render(request, 'registration/activate_account.html')

# disactivate account
@login_required(login_url='/account/login')
def disactivate_account(request):
    # checking if post
    if request.method == 'POST':
        # get the value from post
        disactivate_account = request.POST['disactivate_account']

        # disactivating user
        disactivate_account = User.objects.get(username=request.user.username)
        disactivate_account.is_active = False
        disactivate_account.save()

        messages.success(request, "Account disactivated")
        return redirect('/')
    else:
        return render(request, 'registration/index.html')