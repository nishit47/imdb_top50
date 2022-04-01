from bs4 import BeautifulSoup
import requests
from csv import writer 

import pandas as pd
from pandas_profiling import ProfileReport

url="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
page=requests.get(url)

soup= BeautifulSoup(page.content, 'html.parser')
lists=soup.find_all('div', class_="lister-item")

with open('imdb.csv', 'w', encoding='utf8', newline='') as f:
    thewriter=writer(f)
    heading=["Rank", "Name", "Released Year", "Genre", "IMdB Rating"]
    thewriter.writerow(heading)
    
    for list in lists:
        title=list.h3.a.text
        year=list.h3.find('span', class_="lister-item-year").text.replace("(", "").replace(")","")
        genre=list.p.find('span', class_="genre").text.replace("\n", "")
        ratingbar=list.find('div', class_="ratings-bar")
        ratingimdb=ratingbar.find('div', class_="ratings-imdb-rating")
        rating=ratingimdb.strong.text
        rank=list.h3.find('span', class_="lister-item-index").text
        data=[rank, title, year, genre, rating]
        thewriter.writerow(data)

df=pd.read_csv("imdb.csv")

profile=ProfileReport(df)
profile.to_file(output_file="Report.html")