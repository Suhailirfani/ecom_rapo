from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .models import Products, Category


# Create your views here.
def home(request, slug_c=None):
    page_c = None
    if slug_c != None:
        page_c = get_object_or_404(Category, slug=slug_c)
        product = Products.objects.all().filter(category=page_c, available=True)
    else:
        product = Products.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': page_c, 'product': product})


def prod_detail(request, slug_c, slug_p):
    try:
        product = Products.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'product_details.html', {'product': product})


def cart(request):
    return render(request, 'cart.html')


def payments(request):
    return render(request, 'payments.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.lastname = lname

        myuser.save()
        return redirect('signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            print(fname)
            return render(request, 'demo_user.html', {'fname': fname})
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('home')
