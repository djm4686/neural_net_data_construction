from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from byte_reader import read_file_bytes
net = buildNetwork(1, 10, 1)

ds = SupervisedDataSet(1, 1)

for i, bit in read_file_bytes("test_file.bin"):
  ds.addSample((i), (bit))

trainer = BackpropTrainer(net, ds)
thresh = .01
output = 1
while output > thresh:
  output = trainer.train()
  print output
total_hits = 0
total_misses = 0
total = 0
for i, bit in read_file_bytes("test_file_bin"):
  if net.activate((i)) >= .5 and bit == 1:
    total_hits += 1
  else:
    total_misses += 1
  total = i
print total_hits, total_misses
print total_hits + total_misses, i
