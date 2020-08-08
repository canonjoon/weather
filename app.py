from flask import Flask, render_template, request 
import weather_data
import weather_time


#플라스크 앱 서버 인스턴스
app = Flask(__name__)

#url 패턴 - 라우터 설정
@app.route('/')
def index():
    
    local = request.args.get('local1')
    #local = "강남"
    if not local : local=" "
    data = weather_data.n_weather_data(local)
    time = weather_time.n_weather_time(local)
    
    return render_template("index.html", data=data,time=time) 


#메인 테스트
if __name__ == "__main__":
    app.run(debug=True)

