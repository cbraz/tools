#!/usr/bin/env python3

from libs import sshlib, yamllib, collect, runlocal
import sys


#print (sys.argv)
def test_libssh():
  result = sshlib.execute(sys.argv[1],"df -h")
  print ("stdout", result["stdout"])
  print ("stderr", result["stderr"])

def test_yamllib():
  try:
    yamllib.print_yaml(sys.argv[1])
    ldict = yamllib.load_yaml(sys.argv[1])
    for key,value in ldict.items():
      print(key, "=>", value)
  except:
    exit(1)

def test_collect():
  try:
    config = yamllib.load_yaml(sys.argv[1])
  except:
    exit(1)

  output = collect.run(config, ["192.168.1.150", "192.168.1.127"])

def test_runlocal():
  result = runlocal.execute("ls -l /")
  print ("\tstdout:\n")
  for line in result["stdout"]:
    print(line)
  print ("\tstderr:\n")
  for line in result["stderr"]:
    print(line)
 


if __name__ == '__main__':
  #test_collect()  
  test_runlocal()
