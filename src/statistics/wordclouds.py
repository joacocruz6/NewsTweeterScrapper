from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re
PATH = "../bdUploader/exports.csv"
LINK_REGEX = "http[s]{0,1}://\w+\.[ly|com|cl]/\w*"
def main(args: list)->int:
    df = pd.read_csv(PATH,encoding="utf-8")
    print(df[2])
    return 0


if __name__=="__main__":
    main(sys.argv)