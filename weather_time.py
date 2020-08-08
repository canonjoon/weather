import requests
from bs4 import BeautifulSoup


def n_weather_time(location) : 
    
    n_url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(location+' 날씨')
    n_r= requests.get(n_url)
    n_soup=BeautifulSoup(n_r.text , 'lxml')

    
    n_test_html = n_soup.select_one('div[class=sc_head] > h2')
    if not n_test_html :
        local ={"시간대별 날씨":"없음"}
        return local

    n_localt = n_soup.select('dd[class=item_time] > span')
    j=0
    h=0
    y=0
    data={}
    time=[] # 시간 구하기
    wea=[] # 시간별 날씨 구하기
    #시간별 날씨
    n_localtw=n_soup.select('dd[class=item_condition]')

    for i in n_localt :
        hour = i.text
        time.append(hour)
        j=j+1
        
        if (j==8):
            break

    for k in n_localtw :
        wt=k.text
        wea.append(wt)
        h=h+1

        if (h==8):
            break
    
    for t in time :
        data[t]=wea[y]
        y=y+1

    
    return data

if __name__ == "__main__":
    print(n_weather_time("부산서면"))