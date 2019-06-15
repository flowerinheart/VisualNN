from keras import datasets


def load_imdb():
    return datasets.imdb.load_data(num_words=20000)
buildin_datasets = {"mnist" : datasets.mnist.load_data, 
                    "cifar10" : datasets.cifar10.load_data,
                    "imdb" : load_imdb}  

def load_buildin_dataset(dataset):
    load_handler = buildin_datasets.get(dataset)
    if load_handler == None:
        raise RuntimeError("no such build-in dataset : " + dataset)
    return load_handler()


def load_dir(path):
    f = np.load(path)
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test)