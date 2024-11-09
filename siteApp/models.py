from django.db import models
from PIL import Image

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img = img.resize((450, 350))  # Resize to specific ratio
        img.save(self.image.path)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)  # e.g., CEO, Developer
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')  # Store images in 'media/clients/'
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img = img.resize((450, 350))  # Resize to specific ratio
        img.save(self.image.path)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


