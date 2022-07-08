from inspect import Parameter
import requests
import json
import yaml
from urllib.parse import urlunsplit, urlencode

# Perform a request to bwg api, filter result and return data usage information
# Input [config]:<Dict> User configuration read from config.yaml 
# Output: <Dict> Information selected by 'lookup_params' in config.yaml
def bwg_lookup(config):
    # Call bandwagon api
    url = build_url(config)
    response = requests.get(url)
    data = json.loads(response.content)  
    result = {key:value for key,value in data.items() if key in config['bwg']['lookup_params']}
    return result

# Compose url form user configuration data
# INPUT [config]: <Dict> User configuration read from config.yaml
# OUTPT: <String> url requesting bwg api
def build_url(config):
    # generate query string from user configuration, select those only needed by bwg api
    query = urlencode({key:value for key, value in config['user'].items() if key in config['bwg']["parameters"]}) 
    url = urlunsplit((config['bwg']['scheme'], config['bwg']['domain'],config['bwg']['path'],query,""))
    return url
