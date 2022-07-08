from inspect import Parameter
import requests
import json
import yaml
from urllib.parse import urlunsplit, urlencode
def main():
    # Read user config
    with open("local_config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    url = build_url(config)
    #Call bandwagon api
    # response = requests.get('')
    # data = json.loads(response.content)  
    # print(data)

# Compose url form user configuration data
# INPUT: <Dict> User configuration read from config.yaml
# OUTPT: <String> url requesting bwg api
def build_url(config):
    # generate query string from user configuration, select those only needed by bwg api
    query = urlencode({key:value for key, value in config['user'].items() if key in config['bwg']["parameters"]}) 
    url = urlunsplit((config['bwg']['scheme'], config['bwg']['domain'],config['bwg']['path'],query,""))
    return url


if __name__ == "__main__":
    main()