from __future__ import print_function
import sys
import keras
import numpy as np
from keras.preprocessing import sequence


num_classes = 10.
# assume all dataset is channel last
    # x_train = x_train.reshape(60000, 784)
    # x_test = x_test.reshape(10000, 784)
def get_shape(shape_s):
    splits = shape_s.split(",")
    res = []
    for split in splits:
        res.append(int(split))
    return res

def imdb_preprocessing(x_train, y_train, x_test, y_test, shape_s=None):
    maxlen = 80
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
    print('x_train shape:', x_train.shape)
    print('x_test shape:', x_test.shape)
    return x_train, y_train, x_test, y_test

def mnist_preprocessing(x_train, y_train, x_test, y_test, shape_s=None):
    num_classes = 10
    if shape_s != None:
        shape = get_shape(shape_s)
        x_train = x_train.reshape(shape)
        x_test = x_test.reshape(shape)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print(x_train.shape, 'train shape')
    print(x_test.shape, 'test shape')
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return x_train, y_train, x_test, y_test
# x_train, y_train, x_test, y_test = mnist_preprocessing(sys.argv[1], sys.argv[2])
# np.savez(sys.argv[3], x_train = x_train, y_train = y_train, x_test = x_test, y_test = y_test)
def cifar10_preprocessing(x_train, y_train, x_test, y_test, shape_s=None):
    num_classes = 10
    if shape_s != None:
        shape = get_shape(shape_s)
        x_train = x_train.reshape(shape)
        x_test = x_test.reshape(shape)
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return x_train, y_train, x_test, y_test
# x_train, y_train, x_test, y_test = mnist_preprocessing(sys.argv[1], sys.argv[2])
# np.savez(sys.argv[3], x_train = x_train, y_train = y_train, x_test = x_test, y_test = y_test)

buildin_datasets = {"mnist" : mnist_preprocessing, 
                    "cifar10" : cifar10_preprocessing,
                    "imdb" : imdb_preprocessing}
def preprocess_buildin_dataset(x_train, y_train, 
                                  x_test, y_test, dataset_s, shape=None):
    handler = buildin_datasets.get(dataset_s)
    return handler(x_train, y_train, x_test, y_test, shape)


