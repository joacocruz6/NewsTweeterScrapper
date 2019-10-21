from bs4 import BeautifulSoup
import requests
import sys
import json

def getContent(url:str):
    """
    Gets the content for a given url in the web
    
    Arguments: 
        url {str} -- [
            The url of the webpage to scrap
        ]
    
    Returns:
        [type] -- [
            The content as a BeautifulSoup object
        ]
    """
    response = requests.get(url,timeout=5)
    content = BeautifulSoup(response.content,"html.parser")
    return content

def main(args):
    url = args[1]
    content = getContent(url)
    print(content)
    return 0


if __name__ == "__main__":
    main(sys.argv)