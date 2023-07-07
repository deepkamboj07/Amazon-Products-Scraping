import requests
import random
from bs4 import BeautifulSoup
from proxy import getProxies
import productModule


#Url list from which we have to scrap products

link="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"

urls=[]
for i in range(1,21):
    string=link+str(i)
    urls.append(string)

#get list of different proxie
proxiList=getProxies()
proxies = {'http': random.choice(proxiList)}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


#Traverse through each url
for url in urls:
    r = requests.get(url,headers=headers,proxies=proxies)
    load=True

    #Loop while we don't find valid IP address which is non blocked by amazon or website
    while(r.ok==False):
        if load:
            print("\n Checking Valid Proxies of new url Loading.......\n")
            load=False
        proxies = {'http': random.choice(proxiList)}
        r = requests.get(url,headers=headers,proxies=proxies)
        
    print("\n Scraping product into file....\n")
    soup=BeautifulSoup(r.text,'html.parser')
    productsDiv=soup.find_all("div",attrs={"data-component-type":"s-search-result"})

    for product in productsDiv:

        prod=product.find("div",attrs={"class":"s-title-instructions-style"}).find("a",attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
        productUrl="https://amazon.in/"+prod.get("href")
        productName=prod.find("span").string
        productPrice=product.find("span",attrs={"class":"a-price-whole"})
        if productPrice:
            productPrice=productPrice.string
        else: 
            productPrice=""
        productRating=product.find("span",attrs={"class":"a-icon-alt"})
        if productRating:
            productRating=productRating.string
        else:
            productRating=""
        customerReview=product.find("span",attrs={"class":"a-size-base s-underline-text"})
        if customerReview:
            customerReview=customerReview.string
        else:
            customerReview=""
        

        #Save into product class
        obj= productModule.Product(productName,productPrice,customerReview,productRating,productUrl)
        obj.writeIntoCSV()

