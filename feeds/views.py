from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }

    return render(request, 'home_page.html', context)
# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Contact Form Submission From Portfolio',
                f'Your Name: {name}\n\nYour Email: {email}\n\nMessage: {message}',
                'portfolio@gmail.com',  # Your email address
                ['yaminlambappi@gmail.com'],  # Your email address or a list of recipient email addresses
                fail_silently=False,
            )
            return render(request, 'thank_you.html')  # Render a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
