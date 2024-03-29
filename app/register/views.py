from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})