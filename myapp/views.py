from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def logout(request):
    return render(request, "logout.html")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page after successful login
        else:
            messages.error(request, "Invalid username or password")  # Show error if authentication fails

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('login')  # Redirect to a homepage or dashboard after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     print(f"Form is valid: {form.cleaned_data}")  # Print form data
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     print(f"Form errors: {form.errors}")  # Print form errors
    #     return super().form_invalid(form)
    def form_valid(self, form):
        # Save the new user to the database
        user = form.save()

        # Send a welcome email to the user
        user.email_user(
            'Welcome to Our Site',  # Subject of the email
            'Thank you for registering with us. We are excited to have you on board!'  # Body of the email
        )

        # Optionally, add a success message
        messages.success(self.request, 'Your account has been created successfully! You can now log in.')

        # Redirect to success_url (login page in this case)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)