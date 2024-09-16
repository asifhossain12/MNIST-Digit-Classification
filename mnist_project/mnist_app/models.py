# Create your models here.
from django.db import models

class DigitImage(models.Model):
    image = models.ImageField(upload_to='images/')
    predicted_digit = models.IntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}: Predicted Digit {self.predicted_digit}"
