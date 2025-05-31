from django.shortcuts import render, redirect

from django.utils import timezone
from .models import Sermon, Event
from .forms import SermonForm, EventForm, ContactForm, AdminLoginForm
from django.contrib import messages
from .forms import SermonForm  # You'll need to create this form
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from newject.forms import AdminLoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class AdminLoginView(LoginView):
    template_name = 'newject/admin_login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return self.request.GET.get('next', '/admin/')



def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
    else:
        form = AdminLoginForm()
    return render(request, 'newject/admin_login.html', {'form': form, 'type': 'login'})

@login_required
def admin_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def home(request):
    featured_events = Event.objects.filter(is_featured=True, start_date__gte=timezone.now()).order_by('start_date')[:3]
    latest_sermons = Sermon.objects.all().order_by('-date_preached')[:3]
    return render(request, 'newject/home.html', {
        'featured_events': featured_events,
        'latest_sermons': latest_sermons
    })

def sermons(request):
    sermons = Sermon.objects.all().order_by('-date_preached')
    return render(request, 'newject/sermons.html', {'sermons': sermons})


def events(request):
    upcoming_events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    past_events = Event.objects.filter(start_date__lt=timezone.now()).order_by('-start_date')
    return render(request, 'newject/events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event added successfully!')
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'newject/admin_login.html', {'form': form, 'type': 'event'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'newject/contact.html', {'form': form})
