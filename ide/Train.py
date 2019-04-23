from __future__ import print_function
import sys
import numpy as np
from keras.models import model_from_json
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128
epochs = 20
def load(path):
    f = np.load(path)
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test)

def buildModel(modelPath):
    modelFile = open(modelPath, 'r')
    model = modelFile.read()
    modelFile.close()
    model = model_from_json(model)
    return model

def trainModel(model_path, data_path, result_path):
    #model = buildModel(sys.argv[1])
    model = buildModel(model_path)
    #(x_train, y_train), (x_test, y_test) = load(sys.argv[2])
    (x_train, y_train), (x_test, y_test) = load(data_path)
    print(x_train[0].shape)

    model.compile(loss='categorical_crossentropy',
                optimizer=RMSprop(),
                metrics=['accuracy'])

    history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=1,
                        validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    #model.save_weights(sys.argv[3])
    model.save_weights(result_path)


