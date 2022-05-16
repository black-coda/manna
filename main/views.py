from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import MannaForm, RegisterForm
from main.models import Manna, User
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from hitcount.views import HitCountDetailView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


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
    paginate_by = 4


def manna_detail_view(request,slug):
    manna = get_object_or_404(Manna, slug=slug)
    manna_comment = manna.manna_comments.all()

    context = {
        'manna':manna,
        'comments':manna_comment,
    }
    return render(request, 'main/manna_detail.html', context)

class MannaDetailView(HitCountDetailView):
    model = Manna
    template_name = 'main/manna_detail.html'
    slug_field = 'slug'
    count_hit = True
    context_object_name = 'manna'

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     return redirect(self.object.song.audio_file.url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        'popular_posts': Manna.objects.order_by('-hit_count_generic__hits')[:3],
        # 'manna_by_author':Manna.objects.filter(user=self.user)

        })
        return context    


def user_profile_view(request, pk):
    user = User.objects.get(id=pk)
    manna = user.manna_set.all()
    print(manna)

    context = {
        'user':user,
        'manna':manna

    }
    return render(request, 'profile.html')



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
        print(request.POST)
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


def password_reset_view(request):
    form = PasswordResetForm()
    context = {
        'form':form
    }
    return render(request, 'trial.html', context)



def password_change_form(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data = request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('login-view')
        else:
            form = PasswordChangeForm(user=request.user)
        

    context = {
        'form':form
    }
    return render(request, 'password_change.html', context)
    