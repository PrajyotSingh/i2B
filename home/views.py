from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Influencers,Brands

def home(request):
    return render(request,'home.html',{'name':'Shubham'})

def result(request):
    person=request.GET['person']
    context={'user':person}
    return render(request,'form.html',context)

def final(request):
    userr=request.POST['user']
    if userr=='influencer':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        username=request.POST['username']
        followers=request.POST['followers']
        category=request.POST['category']
        others=request.POST['others']
        
        inf=Influencers(FirstName=fname,LastName=lname,Email=email,Mobile=mobile,Username=username,Followers=followers,Category=category,Others=others)
        inf.save()
      
    elif userr=='brand':
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Email=request.POST['Email']
        Mobile=request.POST['Mobile']
        Brand=request.POST['Brand']

        brand=Brands(FirstName=Fname,LastName=Lname,Email=Email,Mobile=Mobile,BrandName=Brand)
        brand.save()

    messages.success(request,"Registered Successfully !! We will contact you soon !")
    return redirect('home')
    





