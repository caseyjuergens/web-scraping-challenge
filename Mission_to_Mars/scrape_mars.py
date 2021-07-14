from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():
    browser=init_browser()
    #url of redscience page to be scraped
    red_url= 'https://redplanetscience.com/'
    browser.visit(red_url)
    html= browser.html
    soup= bs(html, 'html.parser')

    #scrape news title
    news_title= soup.find('div', class_='content_title').text
    print(news_title)

    #scrape paragraph text
    news_p= soup.find('div', class_='article_teaser_body').text
    print(news_p)

    #url of space image site to be scraped
    image_url= 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    for x in range(1):
        html=browser.html
        soup= bs(html, 'html.parser')
        link_button= soup.find('div', class_='floating_text_area')
        browser.click_link_by_partial_text('FULL IMAGE')
        
        image_box=soup.find('a', class_="showimg fancybox-thumbs")
        pic_url=image_box['href']
        
        #print(pic_url)

    #put together url
    featured_image_url= image_url+pic_url
    print(featured_image_url)

    #url of facts site
    facts_url='https://galaxyfacts-mars.com/'
    facts_table=pd.read_html(facts_url)
    table_df= facts_table[0]
    table_df.head()

    facts_table_html= table_df.to_html()
    facts_table_html
    
    #url of hemispheres site
    hemi_url='https://marshemispheres.com/'
    browser.visit(hemi_url)
    html= browser.html
    soup= bs(html, 'html.parser') 
    hemis= soup.find_all('h3', limit=4)
    print(hemis)

    hemispheres_dict={'title':[hemis],'img_url':[]}
    print(hemispheres_dict)

    #reset browser
    hemi_url='https://marshemispheres.com/'
    browser.visit(hemi_url)
    html= browser.html
    soup= bs(html, 'html.parser')

    for i in range(4):
        browser.find_by_css('a.itemLink h3')[i].click()
        hemispheres_dict['img_url']= browser.find_by_text('Sample')['href']
        browser.back()
    print(hemispheres_dict)


    browser.quit()

    scrape_dict={
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "hemi_dict": hemispheres_dict
    }



    return scrape_dict