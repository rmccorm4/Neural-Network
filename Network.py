import random
import numpy as np

class Network:
	def __init__(self, layer_sizes):
		# List of the sizes of each layer in order
		self.layer_sizes = layer_sizes
		self.num_layers = len(layer_sizes)
		# Figure out why thees are good initializations
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:], sizes[1:])]
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]

	def feed_forward(self, arg):
		for bias, weight in zip(self.biases, self.weights):
			arg = relu(np.dot(weight, arg)+bias)
		return layer

	# Stochastic Gradient Descent
	def sgd(self, training_sample, test_sampe=None):
		pass


# Rectified Linear Unit function for non-linearity
# Piecewise linear == non-linear
def relu(result):
	if result > 0:
		return result
	return 0
