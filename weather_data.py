import requests
from bs4 import BeautifulSoup

#네이버 지역 날씨

n_url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format('강남구')+'날씨'
n_r= requests.get(n_url)
n_soup=BeautifulSoup(n_r.text , 'lxml')
#print(soup.text)
#지역 이름
n_localname = n_soup.select_one('span[class=btn_select]')
print(n_localname.text)
#지역 현재온도
n_localde=n_soup.select_one('span[class=todaytemp]')
print(n_localde.text)
#지역 현재날씨
n_localwea=n_soup.select_one('p[class=cast_txt]')
print(n_localwea.text)


#시간
n_localt = n_soup.select('dd[class=item_time] > span')
j=0
h=0
time=[] # 시간 구하기
wea=[] # 시간별 날씨 구하기
#시간별 날씨
n_localtw=n_soup.select('dd[class=item_condition]')

for i in n_localt :
    hour = i.text
    time.append(hour)
    j=j+1
    
    for k in n_localtw :
        wt=k.text
        wea.append(wt)
        h=h+1
        if (h==8):
            continue
    if (j==8):
        break
#print(time)          


print(time,wea)  
