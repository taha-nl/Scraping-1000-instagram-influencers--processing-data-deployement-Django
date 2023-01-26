### importing Libraries

import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

if __name__=='__main__':
    
    browser=uc.Chrome()

    browser.maximize_window()

    time.sleep(3)### waiting for three seconds  

    profiles=pd.read_csv('username_scraped.csv')#loading  profiles already scraped
    profiles=list(profiles["username"].astype("str"))
    liste=map(lambda x: x.replace("@",""),profiles)
    
    prf=list(liste)
    
    for compte in prf:
        try:

            url =f"https://www.instagram.com/{compte}/?hl=fr"

            #sending request to url
            browser.get(url)
            #extracting data from the source as this example using CSS_SELECTOR:
            """
           ['11M', 'followers,', '3,221', 'suivis,', '10K', 'publications', '-', 'Voir', 'les', 'photos', 'et',
                                                             'vidéos', 'Instagram', 'de', 'Heart', 'Evangelista', '(@iamhearte)']
            """
            data = browser.find_element(By.CSS_SELECTOR,("meta[property='og:description']"))
            text = data.get_attribute('content').split()

            ##getting the DATA

            username=text[-1][2:-1]#getting the username(@iamhearte) and removing @ and parentheses 
            name=" ".join(text[-3:-1]) # getting and joining the name together
            number_followers=text[0] #extracting number of followers
            number_following=text[2]#extracting number of following
            number_publi=text[4]#extracting number of publications

            ## Loading the Data in a csv file
            with open('instagram_scrapping.csv', 'a') as myFile:
                myFile.write(name +","+username+","+number_following+","+number_followers+","+number_publi+"\n")
        except:
            pass
        

        

   




   