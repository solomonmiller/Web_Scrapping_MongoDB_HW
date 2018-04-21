
# coding: utf-8

# In[21]:


####STEP 1

# Dependencies
from bs4 import BeautifulSoup
import requests
import time
from splinter import Browser
import pandas as pd
from selenium import webdriver


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict = {}

# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

# Retrieve page with the requests module
    response = requests.get(url)
# Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')


# In[4]:


    print(soup.prettify())


# In[38]:


# results are returned as an iterable list
    results = soup.find('div', class_="rollover_description_inner")
    results2 = soup.find('div', class_="content_title")


# In[37]:


    news_p = results.text.strip()

    mars_dict['News_P'] = news_p

# In[41]:


    news_title = results2.text.strip()

    mars_dict['News_Title'] = news_title

# In[42]:


# In[6]:


    import time


# In[7]:



    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/'
    browser.visit(url)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')


# In[16]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results3 = soup.find('figure', class_="lede")





    link = results2.find('a')
    href = link['href']


    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17924_hires.jpg"

    mars_dict['featured_image_url'] = featured_image_url

# In[22]:


    url = "https://twitter.com/marswxreport?lang=en"

# Retrieve page with the requests module
    response = requests.get(url)
# Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')


# In[23]:


# results are returned as an iterable list
    tweet = soup.find('div', class_="js-tweet-text-container")


# In[24]:


    paragraph = tweet.find('p')


# In[28]:


    mars_weather = paragraph.text.strip()

    mars_dict['Mars_weather'] = mars_weather

    url = 'https://space-facts.com/mars/'


    tables = pd.read_html(url)
    tables = pd.DataFrame(tables)


# In[33]:


    html_table = tables.to_html()

# In[62]:
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image1 = soup.find('div', class_="downloads")
    title = soup.find('div', class_="content")
    title1 = title.find('h2').text
#link = results2.find('ul')
    tst = image1.find('li')
    tst2 = tst.find('a')
    href_1 = tst2['href']
    time.sleep(5)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image1 = soup.find('div', class_="downloads")
    title = soup.find('div', class_="content")
    title2 = title.find('h2').text
#link = results2.find('ul')
    tst = image1.find('li')
    tst2 = tst.find('a')
    href_2 = tst2['href']
    print(href_1)
    print(href_2)
    print(title1)
    print(title2)


# In[64]:

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'    
    browser.visit(url)

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image1 = soup.find('div', class_="downloads")
    title = soup.find('div', class_="content")
    title3 = title.find('h2').text
    #link = results2.find('ul')
    tst = image1.find('li')
    tst2 = tst.find('a')
    href_3 = tst2['href']
    print(href_3)
    print(title3)


# In[65]:

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image1 = soup.find('div', class_="downloads")
    title = soup.find('div', class_="content")
    title4 = title.find('h2').text
    #link = results2.find('ul')
    tst = image1.find('li')
    tst2 = tst.find('a')
    href_4 = tst2['href']
    print(href_4)
    print(title4)


# In[75]:


    aDict1 = {}
    aDict2 = {}
    aDict3 = {}
    aDict4 = {}

    aDict4['title'] = title4
    aDict4['img_url'] = href_4
    aDict1['title'] = title1
    aDict1['img_url'] = href_1
    aDict2['title'] = title2
    aDict2['img_url'] = href_2
    aDict3['title'] = title3
    aDict3['img_url'] = href_3

    hemisphere_image_urls = [aDict1,aDict2,aDict3,aDict4]

    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls
    print(mars_dict)
    return mars_dict
# In[77]:


#####END STEP 1

