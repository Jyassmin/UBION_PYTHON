from flask import Flask #Flask라는 클래스를 가져오겠다

#__name__ : 파일의 이름
app = Flask(__name__)

@app.route("/")     #127.0.0.1:5000/ 로 접속(요청)했을 때 아래의 함수를 실행한다.
def index():
    return "Hello World"

@app.route("/second")   #127.0.0.1:5000/second 로 접속했을 때 아래 함수 실행
def second():
    return "Second Page"


app.run()