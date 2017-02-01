from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

net = buildNetwork(2, 3, 1)

ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0))
ds.addSample((0, 1), (1))
ds.addSample((1, 0), (1))
ds.addSample((1, 1), (0))

trainer = BackpropTrainer(net, ds)
thresh = .001
output = 1
while output > thresh:
  output = trainer.train()
  print output
print net.activate((0, 0))
print net.activate((0, 1))
print net.activate((1, 0))
print net.activate((1, 1))
