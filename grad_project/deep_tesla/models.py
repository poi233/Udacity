import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Lambda, BatchNormalization, ZeroPadding2D, Convolution2D, Activation
from keras import initializers
from keras import optimizers
from keras.callbacks import ModelCheckpoint, EarlyStopping

def get_model_one(keep_prob, learning_rate):
    # Hyperparameters
    keep_prob = keep_prob
    learning_rate = learning_rate
    input_shape = (66, 200, 3)
    # model
    model_one = Sequential()
    model_one.add(Conv2D(filters=24, kernel_size=5, strides=2, padding='valid', activation='relu', input_shape=input_shape))
    model_one.add(Conv2D(filters=36, kernel_size=5, strides=2, padding='valid', activation='relu'))
    model_one.add(Conv2D(filters=48, kernel_size=5, strides=2, padding='valid', activation='relu'))
    model_one.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='valid', activation='relu'))
    model_one.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='valid', activation='relu'))
    model_one.add(Flatten())
    model_one.add(Dense(units=1160, activation='relu'))
    model_one.add(Dropout(keep_prob))
    model_one.add(Dense(units=100, activation='relu'))
    model_one.add(Dropout(keep_prob))
    model_one.add(Dense(units=50, activation='relu'))
    model_one.add(Dense(units=10, activation='relu'))
    model_one.add(Dense(units=1,))
    adam = optimizers.Adam(lr=learning_rate)
    model_one.compile(loss='mse', optimizer=adam)
    return model_one

def get_model_two(keep_prob, learning_rate):
    # Hyperparameters
    keep_prob = keep_prob
    learning_rate = learning_rate
    input_shape = (66, 200, 3)
    # model
    model_two = Sequential()
    model_two.add(
        Conv2D(filters=16, kernel_size=3, strides=1, padding='valid', activation='relu', input_shape=input_shape))
    model_two.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
    model_two.add(Conv2D(filters=32, kernel_size=3, strides=1, padding='valid', activation='relu'))
    model_two.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
    model_two.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='valid', activation='relu'))
    model_two.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
    model_two.add(Flatten())
    model_two.add(Dense(units=1024))
    model_two.add(BatchNormalization())
    model_two.add(Activation('relu'))
    model_two.add(Dropout(keep_prob))

    model_two.add(Dense(units=512))
    model_two.add(BatchNormalization())
    model_two.add(Activation('relu'))
    model_two.add(Dropout(keep_prob))

    model_two.add(Dense(units=128))
    model_two.add(BatchNormalization())
    model_two.add(Activation('relu'))
    model_two.add(Dropout(keep_prob))

    model_two.add(Dense(units=32))
    model_two.add(BatchNormalization())
    model_two.add(Activation('relu'))
    model_two.add(Dropout(keep_prob))

    model_two.add(Dense(units=1))
    adam = optimizers.Adam(lr=learning_rate)
    model_two.compile(loss='mse', optimizer=adam)
    return model_two