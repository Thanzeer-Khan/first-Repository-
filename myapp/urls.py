from django.urls import path
from myapp import views

urlpatterns = [
path('indexfn/',views.indexfn,name="indexfn"),
path('categoryfn/',views.categoryfn,name="categoryfn"),
path('savedata/',views.savedata,name="savedata"),
path('categorydisplay/',views.categorydisplay,name="categorydisplay"),
path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
path('updatefn/<int:dataid>/',views.updatefn,name="updatefn"),
path('deletefn/<int:dataid>/',views.deletefn,name="deletefn"),
path('productfn/',views.productfn,name="productfn"),
path('savedata2/',views.savedata2,name="savedata2"),
path('productdisplay/',views.productdisplay,name="productdisplay"),
path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
path('updatefn2/<int:dataid>/',views.updatefn2,name="updatefn2"),
path('deletefn2/<int:dataid>/',views.deletefn2,name="deletefn2")


]