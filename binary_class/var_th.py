############################################## README #################################################

# This calculates threshold for an image depending upon its spiking activity.

########################################################################################################


import numpy as np
from binary_class.neuron import neuron
import random
from matplotlib import pyplot as plt
from binary_class.recep_field import rf
from binary_class.spike_train import encode
from binary_class.rl import rl
from binary_class.rl import update
from binary_class.reconstruct import reconst_weights
from binary_class.parameters import param as par
import os
from PIL import Image


def threshold(train):

	tu = np.shape(train[0])[0]
	thresh = 0
	for i in range(tu):
		simul_active = sum(train[:,i])
		if simul_active>thresh:
			thresh = simul_active

	return (thresh/3)*par.scale


if __name__ == '__main__':

	# img = cv2.imread("mnist1/" + str(1) + ".png", 0)
	img = np.array(Image.open("mnist1/" + str(1) + ".png"))
	print(img)
	# pot = rf(img)
	# train = np.array(encode(pot))
	# print threshold(train)