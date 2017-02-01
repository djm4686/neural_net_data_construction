
def read_file_bytes(filename):
  with open(filename, "rb") as f:
    try:
      byte = f.read(1)
      i = 0
      while byte != "":
        for j in xrange(8):
          yield i, (ord(byte) >> j) & 1
          i += 1
        byte = f.read(1)
    except Exception as e:
      print e

if __name__ == "__main__":
  for i, b in read_file_bytes("test_file.bin"):
    print i, b
