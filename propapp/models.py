from django.db import models
from autoslug import AutoSlugField

#I created a postPost model
PLOTTYPE=(('Resale','resale'), ('Primary-Market Property','primarymarketroperty'))
class plotPost(models.Model):
    mainimage = models.ImageField(upload_to="propapp\images", blank = True, null = True)
    image1 = models.ImageField(upload_to="propapp\images", blank = True, null = True)
    image2 = models.ImageField(upload_to="propapp\images", blank = True, null = True)
    image3 = models.ImageField(upload_to="propapp\images", blank = True, null = True)
    ytvideo = models.TextField()
    heading = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    description = models.TextField()
    search_result = models.TextField()
    slug=AutoSlugField(populate_from='heading', unique = True, null=True, default = None)
    mobile_no = models.CharField(max_length=10)
    plot_type = models.CharField(max_length=100, choices=PLOTTYPE, default='Resale')
    plot_size = models.CharField(max_length=225)
    admap = models.TextField()
    
    
    def __str__(self):
        return self.heading
    
    
class contactInfo(models.Model):
    name_contact = models.CharField(max_length=50)
    mobile_contact = models.CharField(max_length=50)
    email_contact = models.CharField(max_length=50)
    city_contact = models.CharField(max_length=50)
    location_contact = models.CharField(max_length=50)
    message_contact = models.TextField()
        
    def __str__(self):
            return self.name_contact
        