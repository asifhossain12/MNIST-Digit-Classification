
from rest_framework import serializers
from .models import DigitImage

class DigitImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitImage
        fields = ['image', 'predicted_digit']  # Make sure 'predicted_digit' is included
