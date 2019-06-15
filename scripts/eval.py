from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.models import model_from_json
import os
import sys


def getFile(fpath):
    if os.path.exists(fpath):
        #file find, just return fpath
        return fpath
    else:
        #a hdfs fpath
        raise NameError
        pass

def buildModel(modelPath, weightPath):
    modelFile = open(modelPath, 'r')
    model = modelFile.read()
    modelFile.close()
    model = model_from_json(model)
    print (model.summary())
    model.load_weights(weightPath)
    return model

def preprocessing(instancePath):
    image = load_img(instancePath, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    return image

if __name__ == "__main__":
    print(sys.argv)
    modelPath = getFile(sys.argv[1])
    weightPath = getFile(sys.argv[2])
    testInstance = getFile(sys.argv[3])
    testInstance = preprocessing(testInstance)
    model = buildModel(modelPath, weightPath)
    yhat = model.predict(testInstance)
    label = decode_predictions(yhat)
    label = label[0][0]
    print('%s (%.2f%%)' % (label[1], label[2]*100))
