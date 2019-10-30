# Dependencies
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import time 

def get_news():
    browser= webdriver.Chrome("chromedriver")
    browser.get("https://mars.nasa.gov/news/")
    time.sleep(2)
    html = browser.page_source
    soup = bs(html, "html.parser")

    news_title = soup.find("div", class_="content_title").find("a").text 
    news_p = soup.find("div", class_="article_teaser_body").text
    browser.close()
    return [news_title, news_p]


def get_image():
    browser= webdriver.Chrome("chromedriver")
    browser.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    html = browser.page_source
    soup = bs(html, "html.parser")
    featured_image = soup.find("a",attrs={"data-fancybox-href": True})["data-fancybox-href"]
   
    featured_image_url = soup.find_all("img")[2]["src"]
    browser.close()
    image_url = 'https://www.jpl.nasa.gov' + featured_image
    
    return [featured_image_url, image_url]


def get_weather():
    browser= webdriver.Chrome("chromedriver")
    browser.get("https://twitter.com/marswxreport?lang=en")
    time.sleep(2)
    html = browser.page_source
    soup = bs(html, "html.parser")

    mars_weather = soup.find("div", class_="js-tweet-text-container").text
    browser.close()
    return mars_weather


def get_facts():
    facts_url= 'https://space-facts.com/mars/'

    facts_tables = pd.read_html(facts_url)
    facts_tables[0]
    facts_tables[0].to_html()
    tables = facts_tables[0].to_html()
    return tables


def get_hemispheres():
    browser= webdriver.Chrome("chromedriver")
    browser.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    time.sleep(2)
    html = browser.page_source
    soup = bs(html, "html.parser")
    root = "https://astrogeology.usgs.gov"

    image_divs = soup.find_all("div", class_="description")

    hemisphere_image_url = []

    for image_div in image_divs:
        href = image_div.a["href"]
        image_page_url = root + href
        title=image_div.a.text
        browser.get(image_page_url)
        html = browser.page_source
        soup = bs(html, "html.parser")
        image_url = soup.find("img", class_="wide-image")["src"]
        image_url = root + image_url
        d = {"title": title, "img_url": image_url}
        hemisphere_image_url.append(d)
    browser.close()
    return hemisphere_image_url


def get_all():
    hemispheres = get_hemispheres()
    news = get_news()
    images = get_image()
    weather = get_weather()
    facts = get_facts()

    mars_data = {
        "hemispheres":hemispheres,
        "news": news,
        "images": images,
        "weather": weather,
        "facts": facts
    }
    return mars_data
#print(get_all())
