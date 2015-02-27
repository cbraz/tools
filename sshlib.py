import subprocess
import sys


def cleanup_output(result):
  clean = []
  for line in result:
    clean.append(line.decode().rstrip('\n'))

  return clean 

def execute(host, command):
#HOST="192.168.1.127"
# Ports are handled in ~/.ssh/config since we use OpenSSH
#COMMAND="df -h"

  ssh = subprocess.Popen(["ssh", "%s" % host, command],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
  result = ssh.stdout.readlines()
  error = ssh.stderr.readlines()
  #print("ERROR:",error)
  return {"stdout" : cleanup_output(result),"stderr" : cleanup_output(error)}
#    result = cleanup_output(result)
#    for line in result:
#      print(line)

