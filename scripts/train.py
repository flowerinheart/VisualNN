"""Usage: 
train.py <model> <dataset> [options]

Options:
-h --help    show this
--output=FILE    Output file [default: ~/.visualnn/temp.h5].
--loss=LOSS      loss type [default: categorical_crossentropy]
--shape=SHAPE    preprocessing's shape.

"""
from keras import backend as K
from docopt import docopt
from load_data import load_buildin_dataset
from preprocessing import preprocess_buildin_dataset
from docopt import docopt
from keras.optimizers import RMSprop
from keras.models import model_from_json
#K.tensorflow_backend._get_available_gpus()


batch_size = 128
epochs = 20
batch_size = 32
epochs = 15
def buildModel(modelPath):
	modelFile = open(modelPath, 'r')
	model = modelFile.read()
	modelFile.close()
	model = model_from_json(model)
	return model



if __name__ == "__main__":
	arguments = docopt(__doc__)
	model_path = arguments["<model>"]
	dataset = arguments["<dataset>"]
	output_path = arguments["--output"]
	shape = arguments["--shape"]
	loss = arguments["--loss"]
	print(loss)

	model = buildModel(model_path)
	(x_train, y_train), (x_test, y_test) = load_buildin_dataset(dataset)
	x_train, y_train, x_test, y_test = preprocess_buildin_dataset(x_train, 
									   y_train, x_test, y_test, dataset, shape)

	model.compile(loss=loss,
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
	model.save_weights(sys.argv[3])
