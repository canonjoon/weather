from flask import Flask, render_template, request 
import weather_data
import weather_time
from datetime import date, timedelta
from datetime import datetime



#플라스크 앱 서버 인스턴스
app = Flask(__name__)

#url 패턴 - 라우터 설정
@app.route('/')
def index():
    
    # now = date.today()
    # now_str=now.strftime("%m%d%H%M")
    now_time = datetime.now()
    time_hour =now_time.strftime('%m월%d일 - %H시')


    local = request.args.get('local1')
    #local = "강남"
    if not local : local=" "
    data = weather_data.n_weather_data(local)
    time = weather_time.n_weather_time(local)
    
    return render_template("index.html", data=data,time=time, time_hour=time_hour) 


#메인 테스트
if __name__ == "__main__":
    app.run(debug=True)

