from django.shortcuts import render
from django.http import HttpResponse
from photologue.models import *
from django.shortcuts import render_to_response
from django.conf import settings
import os
from PIL import Image
import datetime
from .models import Text
from .models import PhotoTextMap

def upload(request):
    return render(request,'example1/upload.html')

def allupload(request):
    try:
        f=request.FILES['xinwentuxiang']
        if f.size > 5000000:
          return HttpResponse("it is large!")
        try:
          parser=ImageFile.Parser()
          for chunk in f.chunks():
            parser.feed(chunk)
          img=parser.close()
        except IOError:
          return HttpResponse("it is an io error!")
        imageName='photologue/photos/'+f.name
        name=settings.STATIC_PATH+'/'+imageName
        
        img=Image.open(f)
        img.save(name) 

    except UnicodeEncodeError:
        return render_to_response('example1/upload.html',{'image_error':"please use English"})

    now ='00TB'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    photoInfo=Photo(image=imageName,title=now,slug=now,is_public=True)
    photoInfo.save()

    phototype="0000"                    
                             

    try:
        f1=request.FILES['fengmiantuxiang']
        if f1.size > 5000000:
          return HttpResponse("it is large!")
        try:
          parser1=ImageFile.Parser()
          for chunk1 in f1.chunks():
            parser1.feed(chunk1)
          img1=parser1.close()
        except IOError:
          return HttpResponse("it is an io error!")
        imageName1='photologue/photos/'+f1.name
        name1=settings.STATIC_PATH+'/'+imageName1
        
        img1=Image.open(f1)
        img1.save(name1) 
    except UnicodeEncodeError:
        return render_to_response('example1/upload.html',{'image_error':"please use English"})

    now1 ='11TB'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    photoInfo1=Photo(image=imageName1,title=now1,slug=now1,is_public=True)
    photoInfo1.save()

    phototype1="0001"        

    title=request.POST['xinwenwenbenkuang']
    content=request.POST['xinwenwenbenyu']
    name=request.POST['tuxiangwenbenkuang']
    tt=Text()
    tt.text_title=title
    tt.text_content=content
    tt.photo_name=name
    tt.save()      

    pe=PhotoTextMap()
    pe.PhotoTextMap_texttitle=title
    pe.PhotoTextMap_phototype=phototype
    pe.PhotoTextMap_phototitle=now
    pe.save()

    pe1=PhotoTextMap()
    pe1.PhotoTextMap_texttitle=title
    pe1.PhotoTextMap_phototype=phototype1
    pe1.PhotoTextMap_phototitle=now1
    pe1.save() 

    return HttpResponse("it is ok!") 

def showall(request):
      photo_list= Photo.objects.all()
      text_list=Text.objects.all()
      phototextmap_list=PhotoTextMap.objects.all()
      return render_to_response('example1/showall.html',{'photo_list':photo_list,'text_list':text_list,'phototextmap_list':phototextmap_list})

def showmore(request,phototextmapPhotoTextMap_phototitle):
      m=phototextmapPhotoTextMap_phototitle
      pp=PhotoTextMap.objects.get(PhotoTextMap_phototitle=m)
      p=pp.PhotoTextMap_texttitle
      t=Text.objects.get(text_title=p)
      photo_list= Photo.objects.all()
      phototextmap_list=PhotoTextMap.objects.all()
      return render_to_response('example1/showmore.html',{'photo_list':photo_list,'phototextmap_list':phototextmap_list,'t':t})
