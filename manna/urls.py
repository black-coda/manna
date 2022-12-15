from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from main.views import MannaListView, login_view, password_change_form, password_reset_view, register_view, logout_view, \
    user_profile_view, ResetPasswordView, update_user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('forum/', include("forum.urls")),
                  path('', RedirectView.as_view(url='dashboard/', permanent=True)),
                  path('dashboard/', include('main.urls')),
                  path('accounts/login/', login_view, name='login-view'),
                  path('accounts/register/', register_view, name='register-view'),
                  path('accounts/logout/', logout_view, name='logout-view'),
                  path('user-profile/<str:username>/', user_profile_view, name='profile'),
                  path('user-profile/<str:username>/update/', update_user_view, name='update_profile'),
                  path('accounts/password-reset/', ResetPasswordView.as_view(), name='password-reset-view'),
                  #   path('accounts/password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html') , name='password-reset'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
