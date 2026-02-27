import tensorflow as tf
from tensorflow.keras import layers

def get_model():
    IMG_SIZE = 380

    augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2)
    ])

    input = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
    x = augmentation(input)
    x = tf.keras.applications.efficientnet.preprocess_input(x)

    model = tf.keras.applications.EfficientNetB4(
            include_top=False,
            weights='imagenet',
            input_tensor=x
    )
    model.trainable = False

    x = layers.GlobalAveragePooling2D()(model.output)
    output = layers.Dense(7, activation="softmax")(x)

    return tf.keras.Model(inputs=model.input, outputs= output)
