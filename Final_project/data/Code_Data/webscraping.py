#!/usr/bin/python

from bs4 import BeautifulSoup
from urlparse import urljoin
import requests

base = "http://www.who.int"

url_list = ['http://www.who.int/mediacentre/factsheets/fs297/en/','http://www.who.int/cancer/nccp/en/','http://www.who.int/gho/ncd/mortality_morbidity/cancer/en/','http://www.who.int/gho/ncd/mortality_morbidity/cancer_text/en/','http://www.who.int/hrh/statistics/minimun_data_set/en/','http://www.who.int/ith/links/national_links/en/','http://www.who.int/hrh/resources/en/','http://www.who.int/hrh/links/en/','http://www.who.int/cancer/publications/en/','http://www.who.int/healthinfo/statistics/mortality_rawdata/en/']

# Iterate through all the required URLs and find the links with downloadable files.

for url in url_list:
    page = requests.get(url)
    bs = BeautifulSoup(page.content,'html.parser')

#Scrape all the download links from each URL
    lists =  bs.find_all('a', class_ = "link_media",href = True)

    length = len(lists)
    print "The number of documents available for download in the URL: " + url + " are  " + str(length)
    print ""
    print ""



# For each downloadable link get the URL and the info about the file
    for l in lists:
        href = l.get('href')
        link = urljoin(base,href)
        print "*********************************************"
        print "*********************************************"
        print link
        print l.next_sibling.next_sibling


    print "*********************************************"
