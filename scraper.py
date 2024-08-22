#Web scraping application
import requests #HTTP requests
from bs4 import BeautifulSoup #Soup object for, HTML response
import pandas as pd
from io import StringIO
import matplotlib as mpl

def main():
    url="https://www.basketball-reference.com/teams/NYK/2024.html"
    response=requests.get(url)
    #print(response.text)

    soup=BeautifulSoup(response.content, "html.parser")
    #print(soup)

    statsPG=soup.find(id="per_game")
    #print(statsPG)

    statsDF = pd.read_html(StringIO(str(statsPG)))[0]  # Use StringIO to wrap the HTML string
    

    #drop rank
    statsDF=statsDF.drop('Rk', axis=1)
    print(statsDF)

if __name__=="__main__":
    main()