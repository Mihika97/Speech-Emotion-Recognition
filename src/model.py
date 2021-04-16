

import keras
import tensorflow as tf
from keras.models import Sequential, Model
from keras.layers import Dense, Embedding, Conv1D, Conv2D, MaxPooling1D, AveragePooling1D, BatchNormalization, \
    Input, Flatten, Dropout, Activation


# 7 layered Deep Neural net using sequential
def ml_model():
    model = keras.Sequential()
    model.add(Conv1D(256, 5, padding='same', input_shape=(188, 1)))

    model.add(Activation('relu'))
    model.add(Conv1D(128, 5, padding='same'))

    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling1D(pool_size=8))

    model.add(Conv1D(128, 5, padding='same'))

    model.add(Activation('relu'))
    model.add(Conv1D(128, 5, padding='same'))

    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(10))
    model.add(Activation('softmax'))

    opt = tf.keras.optimizers.RMSprop(lr=0.0001, decay=1e-6)
    return model, opt
