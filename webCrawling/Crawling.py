import csv
import requests
import lxml
import unicodedata
from bs4 import BeautifulSoup

#To write data in CSV format

f = open("D:/test.csv", 'wt')
writer = csv.writer(f)
writer.writerow( ('Show Name', 'URL', 'Number Of Episodes', 'Number Of Seasons') )

#URL of Couch-tuner web site
Couch_url='http://www.couch-tuner.bz/tv-shows/#.V-Z06aJS3Gt'
r=requests.get(Couch_url)
soup = BeautifulSoup(r.content,'lxml')

g_data = soup.find_all("div", class_="parentdiv")

for element in g_data:
    links=element.findAll('a')  # "a">> anchor tag in the web page
    for a in links:
        tvShow_url= a['href']

        title=a.string
        title=title.encode("utf-8")
        
        print title        #To print Name of Tv Show
        
        print tvShow_url   #To print URL link of TV show
        
        r2=requests.get(tvShow_url)
        soup2 = BeautifulSoup(r2.content,'lxml')
        g_data2= soup2.findAll('span',class_='catDivTest')      # To find episodes of TV show in web page
        g_data3= soup2.findAll('h2',style="margin-left:15px;")  # To find seasons of TV show in web page

        #To count Number of Episodes of each TV show
        
        count=0
        for span in g_data2:
           #print span
           count +=1
        print count
        
        #To count number of seasons of each TV show
        
        count2=0
        for h2 in g_data3:
          #print span
          count2 +=1
        if(count2==0 and count!=0):
         count2=1
        print count2

        writer.writerow((title,tvShow_url,count,count2))       

f.close()   
           
           
        










    
    



  
    
        
        
    


