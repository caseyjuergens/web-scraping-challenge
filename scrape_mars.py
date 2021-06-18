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

    #find title cerberus, get pic url
    for x in range(1):
        #start path to hemi full pic url
        cerberus= soup.find_all('div', class_='item')
        #print(cerberus)
        
        #click link
        browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
        
        html=browser.html
        soup= bs(html, 'html.parser')
        
        #get hemi name
        c_title=soup.find('h2', class_="title").text
        
        #finding pic url
        downloads= soup.find('div', class_='downloads')
        li=downloads.find('li')
        url=li.find('a')['href']
        #print(url)
        
        #add full image url to original url
        cerb_url= hemi_url+url
        #print(cerb_url)
        
        #create dict of hemi name and url
        hemi_dict={
            "title": c_title,
            "url": cerb_url
        }
        print(hemi_dict)

    #reset browser
    hemi_url='https://marshemispheres.com/'
    browser.visit(hemi_url)
    html= browser.html
    soup= bs(html, 'html.parser') 

    #find title schiaparelli, get pic url
    for x in range(2):
        #start path to hemi full pic url
        schia= soup.find_all('div', class_='item')
        #print(schia)
        
        #click link
        browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
        
        html=browser.html
        soup= bs(html, 'html.parser')
        
        #get hemi name
        s_title=soup.find('h2', class_="title").text
        
        #finding pic url
        downloads= soup.find('div', class_='downloads')
        li=downloads.find('li')
        url=li.find('a')['href']
        #print(url)
        
        #add full image url to original url
        schia_url= hemi_url+url
        #print(schia_url)
        
        #create dict of hemi name and url
        hemi_dict[s_title]= schia_url
        print(hemi_dict)

    #reset browser
    hemi_url='https://marshemispheres.com/'
    browser.visit(hemi_url)
    html= browser.html
    soup= bs(html, 'html.parser') 

    #find title syrtis major, get pic url
    for x in range(3):
        #start path to hemi full pic url
        syrtis= soup.find_all('div', class_='item')
        #print(syrtis)
        
        #click link
        browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
        
        html=browser.html
        soup= bs(html, 'html.parser')
        
        #get hemi name
        syr_title=soup.find('h2', class_="title").text
        
        #finding pic url
        downloads= soup.find('div', class_='downloads')
        li=downloads.find('li')
        url=li.find('a')['href']
        #print(url)
        
        #add full image url to original url
        syrtis_url= hemi_url+url
        #print(syrtis_url)
        
        #create dict of hemi name and url
        hemi_dict[syr_title]= syrtis_url
        print(hemi_dict)
        #reset browser

    hemi_url='https://marshemispheres.com/'
    browser.visit(hemi_url)
    html= browser.html
    soup= bs(html, 'html.parser') 

    #find title valles marineris, get pic url
    for x in range(4):
        #start path to hemi full pic url
        valles= soup.find_all('div', class_='item')
        #print(valles)
        
        #click link
        browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
        
        html=browser.html
        soup= bs(html, 'html.parser')
        
        #get hemi name
        v_title=soup.find('h2', class_="title").text
        
        #finding pic url
        downloads= soup.find('div', class_='downloads')
        li=downloads.find('li')
        url=li.find('a')['href']
        #print(url)
        
        #add full image url to original url
        valles_url= hemi_url+url
        #print(valles_url)
        
        #create dict of hemi name and url
        hemi_dict[v_title]= valles_url
        print(hemi_dict)

    browser.quit()

    scrape_dict={
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "hemi_dict": hemi_dict
    }



    return scrape_dict