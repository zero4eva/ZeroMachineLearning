from perceptron import Perceptron

def f(x):
	return 1 if x > 0 else 0

def get_training_dataset():
	input_vecs = [[1,1], [0,0], [1,0], [0,1]]
	labels = [1, 0, 1, 1]
	return input_vecs, labels

def train_and_perceptron():
	p = Perceptron(2, f)
	input_vecs, labels = get_training_dataset()
	p.train(input_vecs, labels, 10, 0.1)
	return p

if __name__ == '__main__':
	and_perceptron = train_and_perceptron()
	print and_perceptron
	print '1 or 1 = %d' % and_perceptron.predict([1, 1])
	print '0 or 0 = %d' % and_perceptron.predict([0, 0])
	print '1 or 0 = %d' % and_perceptron.predict([1, 0])
	print '0 or 1 = %d' % and_perceptron.predict([0, 1])