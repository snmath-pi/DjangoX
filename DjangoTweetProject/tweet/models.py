from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    photo=models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'

from django.db.models.signals import post_save
from django.dispatch import receiver  
from PIL import Image 
@receiver(post_save, sender=Tweet)
def resize_photo(sender, instance, **kwargs):
    if instance.photo:
        img = Image.open(instance.photo.path)
        img.thumbnail((300, 300))  # Resize the image to fit within 300x300 pixels
        img.save(instance.photo.path)
        
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=('username','email','password1','password2')