from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)