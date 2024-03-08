from django.shortcuts import render, HttpResponse
from propapp.models import plotPost
from propapp.models import contactInfo
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    plotData = plotPost.objects.all()
    context = {'plotData': plotData}
    return render(request, 'index.html',context)
    


def contact(request):
    if request.method == 'POST':
        name_contact = request.POST.get('name_contact')
        mobile_contact = request.POST.get('mobile_contact')
        email_contact = request.POST.get('email_contact')
        city_contact = request.POST.get('city_contact')
        location_contact = request.POST.get('location_contact')
        message_contact = request.POST.get('message_contact')

        # Save the contact info to the database
        contact = contactInfo(
            name_contact=name_contact,
            mobile_contact=mobile_contact,
            email_contact=email_contact,
            city_contact=city_contact,
            location_contact=location_contact,
            message_contact=message_contact
        )
        contact.save()

        # Send an email to the site administrator
        subject = f'New contact form submission from {name_contact}'
        message = f'''
            Hi Admin,

            Their is a Form Submission from  {name_contact}:
            Other Details given below, Contact them 
            Name: {name_contact}
            Mobile: {mobile_contact}
            Email: {email_contact}
            City: {city_contact}
            Location: {location_contact}
            Message: {message_contact}

            Thanks!
        '''
        from_email = 'propertymall247@gmail.com'
        recipient_list = ['riteshsmalviya03@gmail.com']
        
        
        send_mail(subject, message, from_email, recipient_list)

        # Show a success message to the user
        messages.success(request, 'We will reach out to you soon!')

    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html')

def plotBrief(request,plotid):
    plotData = get_object_or_404(plotPost, slug = plotid)
    context = {'plotData': [plotData]}
    return render(request, 'plotBrief.html', context)
    
    
def search(request):
    search = request.GET['search']
    plotData = plotPost.objects.filter(search_result__icontains=search)
    context = {'plotData': plotData}
    return render(request, 'search.html', context)

def price(request):
    return render(request, 'pricing.html')