from django.contrib import messages
from django.shortcuts import redirect, render
from main.forms import MannaForm, RegisterForm
from main.models import Manna, User
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from hitcount.views import HitCountDetailView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
import requests


def index_view(request):
    return render(request, 'index.html')


def create_manna_view(request):
    form = MannaForm()
    if request.method == "POST":
        form = MannaForm(request.POST)
        if form.is_valid():
            bible_verses = form.cleaned_data.get('bible_verses')
            chapter = int(form.cleaned_data.get('chapter_of_bible_verse'))
            verse = form.cleaned_data.get('verse_of_chapter')

            verse = verse.split('-')
            verseFrom = int(verse[0])
            verseTo = int(verse[1])

            url = "https://ajith-holy-bible.p.rapidapi.com/GetVerses"

            querystring = {"VerseTo": verseTo, "VerseFrom": verseFrom, "chapter": chapter, "Book": bible_verses}

            headers = {
                "X-RapidAPI-Host": "ajith-holy-bible.p.rapidapi.com",
                "X-RapidAPI-Key": "be532bde6cmsh60515fab6019230p1ab77djsn2e6ba45ca46d"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            data = response.json()
            manna = form.save(commit=False)
            manna.display_verse = data['Output']
            manna.user = request.user
            manna.save()

            return redirect('dashboard')
    return render(request, 'trial.html', {'form': form})


def update_manna_view(request, pk):
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


class MannaDetailView(HitCountDetailView):
    model = Manna
    template_name = 'main/manna_detail.html'
    slug_field = 'slug'
    count_hit = True
    context_object_name = 'manna'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'popular_posts': Manna.objects.order_by('-hit_count_generic__hits')[:3],
            'other_manna': Manna.objects.filter()[:3]

        })
        return context


def user_profile_view(request, pk):
    user = User.objects.get(id=pk)
    manna = user.manna_set.all()

    context = {
        'user': user,
        'manna': manna

    }
    return render(request, 'profile.html', context)


def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'email or password not authentic 🤨')

    context = {
        'page': page
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
            user_form = form.save(commit=False)
            user_form.first_name = user_form.first_name.capitalize()
            user_form.last_name = user_form.last_name.capitalize()
            user_form.save()
            messages.success(request, 'Account Created as successfully,Login to continue 😁😉')
            return redirect('login-view')
        else:
            messages.error(request, 'Error Processing Registration 😔')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def password_reset_view(request):
    form = PasswordResetForm()
    context = {
        'form': form
    }
    return render(request, 'trial.html', context)


def password_change_form(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('login-view')
        else:
            form = PasswordChangeForm(user=request.user)

    context = {
        'form': form
    }
    return render(request, 'password_change.html', context)


def password_reset_view(request):
    form = PasswordResetForm()

    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('email')
            user = User.objects.filter(email=data)

            if user.exists():
                pass


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_rest_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy("dashboard")
