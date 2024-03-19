from django.shortcuts import reverse, get_object_or_404
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    image = models.ImageField(upload_to='authors/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self) -> str:
        url = reverse("authorprofile", args=[self.id])
        return url
    
    @property
    def create_url(self):
        url = reverse('create_author')
        return url
    
    @property
    def list_url(self):
        url = reverse('listauthors')
        return url
    
    @property
    def edit_url(self):
        url = reverse('edit_author', args=[self.id])
        return url
    
    @property
    def del_url(self):
        url = reverse('delete_author', args=[self.id])
        return url

    @classmethod
    def create_object(cls,name, birth_date , image ):
        try:
            author = cls(name=name, ebirth_date=birth_date,image=image)
            print(name, birth_date, image)
            author.save()
        except Exception as e:
            print(e)
            return False
        else:
            return author
    
    @classmethod
    def get_all_authors(cls):
        return cls.objects.all()

    @classmethod
    def get_sepcific_author(cls, id):
        return get_object_or_404(cls,id=id)