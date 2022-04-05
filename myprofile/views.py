from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact, Skills
from .models import Testimonials
from .models import Intrests
from .models import Social
from .models import Service
from .models import Portfolio
from .models import Status
from .models import Education
from .models import About
from .models import Experience
from .forms import ContactForm


# Create your views here.
def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Your Message has been submitted')
        return redirect('/')
    
    show_skill = Skills.objects.all()
    show_testi = Testimonials.objects.all()
    show_intrest = Intrests.objects.all()
    show_social = Social.objects.all()
    show_service = Service.objects.all()
    show_portfolio = Portfolio.objects.all()
    show_status = Status.objects.all()
    show_education = Education.objects.all()
    show_about = About.objects.all()
    show_experience = Experience.objects.all()
    c = Portfolio.objects.count()
    return render(request, "index.html", 
                  {
                      'show_skill':show_skill,
                      'show_testi':show_testi,
                      'show_intrest':show_intrest,
                      'show_social':show_social,
                      'show_service':show_service,
                      'show_portfolio':show_portfolio,
                      'show_status':show_status,
                      'show_education':show_education,
                      'show_about':show_about,
                      'show_experience': show_experience,
                      'c':c,
                      'form':ContactForm(request.POST or None)
                      })

    
    
def portfolio_details(request,id):
    show_portfolio_detail = Portfolio.objects.get(pk=id)
    return render(request, "portfolio_details.html", 
                  {
                      'show_portfolio_detail':show_portfolio_detail
                  })
    
    

    
    
# def sendmail(request):
#     if request.method =="POST":
#         subject = request.POST['subject']
#         message = request.POST['message']
        
#         send_mail(
#             # name, # your name
#             # #email, # from email
#             subject , # subject
#             message, # message
#             'shreesranak@gmail.com',
#             ['kshrees117@gmail.com'],
#             fail_silently=False,
#         )
#         messages.info(request, "mail sent")
#         return render(request, 'index.html')
#     else:
#         messages.info(request, "mail sent")
#         return render(request, 'index.html')
    
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         contact=Contact.objects.create(name=name,email=email,subject=subject,message=message)
#         contact.save()
#         messages.success(request,'Message has been submitted')
#     else:
#         messages.success(request,'Message has not been submitted')
#     return render(request,'message.html')

def contact(request):
    form = ContactForm()
    context={
        "form":form,
    }
    return render(request, '/', context)