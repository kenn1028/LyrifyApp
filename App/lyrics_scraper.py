'''
Spotify Lyrics Player Project (June 2020)



Dependencies:
pip install beautifulsoup4
pip install requests
'''

import json
import requests
import webbrowser
from urllib.request import urlopen as uReq
from urllib.parse import urlencode
from bs4 import BeautifulSoup

class LyricScraper(object):
    song_name = None
    artist_name = None
    search_urls = ["https://colorcodedlyrics.com/"]

    def __init__(self, song_name, artist_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.song_name = song_name
        self.artist_name = artist_name

    def get_lyrics(self):
        search_query = f"{self.song_name} {self.artist_name}"
        params = urlencode({"s": f"{search_query}"})
        lookup_url = f"{self.search_urls[0]}?{params}"

        lookup_url = "https://search.azlyrics.com/search.php?q=girl's+talk+loona"
        #print(lookup_url)
        #webbrowser.open(lookup_url)

        html_content = requests.get(lookup_url).text
        # if html_content.status_code not in range (200,299):
        #     raise Exception("Couldn't fetch lookup_url")

        soup = BeautifulSoup(html_content, "lxml")

        data = soup.find_all("div", attrs={'class':'inner'}) #"div", attrs={'class':'site-content'}

        # a_class = data[0].find_all('a')
        # url_ = a_class[0].get('href')
        # print(url_)

        for n in range(len(data)):
            #print(data[n].find('a').text)
            print(data[n].find('a').get('href'))

        # for a in link.find_all("a"):
        #     print("Inner Text: {}".format(a.text))
        #     print("Title: {}".format(a.get("title")))
        #     print("href: {}".format(a.get("href")))

        # with open('html.txt', 'w', encoding = "utf-8") as w:
        #     w.write(soup.prettify())
        #print(soup.prettify())



lyrics = LyricScraper(song_name = "Girl's Talk", artist_name = "LOONA")

lyrics.get_lyrics()
