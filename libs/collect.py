#!/usr/bin/env python3

from libs import sshlib
import sys
import logging

def find_values(config, value_list, KEY):
  for element in config:
    if type(config) is dict:
      if element == KEY:
        if type(config[element]) is str:
          logging.debug('DEBUG: found command: '+config[element])
          value_list.append(config[element])
        if type(config[element]) is list:
          for value in config[element]:
            logging.debug('DEBUG: found command: '+value)
            value_list.append(value) 
      else:
        find_values(config[element], value_list, KEY)
  return value_list 

def get_commands(config):
  comm = []
  return find_values(config, comm, "command") 

def run(config, host_list):
  commands = get_commands(config)  
  output = {}
  for host in host_list:
    output[host] = []
    for command in commands:
       output[host].append(sshlib.execute(host, command))


   
