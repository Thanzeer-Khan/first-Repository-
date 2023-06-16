from django.shortcuts import render,redirect
from myapp.models import categorydb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from myapp.models import productdb
from django.contrib import messages

# Create your views here.
def indexfn(request):
    return render(request,"indexpage.html")
def categoryfn(request):
    return render(request,"addcategory.html")
def savedata(request):
    if request.method=="POST":
        cn=request.POST.get('Category Name')
        img=request.FILES['Image']
        des=request.POST.get('Description')
        obj=categorydb(Category_Name=cn,image=img,Description=des)
        obj.save()
        messages.success(request,'category saved successfully')
    return redirect(categoryfn)
def categorydisplay(request):
    data = categorydb.objects.all()
    return render(request, 'categorydisplay.html',{'data': data})
def editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(request,'editcategory.html',{'data':data})
def updatefn(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('Category Name')
        des = request.POST.get('Description')
    try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
    except MultiValueDictKeyError:
        file = categorydb.objects.get(id=dataid).image
    categorydb.objects.filter(id=dataid).update(Category_Name=cn,Description=des,image=file)
    return redirect(categorydisplay)
def deletefn(request,dataid):
        data=categorydb.objects.filter(id=dataid)
        data.delete()
        return redirect(categorydisplay)
def productfn(request):
    data= categorydb.objects.all()
    return render(request,"product.html",{'data':data})
def savedata2(request):
    if request.method=="POST":
        cn=request.POST.get('Category Name')
        pn=request.POST.get('Product Name')
        img=request.FILES['Pro Image']
        pr=request.POST.get('Price')
        des=request.POST.get('Description')
        obj=productdb(category_Name=cn,Product_Name=pn,Pro_image=img,Price=pr,Description=des)
        obj.save()
    return redirect(productfn)
def productdisplay(request):
    data=productdb.objects.all()
    return render(request,"productdisplay.html",{'data':data})
def editproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    cat=categorydb.objects.all()
    return render(request,'editproduct.html',{'data':data, 'cat':cat})
def updatefn2(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('Category Name')
        pn= request.POST.get('Product Name')
        pr= request.POST.get('Price')
        des = request.POST.get('Description')
    try:
            img = request.FILES['ProImage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
    except MultiValueDictKeyError:
        file = productdb.objects.get(id=dataid).Pro_image
    productdb.objects.filter(id=dataid).update(category_Name=cn,Product_Name=pn,Price=pr,Description=des,Pro_image=file)
    return redirect(productdisplay)

def deletefn2(request, dataid):
        data = productdb.objects.filter(id=dataid)
        data.delete()
        return redirect(productdisplay)