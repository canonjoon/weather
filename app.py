from flask import Flask, render_template, request 



#플라스크 앱 서버 인스턴스
app = Flask(__name__)

#url 패턴 - 라우터 설정
@app.route('/')
def index():
    

    return render_template("index.html") 


#메인 테스트
if __name__ == "__main__":
    app.run(debug=True)

