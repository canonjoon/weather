import requests
from bs4 import BeautifulSoup

#네이버 지역 날씨
def n_weather_data(location):
    n_url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(location+' 날씨')
    n_r= requests.get(n_url)
    n_soup=BeautifulSoup(n_r.text , 'lxml')
    #print(soup.text)
    #지역 이름
    local_data=[]
    n_test_html = n_soup.select_one('div[class=sc_head] > h2')
    if not n_test_html :
        local ={"지역정보":"없음","지역온도":"없음","지역날씨":"없음"}
        return local

    n_localname = n_soup.select_one('div[class=select_box] > span[class=btn_select] > em')
    if not n_localname:
        n_localname=n_soup.select_one('div[class=select_box] > a > em')
    #print(n_localname.text)
    n_localname=n_localname.text
    
    #지역 현재온도
    n_localde=n_soup.select_one('span[class=todaytemp]').text
    #print(n_localde.text)
    #지역 현재날씨
    n_localwea=n_soup.select_one('p[class=cast_txt]').text
    #print(n_localwea.text)
    local_data.append(n_localname)
    local_data.append(n_localde)
    local_data.append(n_localwea)

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
        
        if (j==8):
            break

    for k in n_localtw :
        wt=k.text
        wea.append(wt)
        h=h+1

        if (h==8):
            break
        
    #print(time)

    local = {'local':n_localname,'deg':n_localde,'weath':n_localwea,}
    
    return local        


if __name__ == "__main__":
    print(n_weather_data("부산서면"))