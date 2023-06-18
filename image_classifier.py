import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
import cv2


def image_categorizer(image):
    model = load_model(
        r'C:\Users\ambar\Documents\Projects\Trash-Talk\model.h5')
    img = cv2.imread(
        image)
    resize = tf.image.resize(img, (224, 224))
    prediction_array = model.predict(np.expand_dims(resize/223, 0))
    category_number = np.argmax(prediction_array)

    if category_number in [0, 10]:
        return "black"
    if category_number == 1:
        return "green"
    else:
        return "blue"


image_categorizer(
    r"C:\Users\ambar\Downloads\archive (5)\garbage_classification\clothes\clothes4.jpg")

# the print statement isnt needed, it is just for debugging and testing
# print(image_categorizer(
#     r"C:\Users\ambar\Downloads\archive (5)\garbage_classification\clothes\clothes4.jpg"))
