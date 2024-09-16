import tensorflow as tf
from PIL import Image
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .models import DigitImage
from .serializers import DigitImageSerializer

# Load the pre-trained MNIST model
model = tf.keras.models.load_model('mnist_model.h5')

def preprocess_image(image_path):
    # Check if the image exists at the provided path
    try:
        img = Image.open(image_path).convert('L').resize((28, 28))
        img_array = np.array(img) / 255.0
        return img_array.reshape(1, 28, 28, 1)
    except Exception as e:
        print(f"Error in processing image: {e}")
        return None


class PredictDigit(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES['image']
        file_name = default_storage.save(image_file.name, image_file)
        digit_image = DigitImage.objects.create(image=file_name)

        # Preprocess the image and make the prediction
        processed_image = preprocess_image(digit_image.image.path)
        prediction = model.predict(processed_image)
        digit_image.predicted_digit = int(np.argmax(prediction))
        digit_image.save()

        # Return the prediction result as a JSON response
        serializer = DigitImageSerializer(digit_image)
        return Response(serializer.data)
