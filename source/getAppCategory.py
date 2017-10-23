import requests
import csv
from bs4 import BeautifulSoup


class GooglePlay(object):
        def getPlaystoreDetail(self, app, longapp):
                
                app_page = requests.get(app)
                soup = BeautifulSoup(app_page.content, 'html.parser')		
                title = soup.select('div.id-app-title')
                                                
                try:
                        app_cat = soup.find("span", {"itemprop": "genre"}).text
                except:
                        app_cat = "not found"

                app_details = dict()
                try:
                        app_details['title'] = title[0].text
                except:
                        app_details['title'] = "not found"
                app_details['app_category'] = app_cat
                return app_details




playstore = GooglePlay()
appPrefix = "https://play.google.com/store/apps/details?id="

i = 0
fp = open('appresults.csv', 'a', newline='')
a = csv.writer(fp, delimiter="|")

with open('applist.csv', 'r') as infile:
        for fileline in infile:
                output_list =[]
                i = i + 1
                line = fileline.strip()           

                app_url = appPrefix + line
                app_details =  playstore.getPlaystoreDetail(app_url,line)
                output_list.append([line,app_details['title'].encode("utf-8"),app_details['app_category'].encode("utf-8")])
                a.writerows(output_list)                
        fp.close()
