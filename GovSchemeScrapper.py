#Government Schemes Scraping code
import requests
from bs4 import BeautifulSoup


def main():

    link = 'https://www.india.gov.in/topics/'
    link2 = 'https://www.india.gov.in'
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')

    filename = 'Topics.csv'


    for i in soup.findAll('a',{'role':'link'}):
        try:
            href = i.get('href')
 
            if 'topics' in href:
                #print(href)
                source_code1 = requests.get('https://www.india.gov.in'+href)
                plain_text1 = source_code1.text
                soup1 = BeautifulSoup(plain_text1,'lxml')

                quick_tab = []
                
                for j in soup1.select('ul.quicktabs-style-basic li a[href]'):

                    #quick_tabs[j.text] = j.get('href')
                    quick_tab.append(j.get('href'))
                #print(quick_tab)
                
##                for k in quick_tabs:
##
##                    source_code2 = requests.get('https://www.india.gov.in'+k)
##                    plain_text2 = source_code2.text
##                    soup2 = BeautifulSoup(plain_text2,'lxml')
##
##                    print(k.text)
##
##                    for l in soup2.select('div.block-inner div.block-content ul li a[href]'):
##
##                        print(i.text)
                    
                    
##                for j in soup1.findAll('li',{'class':'even','class':'odd'}):
##                    for k in j.findAll('a'):
##                        #print(k.get('href'))
##                        quick_tab.append(k.get('href'))
##                print(quick_tab)
##                with open(filename,'a') as t:
##                    t.write('https://www.india.gov.in'+href+"\n")
##                t.close()
        except:
            continue

main()  
