import requests
import json
def main():
    response = requests.get('')
    data = json.loads(response.content)  
    print(data)


if __name__ == "__main__":
    main()