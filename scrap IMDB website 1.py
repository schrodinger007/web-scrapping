{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re\n",
    "import lxml\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "from requests import get\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "url= \"https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "page = get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(page.content, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "content = soup.find(id=\"main\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "articleTitle = soup.find(\"h1\", class_=\"header\").text.replace(\"\\n\",\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieFrame = content.find_all(\"div\", class_=\"lister-item mode-advanced\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieFirstLine = movieFrame[0].find(\"h3\", class_=\"lister-item-header\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieTitle = movieFirstLine.find(\"a\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieDate = re.sub(r\"[()]\",\"\", movieFirstLine.find_all(\"span\")[-1].text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieRunTime = movieFrame[0].find(\"span\", class_=\"runtime\").text[:-4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieGenre = movieFrame[0].find(\"span\", class_=\"genre\").text.rstrip().replace(\"\\n\",\"\").split(\",\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieRating = movieFrame[0].find(\"strong\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieDesc = movieFrame[0].find_all(\"p\", class_=\"text-muted\")[-1].text.lstrip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieCast = movieFrame[0].find(\"p\", class_=\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    casts = movieCast.text.replace(\"\\n\",\"\").split('|')\n",
    "    casts = [x.strip() for x in casts]\n",
    "    casts = [casts[i].replace(j, \"\") for i,j in enumerate([\"Director:\", \"Stars:\"])]\n",
    "    movieDirector = casts[0]\n",
    "    movieStars = [x.strip() for x in casts[1].split(\",\")]\n",
    "except:\n",
    "    casts = movieCast.text.replace(\"\\n\",\"\").strip()\n",
    "    movieDirector = np.nan\n",
    "    movieStars = [x.strip() for x in casts.split(\",\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "movieNumbers = movieFrame[0].find_all(\"span\", attrs={\"name\": \"nv\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "if len(movieNumbers) == 2:\n",
    "    movieVotes = movieNumbers[0].text\n",
    "    movieGross = movieNumbers[1].text\n",
    "else:\n",
    "    movieVotes = movieNumbers[0].text\n",
    "    movieGross = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
