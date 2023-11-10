from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'home.html')

# farmacia_online/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# farmacia_online/views.py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    # Personaliza la vista según sea necesario
    template_name = 'registration/login.html'


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

