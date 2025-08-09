from django.db import models
from django.utils import timezone

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