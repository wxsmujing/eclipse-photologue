from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/$',views.upload,name='upload'),
    url(r'^allupload/$',views.allupload,name='allupload'),
    url(r'^showall/$',views.showall,name='showall'),
    #url(r'^showmore/(?P<phototitle>\d\d\w\w\d\d\d\d\d\d\d\d\d\d\d\d\d\d)/$',views.showmore),
    url(r'^showmore/(?P<phototextmapPhotoTextMap_phototitle>\w+([-+.]\w+)*\w+([-.]\w+)*\w+([-.]\w+)*)/$',views.showmore),                                                 
]
