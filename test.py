#!/usr/bin/env python3

from sshlib import execute
from yamllib import load_yaml,print_yaml
import sys

#print (sys.argv)
def test_libssh():
  result = execute(sys.argv[1],"df -h")
  print ("stdout", result["stdout"])
  print ("stderr", result["stderr"])

def test_yamllib():
  try:
    print_yaml(sys.argv[1])
    ldict = load_yaml(sys.argv[1])
    for key,value in ldict.items():
      print(key, "=>", value)
  except:
    print ("error")
test_yamllib()  

