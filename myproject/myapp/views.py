from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from myapp.models import contactUs as contactUsModel



def contactUs(request) : 
    if request.method =='POST' :
        fullName = request.POST.get('full_name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        en = contactUsModel(contactFullName=fullName, contactEmail=email, contactPhoneNumber=phoneNumber, contactSubject=subject, contactMessage=message)
        en.save()
        return HttpResponse("Thanks for contacting")
        
    return render(request, "contact.html")


def adminDashboard(request):
    return render(request, 'recycle.html')


#Contact Display
def displayContactView(request):
    contacts = contactUsModel.objects.filter()
    
    args = {
        "contacts": contacts,  
    }
    return render(request, "contactAdmin.html",args)


#Read contact   
def deleteContact(request, slug):
    certificate = contactUsModel.objects.get(id=slug)
    certificate.delete()

        # Appending the search query for nearby lakes to the Google Maps URL
    return redirect('displayContact')