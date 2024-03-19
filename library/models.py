from django.db import models
from authors.models import Author
class Book (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10, null=True)
    image = models.ImageField(upload_to='library/images/',null=True)
    no_ofpages = models.IntegerField(default=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True, related_name='library')
    
    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return f'/media/{self.image}'



    


