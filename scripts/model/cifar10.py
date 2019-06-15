import keras
import pickle
import os.path
import numpy as np
# import matplotlib.pyplot as plt
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.optimizers import Adam
# from keras.callbacks import ModelCheckpoint
# from keras.callbacks import LambdaCallback
# from keras.callbacks import TensorBoard
# from tensorboardcolab import TensorBoardColab, TensorBoardColabCallback
from sklearn.preprocessing import LabelBinarizer

# Hyperparameters
batch_size = 128
num_classes = 10
epochs = 1000
# epoch_file="gdrive/My Drive/colab/hw8_1_epoch_num.txt"
# data_file="gdrive/My Drive/colab/hw8_1_data.txt"
# filepath="gdrive/My Drive/colab/hw8_1_weights.best.hdf5"
# tbc=TensorBoardColab()

# Load CIFAR10 Data
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print(x_train.shape)
# t = 1 / 0
img_height, img_width, channel = x_train.shape[1],x_train.shape[2],x_train.shape[3]

# convert to one hot encoing 
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# AlexNet Define the Model
model = Sequential()
# model.add(Conv2D(96, (11,11), strides=(4,4), activation='relu', padding='same', input_shape=(img_height, img_width, channel,)))
# for original Alexnet
model.add(Conv2D(48, (3,3), strides=(2,2), activation='relu', padding='same', input_shape=(img_height, img_width, channel,)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2,2)))
# Local Response normalization for Original Alexnet
model.add(BatchNormalization())

model.add(Conv2D(96, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))
# Local Response normalization for Original Alexnet
model.add(BatchNormalization())

model.add(Conv2D(192, (3,3), activation='relu', padding='same'))
model.add(Conv2D(192, (3,3), activation='relu', padding='same'))
model.add(Conv2D(256, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))
# Local Response normalization for Original Alexnet
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dense(512, activation='tanh'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='tanh'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))


# print the model summary
model.summary()

report_data = {
    "acc":[],
    "val_acc":[],
    "loss":[],
    "val_loss":[]
}

num_epoch = 0
# if not os.path.isfile(epoch_file):
#   with open(epoch_file, "w+") as file:  
#     file.write(str(num_epoch))
# else:
#   with open(epoch_file, "r") as file:  
#     num_epoch = int(file.read())

# if os.path.isfile(filepath):
#   model.load_weights(filepath)

# if os.path.isfile(data_file):
#   with open(data_file, "rb") as file:
#     report_data = pickle.load(file)

# determine Loss function and Optimizer
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
raise AssertionError
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])


# def updateEpoch(epoch, logs):
#   to_save = num_epoch + epoch + 1
#   report_data['acc'].append(logs['acc'])
#   report_data['loss'].append(logs['loss'])
#   report_data['val_acc'].append(logs['val_acc'])
#   report_data['val_loss'].append(logs['val_loss'])
#   with open(epoch_file, "w") as file:  
#     file.write(str(to_save))
#   with open(data_file, "wb") as file:
#     pickle.dump(report_data, file)
#   print(epoch, logs)
# checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
# lambdaCall = LambdaCallback(on_epoch_end=updateEpoch)
# callbacks_list = [checkpoint,lambdaCall,TensorBoardColabCallback(tbc)]

# Train the Model

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=(epochs - num_epoch),
                    verbose=1,
                    # callbacks=callbacks_list,
                    validation_data=(x_test, y_test))
