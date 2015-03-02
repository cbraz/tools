import yaml
import sys

def load_yaml(filename):
  try:
    f = open(filename)
    _dict = yaml.safe_load(f)
    f.close
    return _dict
  except IOError:
   # print ("failed to open ", filename)
    print("failed to open", "'"+filename+"'" ,file=sys.stderr)
    raise
  except:
    print("invalid yaml in", "'"+filename+"'" ,file=sys.stderr)
    raise

def print_yaml(filename):
  _dict = load_yaml(filename)
  print(_dict)

