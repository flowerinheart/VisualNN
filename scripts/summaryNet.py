from keras.models import model_from_json
import os
import sys



if __name__ == "__main__":
    #Open the json file.
    modelPath = sys.argv[1]
    model = open(modelPath, 'r')
    #Read and close the json file.
    loadedModel = model.read()
    model.close()
    #Load model from json file content.
    loadedModel = model_from_json(loadedModel)
    #Print the summary 
    print (loadedModel.summary())

