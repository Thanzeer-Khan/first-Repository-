from django.shortcuts import render,redirect
from myapp.models import categorydb
from myapp.models import productdb
from myapp2.models import cartdb,checkdb,registrationdb



# Create your views here.
def homefn(request):
    data= categorydb.objects.all()
    return render (request,"homepage.html", {'data':data})

def profn(request,cat):
    head=categorydb.objects.filter(Category_Name=cat)
    data=productdb.objects.filter(category_Name=cat)
    return render(request,'productpage.html',{'data':data, 'head':head})
def singlefn(request,pro):
    data=productdb.objects.get(id=pro)
    return render(request,'singlepage.html',{'data':data})

def logfn(request):
    return render(request,'loginpage.html')
def signinfn(request):
    return render(request,'signin page.html')
def registrationsave(request):
    if request.method=="POST":
        un=request.POST.get('User Nmae')
        pd=request.POST.get('password')
        em=request.POST.get('Email ID')
        mob=request.POST.get('Mobile Number')
        img=request.POST.get('Profile Image')
        obj=registrationdb(User_Name=un,Password=pd,Email_ID=em,Phone_Number=mob,Profile_Image=img)
        obj.save()
        return redirect(homefn)
def cartfn2(request):
    data= cartdb.objects.all()
    return render(request,'mycart.html',{'data':data})
def savedata1(request):
    if request.method=="POST":
        pn=request.POST.get('product_name')
        des=request.POST.get('description')
        qty=request.POST.get('quantity')
        pr=request.POST.get('price')
        tp=request.POST.get('totalprice')
        obj=cartdb(product_name=pn,description=des,quantity=qty,price=pr,total_price=tp)
        obj.save()
        return redirect(cartfn2)
def delcart(request, dataid):
        data = cartdb.objects.filter(id=dataid)
        data.delete()
        return redirect(cartfn2)
def checkoutfn(request):
    return render(request,'checkout.html')
def checkoutsave(request):
    if request.method=="POST":
        fn=request.POST.get('First Name')
        sn=request.POST.get('second Name')
        em=request.POST.get('Email Id')
        pn=request.POST.get('Phone Number')
        ds=request.POST.get('District')
        obj=checkdb(First_Name=fn,second_Name=sn,Email=em,Phone_number=pn,District=ds)
        obj.save()
        return redirect(checkoutfn)