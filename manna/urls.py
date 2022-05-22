from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from main.views import MannaListView, login_view, password_change_form, password_reset_view, register_view, logout_view,user_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='dashboard/',permanent=True)),
    path('dashboard/', include('main.urls')),
    path('accounts/login/', login_view, name='login-view'),
    path('accounts/register/',register_view, name='register-view'),
    path('accounts/logout/',logout_view, name='logout-view'),
    path('user-profile/<int:pk>/', user_profile_view, name='profile')
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
