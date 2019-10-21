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
def getData(content)->list:
    tweets = content.findAll('div',attrs = {"class" : "tweet"})
    data = list()
    for tweet in tweets:
        tweet_data = dict()
        tweet_content = tweet.find('div',attrs = {"class" : "content"})
        user_name = tweet_content.find('a',attrs = {"class" : "account-group"}).find("strong",attrs={"class" : "fullname"}).text
        tweet_data["user"] = user_name
        date_published = tweet_content.find('a',attrs={"class" : "tweet-timestamp"}).attrs['title']
        tweet_data["date"] = date_published
        tweet_text = tweet_content.find('p', attrs={"class" : "tweet-text"}).text
        tweet_data['text'] = tweet_text
        data.append(tweet_data)
    return data
def main(args: list)->int:
    url = args[1]
    content = getContent(url)
    data = getData(content)
    
    print(data)
    return 0
if __name__ == "__main__":
    main(sys.argv)