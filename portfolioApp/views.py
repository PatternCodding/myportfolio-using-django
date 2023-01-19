from django.shortcuts import render
from .models import SideProfile,About, Duty,Testimonials,Client,Navbar,Blog, Portfolio,Contact,Education,Experience,Skill
from django.contrib.auth import authenticate
from django.http import HttpResponse


def Index(request):
    sideprofile = SideProfile.objects.latest('updated')
    
    
    # about
    edit = About.objects.all()
     
     
    
    # about
    duty = Duty.objects.all()
     
     
    # about
    testimonials = Testimonials.objects.all()
     
     
    # about
    client = Client.objects.all()
      
     
    # # Navbar
    navbar = Navbar.objects.all()
    
    # Education
    education = Education.objects.all()
    
    
    # Experience
    experience = Experience.objects.all()
    
    # Skill
    skill = Skill.objects.all()

     
    # # Navbar
    blog = Blog.objects.all()
    
     
    # # Portfolio
    port = Portfolio.objects.all()
    
    # contact
    if request.method == 'POST':
        contact = Contact()
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
            
        contact.fullname = fullname
        contact.email = email
        contact.messages = messages
        contact.save()
        return HttpResponse("<h1>Successfully Sent! tThanks for reaching us, we will get back to you sooner</h1>")
           
   
    context = {
        'sideprofile':sideprofile,
        'edit':edit,
        'duty':duty,
        'testimonials':testimonials,
        'client':client,
        'navbar':navbar,
        'port':port,
        'blog':blog,
        'education':education,
        'experience':experience,
        'skill':skill,
    }
    return render(request, 'portfolioApp/about.html', context)



def testing(request):
    
    return render(request, 'portfolioApp/testin.html')