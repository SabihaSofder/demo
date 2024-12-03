from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact  # Import the contact model


# If you want to use a ModelForm, define one in forms.py, otherwise just handle the POST manually.

def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # You can add validation here (e.g. check if fields are empty, or validate email format)

        if full_name and email and phone_number and subject and message:
            # Create a new Contact object and save it to the database
            con = contact(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                subject=subject,
                message=message
            )
            con.save()  # Save the object to the database
            return HttpResponse('thank_you')  # Redirect to a success page or show a message
        else:
            return render(request, 'contact.html', {
                'error': 'All fields are required'
            })
    
    return render(request, 'contact.html')

