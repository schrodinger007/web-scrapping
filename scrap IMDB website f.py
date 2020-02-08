import pandas as pd
import numpy as np
import re
import lxml

from bs4 import BeautifulSoup
from requests import get
%matplotlib inline
url= "https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2"
page = get(url)
soup = BeautifulSoup(page.content, 'lxml')
content = soup.find(id="main")
articleTitle = soup.find("h1", class_="header").text.replace("\n","")
movieFrame = content.find_all("div", class_="lister-item mode-advanced")
movieFirstLine = movieFrame[0].find("h3", class_="lister-item-header")
movieTitle = movieFirstLine.find("a").text
movieDate = re.sub(r"[()]","", movieFirstLine.find_all("span")[-1].text)
movieRunTime = movieFrame[0].find("span", class_="runtime").text[:-4]
movieGenre = movieFrame[0].find("span", class_="genre").text.rstrip().replace("\n","").split(",")
movieRating = movieFrame[0].find("strong").text
movieDesc = movieFrame[0].find_all("p", class_="text-muted")[-1].text.lstrip()
movieCast = movieFrame[0].find("p", class_="")
try:
    casts = movieCast.text.replace("\n","").split('|')
    casts = [x.strip() for x in casts]
    casts = [casts[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
    movieDirector = casts[0]
    movieStars = [x.strip() for x in casts[1].split(",")]
except:
    casts = movieCast.text.replace("\n","").strip()
    movieDirector = np.nan
    movieStars = [x.strip() for x in casts.split(",")]
movieNumbers = movieFrame[0].find_all("span", attrs={"name": "nv"})
if len(movieNumbers) == 2:
    movieVotes = movieNumbers[0].text
    movieGross = movieNumbers[1].text
else:
    movieVotes = movieNumbers[0].text
    movieGross = np.nan
