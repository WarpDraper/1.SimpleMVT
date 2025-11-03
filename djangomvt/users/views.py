from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout

from .forms import CustomUserCreationForm
from .utils import compress_image
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                if 'image' in request.FILES:
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(40, 40))
                    user.image_ava.save(image_name, optimized_image, save=False)
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(300, 300))
                    user.image_small.save(image_name, optimized_image, save=False)
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(800, 800))
                    user.image_medium.save(image_name, optimized_image, save=False)
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(1200, 1200))
                    user.image_large.save(image_name, optimized_image, save=False)
                user.save()
                return redirect('categories:show_categories')
            except Exception as e:
                messages.error(request, f'Помилка при реєстрації: {str(e)}')
        else:
            messages.success(request, 'Виправте помилки в формі')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})\

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Вітаю, {user.username}!")
            return redirect('categories:show_categories')
        else:
            messages.error(request, "Невірний логін або пароль")
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, "Ви вийшли з акаунта")
    return redirect('homepage')