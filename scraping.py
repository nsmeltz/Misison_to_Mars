
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


# 1. Mars Nasa News Site Article Scraping 

# Create instance of Splinter & initialize Chrome browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the target URL (Mars Nasa News Site)
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Get the html content of the visited page
html = browser.html

# Create BeautifulSoup object & parse with 'html.parser'
news_soup = soup(html, 'html.parser')

# Create a variable (ie parent element) to hold all html info under 
# the div tag with class list_text w/ the things we want to scrape

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the title of the 1st listed article and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the summary text of the 1st listed article and save it as `news_p`
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# 2. Jet Propulsion Labratory's Images Scraping

# Visit the target URL (Jet Propulsion Laboratory's Space Images website)
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
# the full image button is the second instance of the <button> tag so use index [1]
full_image_elem = browser.find_by_tag('button')[1].click()

# Get the html content of the visited page
html = browser.html

# Create BeautifulSoup object (img_soup) & parse with 'html.parser'
img_soup = soup(html, 'html.parser')


# Find the relative image url for the image that is pulled up after clicking on the full image button
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Close down browser
browser.quit()

# 3. Mars Facts Table Scrape

# Use Pandas read_html function to scrape a whole table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# convert our dataframe back to html for adding to webpage
df.to_html()






