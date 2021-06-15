from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # browser = init_browser()

# Visit https://mars.nasa.gov/news/
    url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = bs(html,'html.parser')
    title = soup.find('div', class_= "content_title").text
    paragraph = soup.find('div', class_ = "article_teaser_body").text

    # browser.quit()
# Scrape Mars image from: spaceimages-mars.com
    # browser = init_browser()
    img = "https://spaceimages-mars.com/"
    browser.visit(img)
    browser.links.find_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = bs(html,'html.parser')
    img_search = soup.find('img', class_='headerimage fade-in').get('src')


    time.sleep(3)
    featured_image_url = f'https://www.spaceimages-mars.com/{img_search}'
    # browser.quit()

    # Scrape Mars Facts table from: galaxyfacts-mars.com
    # browser = init_browser()
    table_url = "https://galaxyfacts-mars.com/"
    browser.visit(table_url)
    table = pd.read_html(table_url)
    table_df = table[1]
    table_final = table_df.to_html(header=False,index=False)

    # browser.quit()

    # Scrape Mars hemisphere from: marshemispheres.com
    # browser = init_browser()
    hemisphere_url = "https://marshemispheres.com/"
    browser.visit(hemisphere_url)
    html = browser.html
    soup = bs(html,'html.parser')

    ht = soup.find_all('div',class_='description')

    hemispheres = []

    for i in ht:
        headers = i.find('h3')
        hemispheres.append(headers.text)

    html = browser.html
    soup = bs(html,'html.parser')

    hi = soup.find_all('div',class_='item')
    hemisphere_img = []

    for i in hi:
        links = i.a['href']
        hemisphere_img.append(f'https://marshemispheres.com/{links}')

    hemisphere_enhanced_img = []

    for j in hemisphere_img:
    
        browser.visit(j)
    
        html = browser.html
        soup = bs(html,'html.parser')
    
        enhanced_img = soup.find_all('img',class_='wide-image')
        enhanced_img_url = enhanced_img[0]['src']
    
        hemisphere_enhanced_img.append(f'https://marshemispheres.com/{enhanced_img_url}')
    hemisphere_zip = zip(hemispheres ,hemisphere_enhanced_img)
    hemisphere_final = []
    for a, b in hemisphere_zip:
        hemisphere_final_dict = {}
    
        hemisphere_final_dict['title'] = a
    
        hemisphere_final_dict['img_url'] = b
    
        hemisphere_final.append(hemisphere_final_dict)
    browser.quit()
    data = {
        'latest_news_title': title,
        'latest_news_paragraph': paragraph,
        'mars_image': featured_image_url,
        'mars_facts': table_final,
        'hemispheres': hemisphere_final
    }
    # browser.quit()
    
    return data
