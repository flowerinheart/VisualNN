import caffe
from caffe import layers
from caffe import params

model_file="caffe_LeNet.prototxt"
output_model_path="."

net=caffe.Net(model_file,output_model_path,caffe.TRAIN)

