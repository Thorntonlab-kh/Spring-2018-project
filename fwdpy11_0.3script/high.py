import subprocess
import tensorflow as tf
import os
from keras import backend as K
os.environ["CUDA_VISIBLE_DEVICES"]="3"

list = [ 1 ]


with tf.device('/device:GPU:3'):
    for i in range(1,257):
            filename1= "/media/khoih/rawdata/hi/final_replicate"+str(i)+".stat.txt"
            filename2= "/media/khoih/rawdata/hi/highalpha/replicate"+str(i)+".result.txt"
            subprocess.call(["python3", "/media/khoih/diploSHIC/diploSHIC.py", "predict", "/media/khoih/100theta_trainingmodel_2500_25000_alpha/modelfile.txt.json", "/media/khoih/100theta_trainingmodel_2500_25000_alpha/modelfile.txt.weights.hdf5", filename1, filename2])


with tf.device('/device:GPU:3'):
    for i in range(1,257):
            filename1= "/media/khoih/rawdata/hi/final_replicate"+str(i)+".stat.txt"
            filename2= "/media/khoih/rawdata/hi/lowalpha/replicate"+str(i)+".result.txt"
            subprocess.call(["python3", "/media/khoih/diploSHIC/diploSHIC.py", "predict", "/media/khoih/100theta_trainingmodel_25_250_alpha/modelfile.txt.json", "/media/khoih/100theta_trainingmodel_25_250_alpha/modelfile.txt.weights.hdf5", filename1, filename2])
