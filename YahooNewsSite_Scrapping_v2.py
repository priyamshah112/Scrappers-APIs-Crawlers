#For Scraping NewsSite (YAHOO NEWS)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body
from selenium import webdriver #For JavaScriptEnabled Sites
import os # For Making Directory of particular Topic
import errno #For error checking
 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://www.yahoo.com/news/us/','https://www.yahoo.com/news/world/',
                 'https://www.yahoo.com/news/politics/','https://finance.yahoo.com/tech/','https://www.yahoo.com/news/science/',
                 'https://finance.yahoo.com/','https://www.yahoo.com/news/now-i-get-it',
                 'https://www.yahoo.com/gma','https://www.yahoo.com/news/originals/'}
                 #+ str(page)


        for i in url:
                #For creating a directory of each category
                filename = "C:/YahooNews/"+i.split('/')[-2]+"/"
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                
            
                for link in soup.findAll('a',{'class':'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)'}):
                
                    href ="https://www.yahoo.com/" + link.get('href')
                    #headlines = link.string
                    article =   Article(href)
                    article.download()
                    article.html
                    article.parse()
                    with open(filename+"/"+article.title,'w') as t:
                            t.write("\t \t \t \t LINK TO NEWS \n"+href +"\n"+"\t \t \t \t HEADLINE \n"+article.title+"\n"+"\t \t \t \t CONTENT \n"+article.text+"\n"+"\t \t \t \t IMAGE LINK \n"+article.top_image+"\n")
                    comments_article(href,article.title,filename)
                        
def comments_article(addr,headline,filename):
        
        driver = webdriver.Firefox(executable_path=r'C:\firefoxdriver\geckodriver.exe') #Using firefox driver 
        driver.get(addr) # Calling url
        html = driver.execute_script("return document.documentElement.outerHTML") #Giving client site call to site for loading javascript and then scraping
        soup = BeautifulSoup(html,'html.parser')
        driver.close() 
        #print(sel_soup.prettify())
        with open(filename+"/"+headline,'a') as t:
            #For name of commenter
                for commenter in soup.findAll('div',attrs={'class':'D(ib) Fw(b) Mend(10px) Fz(14px) C($c-fuji-blue-1-a) Cur(p)'}):
                    t.write("\t \t \t \t COMMENTER  \n"+commenter.get_text()+"\n")
            #For Comments    
                for comments in soup.findAll('div',attrs={'class':'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'}):
                    t.write("\t \t \t \t COMMENTS \n"+comments.get_text()+"\n")
            #For Replies
                for replies in soup.findAll('div',attrs={'class':'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'}):
                    t.write("\t \t \t \t REPLIES \n"+replies.get_text()+"\n")
            #For Comment Likes
                for like in soup.findAll('button',attrs={'class':'O(n) Bgc(t) Bdc(t) M(0) P(0) Bd(n) Mend(12px)'}):
                    t.write("\t \t \t \t LIKE ON COMMENT \n"+like.get_text()+"\n")
            #For Comment Dislikes
                for dislike in soup.findAll('button',attrs={'class':'O(n) Bgc(t) Bdc(t) M(0) P(0) Bd(n)'}):
                    t.write("\t \t \t \t DISLIKE ON COMMENT \n"+dislike.get_text()+"\n")
            #For News Likes
                for happy in soup.findAll('span',attrs={'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-green-1-b) Pend(6px)'}):
                    t.write("\t \t \t \t LIKES ON NEWS \n"+happy.get_text()+"\n")
            #For News Dislikes
                for sad in soup.findAll('span',attrs={'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-red-2-a)'}):
                    t.write("\t \t \t \t DISLIKE ON NEWS \n"+sad.get_text()+"\n")
            #For News Neutrals    
                for neutrals in soup.findAll('span',attrs={'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-orange-b) Pend(6px)'}):
                    t.write("\t \t \t \t NEUTRALS ON NEWS \n"+neutrals.get_text()+"\n")
                #page+=1

main_news() #trade_spider(page)
