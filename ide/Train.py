from __future__ import print_function
import numpy as np
from keras.models import model_from_json
from keras.utils import np_utils
from keras.optimizers import RMSprop

batch_size = 128
epochs = 5
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
    model = buildModel(model_path)
    (x_train, y_train), (x_test, y_test) = load(data_path)
    print(x_train[0].shape)
    x_train = np.reshape(x_train,(60000, 784))
    x_test = np.reshape(x_test, (10000, 784))
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
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
    model.save(result_path)


