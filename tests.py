from bs4 import BeautifulSoup
import requests
import re

class AnnoncesAirsoftOccasion:
    r = requests.get('https://www.airsoft-occasion.fr/')
    soup = BeautifulSoup (r.content, "html.parser")
    soup.prettify()
    annonces = soup.find('div', attrs={'class' :"lah-listing"})
    article = annonces.a.div.p
    zoneArticle = article.span.text
    nomArticle = article.text.split(zoneArticle)[0]
    prixArticle = article.find('span', attrs={'class' :"txt-price-premium"}).text

class AnnoncesAirsoftOccasionAll:
    r = requests.get('https://www.airsoft-occasion.fr/')
    soup = BeautifulSoup (r.content, "html.parser")
    soup.prettify()
    annonces = soup.find('div', attrs={'class' :"lah-listing"})
    articles = annonces.find_all('a', attrs={'class' : "background-ads-premium"})
    zoneArticles = [article.div.p.span.text for article in articles]
    nomArticles = [article.div.p.text.split(article.div.p.span.text)[0] for article in articles]
    prixArticle = [article.find('span', attrs={'class' :"txt-price-premium"}).text for article in articles]

""" print(AnnoncesAirsoftOccasion.nomArticle)
print(AnnoncesAirsoftOccasion.zoneArticle)
print(AnnoncesAirsoftOccasion.prixArticle) """
print(AnnoncesAirsoftOccasionAll.articles)