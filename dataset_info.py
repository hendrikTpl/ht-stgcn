import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

data_path = "./data/Kinetics/ht-hand-50/train_data.npy"
data = np.load(data_path)

print("shape:{} ndim:{} size(total number of elements): {}".format(data.shape,data.ndim, data.size))

data_copy = data[:1,:,:1,:,:].copy()
dt = data_copy.reshape(3,50)
#print(data_copy.shape)
#print(dt)



