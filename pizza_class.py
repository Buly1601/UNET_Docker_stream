import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image as i



class FoodClassification:

    def __init__(self):
        self.model = tf.keras.models.load_model("pizza_steak.keras")
        self.image = None
        self.masked_image = None


    def main(self, image):
        # Parse and preprocess the image
        self.parse_image(image)
        # Get get prediction
        prediction = self.model.predict(self.image)
        if prediction >= 0.5:
            return "steak"
        else:
            return "pizza"


    def parse_image(self, image):
        """
        The images have to be resized and normalized; this function will 
        return a prepared image to be used by the model.
        """
        img = i.load_img(image, target_size=(224, 224))
        self.image = i.img_to_array(img)
        self.image = np.expand_dims(self.image, axis=0)  # Add batch dimension
        self.image /= 255.0  # Normalize image


if __name__ == "__main__":
    img = ""
    food = FoodClassification()
    food.main(img)
