# Web scraping application
import requests  # HTTP requests
from bs4 import BeautifulSoup  # Soup object for HTML response
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import sys

def main():
    url = "https://www.basketball-reference.com/teams/NYK/2024.html"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    statsPG = soup.find(id="per_game")
    
    if statsPG is None:
        print("Failed to find the stats table in the page.")
        return

    statsDF = pd.read_html(StringIO(str(statsPG)))[0]  # Use StringIO to wrap the HTML string

    # Drop the 'Rk' column if it exists
    if 'Rk' in statsDF.columns:
        statsDF = statsDF.drop('Rk', axis=1)


    # Handle stat selection
    try:
        stat = sys.argv[1].upper()
    except IndexError:
        stat=None
    
    while stat is None or stat not in statsDF.columns or stat == "Player":
        if stat is None or stat not in statsDF.columns or stat == "Player":
            print("Available stats:", list(statsDF.columns[1:]))  # Skip 'Player' column
            stat = input("Choose a stat from the list: ").strip().upper()
        
    try:
        if stat in statsDF.columns and stat != "Player":
            chart(stat, statsDF)
        else:
            print(f"Invalid stat '{stat}'. Please choose from: {', '.join(statsDF.columns[1:])}")
    except Exception as e:
        print(f"An error occurred: {e}")

def chart(stat, df):
    """Creates a bar chart based on the provided stat"""
    if stat in df.columns and stat != "Player":
        plt.figure(figsize=(10, 6))
        plt.bar(df['Player'], df[stat], color='skyblue')
        plt.xlabel("Player")
        plt.ylabel(stat.title())
        plt.title(f"Player's {stat} per game")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("There was a failure creating the bar chart")

# Run the script
if __name__ == "__main__":
    main()
