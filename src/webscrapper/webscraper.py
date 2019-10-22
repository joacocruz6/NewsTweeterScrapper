from bs4 import BeautifulSoup
import requests
import sys
import json
import time
ROUTE = '../jsonData/'


def getContent(url: str):
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
    print(f"Now scrapping {url}")
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    return content


def getData(content) -> list:
    """Get the important data of the tweeter scrapper for the json document

    Arguments:
        content {[type]} -- The content of the tweeter account

    Returns:
        list -- list of dictionaries with three keys -name,date,text- on which the data will be dump on
    """
    tweets = content.findAll('div', attrs={"class": "tweet"})
    data = list()
    for tweet in tweets[1:]:
        tweet_data = dict()
        tweet_content = tweet.find('div', attrs={"class": "content"})
        tweet_data["id"] = tweet.attrs['data-tweet-id']
        user_name = tweet_content.find('a', attrs={
                                       "class": "account-group"}).find("strong", attrs={"class": "fullname"}).text
        tweet_data["user"] = user_name
        date_published = tweet_content.find(
            'a', attrs={"class": "tweet-timestamp"}).attrs['title']
        tweet_data["date"] = date_published
        tweet_text = tweet_content.find(
            'p', attrs={"class": "tweet-text"}).text
        tweet_data['text'] = tweet_text
        data.append(tweet_data)
    return data


def dump_json(data: list, jfile: str) -> None:
    """Dump the data to a json file to be uploaded on the DB afterwards

    Arguments:
        data {list} -- the data that will be dumped
        jfile {str} -- The route to the file that will be dumped the data on
    Returns:
        None -- Creates and dump the data on the json file
    """
    with open(jfile, 'w') as output:
        json.dump(data, output)
    return


def main(args: list) -> int:
    url = args[1]
    content = getContent(url)
    data = getData(content)
    json_file = ROUTE + args[2]
    dump_json(data, json_file)
    time.sleep(8) # 8 seconds to wait for next execution
    return 0


if __name__ == "__main__":
    main(sys.argv)  # argv must contain in first position the webpage and in the second position the json file name with it's extension
