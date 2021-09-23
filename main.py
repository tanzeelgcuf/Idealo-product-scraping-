import bs4
import requests 
from bs4 import BeautifulSoup

from openpyxl import load_workbook
import xlrd
import xlsxwriter   
from xlwt import Workbook 
import xlwt 


wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'title')
sheet1.write(0, 1, 'price')
sheet1.write(0, 2, 'src')
sheet1.write(0, 3, 'href')



def function(id):
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36',
              'Accept-Language': 'en-US, en;q=0.5',
                    'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.bauhof.ee/et/tooriistad',
                 
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authority': 'https://www.bauhof.ee/et/tooriistad',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                 })
    
    link = 'https://www.amazon.de/s?k=PIPING+TOOLS&page='+str(id)+'&language=en'
    r = requests.get(link,headers=HEADERS)
    link = BeautifulSoup(r.content, 'html.parser')
    return link


k=1        
for i in range(1,15):
    link=function(i)
     #Garden tools
    soup = link.find('div',{'class','s-main-slot s-result-list s-search-results sg-row'}).find_all('div')

    z1=''
    z2=''

    for i in soup:
        try:
            z=i.find('span',{'class','a-size-base-plus a-color-base a-text-normal'}).text
            #a-size-medium a-color-base a-text-normal
            #a-size-base-plus a-color-base a-text-normal
            zz=i.find('span',{'class','a-offscreen'}).text
        except:
            zz='p'
            z='p'
        if zz=='p' or z=='p':
            continue
        if z1!=z and z2!=zz:
            z1=z
            z2=zz
        else:
            continue
        hre=i.find('a',{'class','a-link-normal a-text-normal'})['href']
        
        
        href='amazon.de'+hre
        title=z1+"\n"
        src=i.img['src']
        price=zz
       
        

        sheet1.write(k, 0, title)
        sheet1.write(k, 1, price)
        sheet1.write(k, 2, src)
        sheet1.write(k, 3, href)
      
        k+=1
        
wb.save('amazon_de/Piping Tools.xls')
    





























"""
    k=1
    for i in soup:
        href=i.a['href']
        title=i.find('a',{'class','product-item-link'}).text.strip()
        price=i.find('span',{'class','price'}).text
        src=i.img['src']
"""



