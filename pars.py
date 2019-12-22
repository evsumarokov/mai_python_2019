
import requests # импортируем библиотеку. предварительно необходимо установить ее в python: pip install requests
from bs4 import BeautifulSoup, BeautifulStoneSoup # для парсинга веб-страниц понадобится библиотека BeautifulSoup. устанвока: pip install bs4
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}


# веб-адрес страницы АК "Россия", с которой мы будем получать информацию
air_dict={}
air_dict.setdefault('АК "Россия"', [])
url_rossiya = r"https://www.rossiya-airlines.com/about/about_us/fleet/aircraft/"
try:
    r = requests.get(url_rossiya, headers=headers)
    bs = BeautifulSoup(r.text, "lxml")
    div_bs = bs.find_all("table", attrs={"class":"no-lines"})
    rows_bs = div_bs[1].find_all("tr", attrs={"style":"background-color: #ffffff;"})
    planes=[]
    for i in rows_bs:
        name=i.find("h2").text
        
        a=i.find_all('span', attrs={'style':f'color: #626262;'})
        b=i.find_all('span', attrs={'style':f'color: #707070;'})
        c=i.find_all('span', attrs={'style':f'color: #555555;'})
        r_list=[]
        if len(a)>0:
            r_list=a
        elif len(b)>0:
            r_list=b
        else:
            r_list=c
        planes.append({"Имя":name,"Размах крыла":''.join(re.findall(r'\d*[,]\d[/]\d*[,]\d|\d*[,]\d', r_list[-6].text)),"Число мест":''.join(re.findall(r'\d*|\d*[/]\d*', r_list[-5].text)),'Макс. взлетный вес':''.join(re.findall(r'\d*|\d*[/]\d*', r_list[-4].text)),"Крейсерская скорость":''.join(re.findall(r'\d*', r_list[-3].text)),"Макс. высота полета":''.join(re.findall(r'\d*', r_list[-2].text)),"Макс. дальность полета":''.join(re.findall(r'\d*', r_list[-1].text))})
    air_dict.update({'АК "Россия"':planes})
           
except Exception as e:
    print(e)
print(air_dict)