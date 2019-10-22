from wordcloud import WordCloud
from stop_words import get_stop_words
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re
STOPWORDS = get_stop_words("es")
PATH = "../bdUploader/exports.csv"
LINK_REGEX = "http[s]{0,1}://\w+\.[ly|com|cl]/\w*"
def main(args: list)->int:
    df = pd.read_csv(PATH,encoding="utf-8")
    text = df["tweet_text"]
    one_text = text[0]
    wordcloud = WordCloud(stopwords=STOPWORDS).generate(one_text)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.savefig("wordcloud.png")
    return 0


if __name__=="__main__":
    main(sys.argv)