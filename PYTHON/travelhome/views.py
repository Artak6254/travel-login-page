from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Travel_banner, Travel_gallery, Booking, Contact
from .forms import BookingForm, ContactForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url='login')  sa decoratora sa nshum en account vra vor urli mej grenq account
# @chtani accounti ej@
def index(request):
    banner_data = Travel_banner.objects.all()
    pack = Travel_gallery.objects.all()
    context = {
        "data_banners": banner_data,
        "pack": pack
    }
    return render(request, "travelhome/index.html", context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('success', booking_id=booking.id)
        else:
            print("Form is not valid.",request.POST)
  

def success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'travelhome/success.html', {'booking': booking})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_success', contact_id=contact.id)
        else:
            print("Form is not valid.", request.POST)
            return render(request, 'travelhome/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'travelhome/contact.html', {'form': form})

def contact_success(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'travelhome/contact.html', {'contact': contact})




def registerPage(request):
    if request.user.is_authenticated:
        return redirect('')
    else:    
        form = CreateUserForm()  # Use custom form with email
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')

                return redirect('login')  # Redirect to login page after registration

        context = {'form': form}        
        return render(request, 'travelhome/register.html', context)


            

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('account')#tox tani account
    else:    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('account')
            else:
                messages.info(request, 'Username and password incorrect')    
        
        context = {}
        return render(request, 'travelhome/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')    


@login_required
def accountPage(request):
    return render(request, 'travelhome/account.html', {'user': request.user})
