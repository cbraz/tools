import subprocess
import logging

def cleanup_output(content):
  clean = []
  for line in content:
    clean.append(line.decode())#.rstrip('\n'))

  return ''.join(clean)

def execute(host, command):

  ssh = subprocess.Popen(["ssh", "%s" % host, command],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
  stdout = cleanup_output(ssh.stdout.readlines())
  stderr = cleanup_output(ssh.stderr.readlines())
  logging.debug("DEBUG: "+host+" stdout "+stdout)
  logging.error("ERROR: "+host+" stderr "+stdout)
  return {"stdout" : stdout,"stderr" : stderr}

