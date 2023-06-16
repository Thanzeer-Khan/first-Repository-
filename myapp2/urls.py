from django.urls import path
from myapp2 import views

urlpatterns=[
path('homefn/',views.homefn,name="homefn"),
path('profn/<cat>/',views.profn,name="profn"),
path('singlefn <pro>/',views.singlefn,name="singlefn"),
path('cartfn2/',views.cartfn2,name="cartfn2"),
path('savedata1/',views.savedata1,name="savedata1"),
path('logfn/',views.logfn,name="logfn"),
path('signinfn/',views.signinfn,name="signin"),
path('registrationsave/',views.registrationsave,name="registrationsave"),
path('delcart/ <int:dataid>',views.delcart,name="delcart"),
path('checkoutfn/',views.checkoutfn, name="checkoutfn"),
path('checkoutsave/',views.checkoutsave, name="checkoutsave"),

]