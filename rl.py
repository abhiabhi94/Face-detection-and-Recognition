from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
import numpy as np

# n = FeedForwardNetwork()
# inLayer = LinearLayer(2)
# hiddenLayer = SigmoidLayer(3)
# outLayer = LinearLayer(1)
# n.addInputModule(inLayer)
# n.addModule(hiddenLayer)
# n.addOutputModule(outLayer)

# in_to_hidden = FullConnection(inLayer, hiddenLayer)
# hidden_to_out = FullConnection(hiddenLayer, outLayer)
# n.addConnection(in_to_hidden)
# n.addConnection(hidden_to_out)
# n.sortModules()
# print n.activate([1, 2])
# print n

faceDB = np.array(np.load("friendlyFaces.npy"))
labels = np.array(np.load("friendlyFacesClassifier.npy"))
print faceDB.shape, labels.shape
from pybrain.datasets import SupervisedDataSet
ds = SupervisedDataSet((80, 65, 65), 80)
ds.addSample(faceDB,labels)