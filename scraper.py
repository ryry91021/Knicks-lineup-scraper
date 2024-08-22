#Web scraping application
import requests #HTTP requests
from bs4 import BeautifulSoup #Soup object fro, HTML response
import pandas as pd
from io import StringIO

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
def main():
    url="https://www.basketball-reference.com/teams/NYK/2024.html"
    response=requests.get(url)
    #print(response.text)

    soup=BeautifulSoup(response.content, "html.parser")
    #print(soup)

    statsPG=soup.find(id="per_game")
    #print(statsPG)

    statsDF = pd.read_html(StringIO(str(statsPG)))[0]  # Use StringIO to wrap the HTML string
    print(statsDF)

if __name__=="__main__":
    main()