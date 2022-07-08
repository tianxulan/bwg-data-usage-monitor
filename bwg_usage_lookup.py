import requests
import json
import config
def main():
    response = requests.get('')
    data = json.loads(response.content)  
    print(data)


if __name__ == "__main__":
    main()