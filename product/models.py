from django.db import models

# Create your models here. 

from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class category (MPTTModel):
    id_category = models.BigAutoField(primary_key=True)  
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')  
    type_category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_category
    
    class MPTTMeta:
      order_insertion_by = ['type_category']
    
class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    nom=models.CharField(max_length=150)
    image=models.ImageField(blank =True,upload_to='images/')
    description=models.CharField(max_length=500)
    prix=models.DecimalField(max_digits=8, decimal_places=2)
    stock= models.IntegerField()
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    image_tag.short_description='Image'
    
class Images(models.Model):
    product=models.ForeignKey(product, on_delete=models.CASCADE, related_name='images')
    nom=models.CharField(max_length=50, blank=True)
    image=models.ImageField(blank=True, upload_to='images/')
    
    def __str__(self): 
        return self.nom
    
    
    
    