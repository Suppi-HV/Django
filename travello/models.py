from django.db import models # type: ignore
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.auth.models import User# type: ignore
#  # type: ignore

# # Create your models here.
# # class Destination:
#     id:int
#     name:str
#     img:str
#     desc:str
#     price:int
#     offer:bool

# class Destination(models.Model):
#     id =models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=100,)
#     img=models.ImageField()
#     desc = RichTextField()
#     price=models.IntegerField()
#     offer=models.BooleanField(default=False)

# travello/models.py

  # Import CKEditor for rich text field

class Destination(models.Model):
    # Define your fields
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='destinations/')  # Upload images to 'media/destinations/'
    desc = RichTextUploadingField()  # CKEditor field for rich text content
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# class Comments(models.Model):
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)  




# from django.db import models
# from django.contrib.auth.models import User

# class Comments(models.Model):
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.comment
    
#     class Meta:
#         ordering = ['created_at']

# from django.db import models
# from django.contrib.auth.models import User
# from .models import Destination  # type: ignore # Ensure you import Destination properly.

# class Comments(models.Model):
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     # New fields for likes and dislikes
#     likes = models.PositiveIntegerField(default=0)
#     dislikes = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.comment

#     class Meta:
#         ordering = ['created_at']

from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # ManyToManyFields for likes and dislikes
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="comment_dislikes", blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['created_at']
