from bs4 import BeautifulSoup
import requests
import sys
import json
def main(args):
    url = args[1]
    response = requests.get(url,timeout=5)
    content = BeautifulSoup(response.content,"html.parser")
    print(content)
    return 0

if __name__ == "__main__":
    main(sys.argv)