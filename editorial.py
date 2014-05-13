# -*- coding: utf-8 -*-
from datetime import datetime

from bs4 import BeautifulSoup
import requests
from textblob import TextBlob


# Scrape newspaper editorial section of the day and guess the main subject
def tema_del_dia():
    today = datetime.today().strftime("%d-%m-%Y")
    url = "http://www.larepublica.pe/politica/editorial-" + today
    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    entry = soup.find("div", "glr-post-entry")

    editorial = ""
    for i in entry.find_all("p"):
        for item in i.contents:
            editorial += str(item.encode("utf-8"))

    editorial = strip_tags(editorial)
    return guess_topic(editorial.decode("utf-8"))


def guess_topic(text):
    our_topics = [
        u"educación",
        u"salud",
        u"corrupción",
        u"seguridad ciudadana",
        u"minería ilegal",
        u"concentración de medios",
        ]
    text = TextBlob(text)

    topic_score = [[text.word_counts[topic], topic] for topic in our_topics]

    most_frequent_word = sorted(topic_score)[-1:][0]
    if most_frequent_word[0] > 0:
        return most_frequent_word[1]
    else:
        return None


def strip_tags(string):
    string = string.replace("<br/>", "")
    string = string.replace("<p>", "")
    string = string.replace("</p>", "")
    return string


def main():
    print tema_del_dia()


if __name__ == "__main__":
    main()
