#!/usr/bin/env python3

from sshlib import execute
import sys

#print (sys.argv)

result = execute(sys.argv[1],"df -h")
print ("stdout", result["stdout"])
print ("stderr", result["stderr"])
