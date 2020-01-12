from bs4 import BeautifulSoup
from selenium import webdriver
import itertools

# Specify the configuration for the Chrome webdriver.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')

# Start the Chrome webdriver (i.e., the web browser).
driver = webdriver\
    .Chrome(
            executable_path = 'chromedriver',
            options=options)

def get_upnextchain(startid): #startid should look like '6LtEO8lYc3k'
    chain=[]
    videoid= startid
    for _ in itertools.repeat(None, 9):
        driver.get('https://www.youtube.com/watch?v='+videoid)
        soup=BeautifulSoup(driver.page_source, 'lxml')
        # related videos are not easily identifiable, so this part was obtained through trial and error
        # I'm not proud of it but it works
        scripts = soup.find_all("script")
        allscripts=[]
        for script in scripts:
            allscripts.append(str(script))
        related = [script for script in allscripts if "window[\"ytInitialData\"]" in script]
        related = related[0].replace(',',' ').replace('{', ' ').replace('}', ' ').split()
        urls = [text for text in related if "/watch?v" in text]
        # first vid is "Up Next"
        relatedid=[]
        for url in urls:
            relatedid.append(url.replace('\"','').split("=")[1])
        upnextid=relatedid[0]
        videoid = upnextid
        if upnextid not in chain and upnextid is not startid: #skipping repeated videos
            chain.append(upnextid)
    return chain
