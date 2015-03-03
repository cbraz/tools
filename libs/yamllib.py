import yaml
import sys
#import logging
import logging

def load_yaml(filename):
  try:
    logging.debug('DEBUG: opening '+filename)
    f = open(filename)
    logging.debug('DEBUG: loading yaml from '+filename)
    _dict = yaml.safe_load(f)
    f.close
    logging.debug('DEBUG: returning dict loaded from '+filename)
    return _dict
  except IOError:
    logging.error('ERROR: Failed to open file '+filename)
    raise
  except yaml.YAMLError:
    logging.error('ERROR: Failed to parse yaml in '+filename)
    raise
  
def print_yaml(filename):
  _dict = load_yaml(filename)
  print(_dict)

