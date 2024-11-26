from django.shortcuts import render,redirect
from .models import * 

def Send(request):
    if request.method =="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']
        SMS.objects.create(name=name,phone=phone,email=email,text=text)

        return redirect('/index/')

def About(request):
    context = {
        'et':Et.objects.first(),
        'stat':Stat.objects.first(),
        'est':Est.objects.all(),
        'team':Team.objects.all(),
        'timon':Timon.objects.all(),

    }
    return render(request, 'about.html',context)

def Blogdetails(request):
    return render(request, 'blog-details.html')

def Blog(request):
    context = {
        'blog1':Blog1.objects.all()
    }
    return render(request, 'blog.html',context)

def Contact(request):
    context = {
        'col':Col.objects.all(),
    }
    return render(request, 'contact.html',context)

def Index(request):
    context = {
        'welcome':Welcome.objects.first(),
        'minus':Minus.objects.first(),
        'cons':Cons.objects.all(),
        'service':Service.objects.all(),
        'enim':Enim.objects.all(),
        'mod':Mod.objects.first(),
        'ho':Ho.objects.first(),
        'tu':Tu.objects.first(),
        'biz':Biz.objects.first(),
        'test':Test.objects.all(),
        'blog1':Blog1.objects.all(),
        }
    return render(request, 'index.html',context)

def Projectdetails(request):
    context={
        'rasm':Rasm.objects.all(),
        'this':This.objects.first(),
        'project':Project.objects.first(),

    }
    return render(request, 'project-details.html',context)

def Projects(request):
    return render(request, 'projects.html')

def Servicedetails(request):
    return render(request, 'service-details.html')

def Services(request):
    context = {
        'service':Service.objects.all(),
        'omnis':Omnis.objects.all(),
        'enim':Enim.objects.all(),
        'test':Test.objects.all(),
        
    }
    return render(request, 'services.html',context)

def Starterpage(request):
    return render(request, 'starter-page.html')
# Create your views here.
