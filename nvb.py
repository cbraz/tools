#!/usr/bin/env python3

from libs import runlocal
from time import sleep
import subprocess
import os


sleep_stop=3600
sleep_kill=5
while True:

  os.environ['DISPLAY'] = ":1"
  print("Starting chromium")
  subprocess.Popen(["chromium", "https://gateway.playneverwinter.com"],env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


  print("waiting for", sleep_stop, "seconds before restart")
  sleep(sleep_stop)
  result = runlocal.execute("ps -fe")
  for line in result["stdout"]:
    if "chromium" in line:
      my_list = line.split()
      print("found chromium process:", my_list[1], ", killing it")
      runlocal.execute("kill "+my_list[1])

  sleep(sleep_kill)
  result = runlocal.execute("ps -fe")
  for line in result["stdout"]:
    if "chromium" in line:
      my_list = line.split()
      print("found chromium process:", my_list[1], ", killing it")
      runlocal.execute("kill -9 "+my_list[1])


