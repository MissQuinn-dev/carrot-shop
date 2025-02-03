from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from item.models import Category, Item

from .forms import SignupForm, ContactForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)  # Populate form with user input
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email="carrotshopstore@gmail.com",
                recipient_list=["quinngeorge22@gmail.com"],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("/contact/")

    return render(request, "core/contact.html", {"form": form})