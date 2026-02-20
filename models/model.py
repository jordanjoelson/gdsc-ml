import tensorflow as tf
from tensorflow.keras import layers

def get_model():
    model = tf.keras.application.EfficientNetB4(
            include_top=False,
            weights='imagenet',
            input_shape=(380, 380, 3)
    )
    
    x = layers.GlobalAveragePooling2D()(model.output)
    output = layers.Dense(7, activation="softmax")(x)

    return tf.keras.Models(inputs=model.input, outputs= output)
