from django.db import models
from django.core.validators import FileExtensionValidator

class Travel_banner(models.Model):
    id = models.AutoField(primary_key=True)
    banner_text = models.CharField(max_length=255, default="Default Banner Text")
    banner_sub_text = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    banner_image = models.ImageField(upload_to='images_uploaded', null=True, blank=True) 
    def __str__(self):
        return f"{self.banner_text} {self.banner_sub_text}, {self.banner_image}"


class Travel_gallery(models.Model):
    id = models.AutoField(primary_key=True)
    gallery_image = models.ImageField(upload_to="image", default="jpg", blank=True)
    gallery_title = models.CharField(max_length=100,default="Armenia")  # Removed the comma
    gallery_text = models.TextField()
    gallery_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.gallery_image} {self.gallery_title}, {self.gallery_text} {self.gallery_price}"



class Booking(models.Model):
    place_name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    arrival_date = models.DateField()
    leaving_date = models.DateField()

    def __str__(self):
        return self.place_name


class Contact(models.Model):
    contact_svg = models.FileField(upload_to='svgs/')
    email_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    people_number = models.IntegerField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    

    def __str__(self):
        return self.email


# https://youtu.be/tUqUdu0Sjyc        # 

