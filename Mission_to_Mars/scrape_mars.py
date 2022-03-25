# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# NASA Mars News

def scrape_info():

    # URL of page to be scraped
    url = "https://www.redplanetscience.com/"

    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Launch browser
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract news title
    results = soup.find_all('div', class_="content_title")

    # Iterate through list to pull out text of the news titles
    news_title = []

    for title in results:
        news_title.append(title.text)

    # Extract news paragraph text
    results = soup.find_all('div', class_='article_teaser_body')

    # Iterate through list to pull out text of the news body
    news_p = []

    for p in results:
        news_p.append(p.text)
        
    # JPL Mars Space Mission

    # Define the URL
    url = "https://spaceimages-mars.com"

    # Launch browser
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract feature image data
    results = soup.find('img', class_="headerimage")

    featured_image_url = results['src']
    featured_image_url = f'{url}/{featured_image_url}'

    # Mars Facts

    # Define the URL
    url = "https://galaxyfacts-mars.com"

    # Read the tables in the URL and import
    tables = pd.read_html(url)

    # Identify the table with the Mars information and clean-up.
    mars_table = tables[1]
    mars_table = mars_table.rename(columns={0:'Fact Title', 1:'Fact Value'})

    # Convert the table to HTML string
    mars_table_html = mars_table.to_html()
    mars_table_html = mars_table_html.replace('\n','')

    # Mars Hemispheres

    # Initiate list of dictionaries
    hemisphere_image_urls = []

    # Cerberus Hemisphere

    # Define the URL
    url = "https://marshemispheres.com/cerberus.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract title
    title = soup.find('h2', class_="title").text

    # Define the URL
    url = "https://marshemispheres.com/cerberus.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract feature image data
    hemisphere_image = soup.find('img', class_="wide-image")

    img_url = hemisphere_image['src']
    img_url = f'https://marshemispheres.com/{img_url}'

    # Append into a dictionary
    hemisphere_image_urls.append({"title":title, "img_url":img_url})

    # Schiaparelli Hemisphere

    # Define the URL
    url = "https://marshemispheres.com/schiaparelli.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract title
    title = soup.find('h2', class_="title").text

    # Define the URL
    url = "https://marshemispheres.com/schiaparelli.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract feature image data
    hemisphere_image = soup.find('img', class_="wide-image")

    img_url = hemisphere_image['src']
    img_url = f'https://marshemispheres.com/{img_url}'

    # Append into a dictionary
    hemisphere_image_urls.append({"title":title, "img_url":img_url})

    # Syrtis Hemisphere

    # Define the URL
    url = "https://marshemispheres.com/syrtis.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract title
    title = soup.find('h2', class_="title").text

    # Define the URL
    url = "https://marshemispheres.com/syrtis.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract feature image data
    hemisphere_image = soup.find('img', class_="wide-image")

    img_url = hemisphere_image['src']
    img_url = f'https://marshemispheres.com/{img_url}'

    # Append into a dictionary
    hemisphere_image_urls.append({"title":title, "img_url":img_url})

    # Valles Hemisphere

    # Define the URL
    url = "https://marshemispheres.com/valles.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract title
    title = soup.find('h2', class_="title").text

    # Define the URL
    url = "https://marshemispheres.com/valles.html"

    # Visit URL
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object, parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # Extract feature image data
    hemisphere_image = soup.find('img', class_="wide-image")

    img_url = hemisphere_image['src']
    img_url = f'https://marshemispheres.com/{img_url}'

    # Append into a dictionary
    hemisphere_image_urls.append({"title":title, "img_url":img_url})

    # Close the browser after scraping
    browser.quit()

    mars_dict = {
        "news_title": news_title, 
        "news_p": news_p, 
        "featured_image_url": featured_image_url, 
        "mars_table_html": mars_table_html, 
        "hemisphere_image_urls": hemisphere_image_urls
        }

    # Return results
    return mars_dict


