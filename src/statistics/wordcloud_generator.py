from wordcloud import WordCloud
from my_stopwords import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re

PATH = "../bdUploader/exports_"
LINK_REGEX = "http[s]{0,1}://\w+\.[ly|com|cl]/\w*"
def main(args: list)->int:
    wordcloud_type = args[1]
    path = PATH + wordcloud_type + ".csv"
    df = pd.read_csv(path,encoding="utf-8")
    text = df["tweet_text"]
    image_text = " ".join(my_text for my_text in text)
    wordcloud = WordCloud(stopwords=STOPWORDS).generate(image_text)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f"wordcloud_{wordcloud_type}.png")
    return 0


if __name__=="__main__":
    main(sys.argv)
