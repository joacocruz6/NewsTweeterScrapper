from wordcloud import WordCloud
from stop_words import get_stop_words
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re
STOPWORDS = get_stop_words("es")
# Appending some useless and non informatic words to the stopwords
STOPWORDS.append("twitter")
STOPWORDS.append("http")
STOPWORDS.append("https")
STOPWORDS.append("bit")
STOPWORDS.append("ly")
STOPWORDS.append("com")
STOPWORDS.append("cl")
STOPWORDS.append("www")
STOPWORDS.append("tinyurl")
STOPWORDS.append("Señal")
STOPWORDS.append("pic")
STOPWORDS.append("AHORA")
STOPWORDS.append("meganoticias")
STOPWORDS.append("Sigue")
STOPWORDS.append("t13")
STOPWORDS.append("lacuarta")
STOPWORDS.append("YouTube")
STOPWORDS.append("mega")
STOPWORDS.append("vivo")
STOPWORDS.append("AHORA24H")
STOPWORDS.append("cronica")
STOPWORDS.append("noticia")
STOPWORDS.append("ÚLTIMO")
STOPWORDS.append("24Play")
PATH = "../bdUploader/exports.csv"
LINK_REGEX = "http[s]{0,1}://\w+\.[ly|com|cl]/\w*"
def main(args: list)->int:
    df = pd.read_csv(PATH,encoding="utf-8")
    
    text = df["tweet_text"]
    image_text = " ".join(my_text for my_text in text)
    wordcloud = WordCloud(stopwords=STOPWORDS).generate(image_text)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.savefig("wordcloud.png")
    return 0


if __name__=="__main__":
    main(sys.argv)
