from django.db import models

class Text(models.Model):
    text_title = models.CharField(max_length=30)
    text_content= models.CharField(max_length=500)
    photo_name=models.CharField(max_length=30)
    def __unicode__(self):             
        return self.text_title                           

class PhotoTextMap(models.Model):
     PhotoTextMap_texttitle=models.CharField(max_length=30)           
     PhotoTextMap_phototype = models.CharField(max_length=30)
     PhotoTextMap_phototitle= models.CharField(max_length=30)
     def __unicode__(self):             
         return self.PhotoTextMap_texttitle
