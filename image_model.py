import tensorflow as tf
import numpy as np
import cv2


base_dir = r"C:\Users\ambar\Downloads\archive (5)\garbage_classification"

IMAGE_SIZE = 224
BATCH_SIZE = 16

# pre=processing
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.1
)

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    validation_split=0.1
)

train_datagen = train_datagen.flow_from_directory(
    base_dir,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    subset='training'
)

test_datagen = test_datagen.flow_from_directory(
    base_dir,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    subset='validation'
)

cnn = tf.keras.Sequential()
cnn.add(tf.keras.layers.Conv2D(filters=64, padding='same', strides=2,
        kernel_size=3, activation='relu', input_shape=(224, 224, 3)))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=32, padding='same',
        strides=2, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=32, padding='same',
        strides=2, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2))

cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(12, activation='softmax'))

cnn.compile(optimizer=tf.keras.optimizers.Adam(),
            loss='categorical_crossentropy', metrics=['accuracy'])

cnn.fit(train_datagen, epochs=4, validation_data=test_datagen)

cnn.save(r'C:\Users\ambar\Documents\Projects\Trash-Talk\image_model.h5')
