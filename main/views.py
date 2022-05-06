from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import MannaForm, RegisterForm
from main.models import Manna, User
from django.contrib.auth import authenticate, login, logout
from django.views import generic

def index_view(request):
    return render(request, 'index.html')

def create_manna_view(request):
    pass

def update_manna_view(request,pk):
    pass

# def delete_obj(request,pk):

#     context={

#     }
#     return render()


class MannaListView(generic.ListView):
    model = Manna
    template_name = "manna_list.html"
    context_object_name = 'mannas'
    paginate_by = 3


def manna_detail_view(request,slug):
    manna = get_object_or_404(Manna, slug=slug)
    manna_comment = manna.manna_comments.all()

    context = {
        'manna':manna
    }
    return render(request, 'main/manna_detail.html', context)


def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
           messages.error(request, 'email or password not authentic 🤨')

    context= {
        'page':page
    }
    return render(request, 'login.html', context)


def logout_view(*args, **kwargs):
    logout(*args, **kwargs)
    return redirect('login-view')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_form =form.save(commit=False)
            user_form.first_name = user_form.first_name.capitalize()
            user_form.last_name = user_form.last_name.capitalize()
            user_form.save()
            messages.success(request, 'Account Created as suceesfully,Login to continue 😁😉')
            return redirect('login-view')
        else:
            messages.error(request, 'Error Processing Registration 😔')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)
    