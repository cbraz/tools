import subprocess
import logging

def cleanup_output(content):
  clean = []
  for line in content:
    line=line.decode().rstrip('\n')
    logging.debug("\t"+line)
    clean.append(line)
  return clean
  

def execute(command):

  cmd_list = command.split()
  try:
    result = subprocess.Popen(cmd_list,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    logging.debug("DEBUG: stdout:")
    stdout = cleanup_output(result.stdout.readlines())
    logging.error("ERROR: stderr:")
    stderr = cleanup_output(result.stderr.readlines())
    return {"stdout" : stdout,"stderr" : stderr}

  # if an invalid (non existent) command is executed, it will generate an exception 
  except Exception as e:
    logging.error("ERROR: failed to execute command:\n"+command)
    logging.error(type(e))
    logging.error(e)
    return {"stdout" : [], "stderr" : [e]}
