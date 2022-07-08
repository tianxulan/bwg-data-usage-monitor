from inspect import Parameter
import requests
import json
import yaml
from urllib.parse import urlunsplit, urlencode
def bwg_lookup():
    # Read user config
    with open("local_config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
    # Call bandwagon api
    url = build_url(config)
    response = requests.get(url)
    data = json.loads(response.content)  
    result = {key:value for key,value in data.items() if key in config['bwg']['lookup_params']}
    return result

# Compose url form user configuration data
# INPUT: <Dict> User configuration read from config.yaml
# OUTPT: <String> url requesting bwg api
def build_url(config):
    # generate query string from user configuration, select those only needed by bwg api
    query = urlencode({key:value for key, value in config['user'].items() if key in config['bwg']["parameters"]}) 
    url = urlunsplit((config['bwg']['scheme'], config['bwg']['domain'],config['bwg']['path'],query,""))
    return url
