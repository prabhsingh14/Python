from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('masala', 'Masala Chai'),
        ('ginger', 'Ginger Chai'),
        ('cardamom', 'Cardamom Chai'),
        ('lemon', 'Lemon Chai'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=CHAI_TYPE_CHOICE, default='masala')
    description = models.TextField(default='A delicious variety of chai.')

    def __str__(self):
        return self.name
    
# One to many
class ChaiReview(models.Model):
    #CASCADE: If a chai is deleted, all its reviews will be deleted
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"Review for {self.chai.name} by {self.user.username}"

# Many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name

#One to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    issued_to = models.CharField(max_length=100)
    issued_on = models.DateField(auto_now_add=True)
    valid_until = models.DateField()
 
    def __str__(self):
        return f"Certificate for {self.chai.name} issued to {self.issued_to}"