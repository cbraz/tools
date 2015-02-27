import subprocess
import sys


def cleanup_output(content):
  clean = []
  for line in content:
    clean.append(line.decode().rstrip('\n'))

  return clean 

def execute(host, command):

  ssh = subprocess.Popen(["ssh", "%s" % host, command],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
  stdout = ssh.stdout.readlines()
  stderr = ssh.stderr.readlines()
  return {"stdout" : cleanup_output(stdout),"stderr" : cleanup_output(stderr)}

