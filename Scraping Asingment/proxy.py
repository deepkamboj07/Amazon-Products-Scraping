import requests
from bs4 import BeautifulSoup
def getProxies():
    url="https://free-proxy-list.net/"
    soup=BeautifulSoup(requests.get(url).text,'html.parser')

    proxies=[]
    proxtTab=soup.find("table").find_all("tr")[1:]

    for row in proxtTab:
        tds=row.find_all("td")
        try:
            ip=tds[0].text.strip()
            port=tds[1].text.strip()
            proxies.append(str(ip)+":"+str(port))
        except IndexError:
            continue


    return proxies


