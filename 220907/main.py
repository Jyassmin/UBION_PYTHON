from flask import Flask, render_template, request, redirect
import pandas as pd

#Flask라는 Class에서 __init__ 함수에 self를 제외한 매개변수 1개 "__name__"
#__name__ : 파일의 이름(main.py)
app = Flask(__name__)


# api 생성
# 127.0.0.1 = localhost
# 5000은 port번호 : 방화벽 문번호(여기 문을 열어두겠다)
# @app.route() -> localhost:5000 요청이 있는 경우에 바로 아래에 있는 함수를 실행

@app.route("/")     #127.0.0.1:5000/ 로 접속(요청)했을 때 아래의 함수를 실행한다.
def index():
    return render_template("index.html")

# get 형식에서 데이터는 url에 실어서 보낸다.
# request -> 유저가 서버에게 보내는 데이터를 dict 형태로 출력
# 유저가 보낸 데이터 중에 url에 있는 데이터는 : request.args 에 있음
@app.route("/second")   #127.0.0.1:5000/second 로 접속했을 때 아래 함수 실행
def second():
    _id = request.args.get("ID") #index.html에 입력된 ID를 가져와서 저장
    _pass = request.args.get("password")
    
    
    # id값과 password값
    # id는 test, password는 1234
    # 위의 조건을 만족해야만 second.html 리턴
    # 위의 조건이 거짓이면 "로그인 실패" 리턴
    
    print(request) # 실행안돼서 일단 무시
    
    # if (_id == "test") and (_pass == "1234"):
    #     return render_template("second.html")
    # else:
    #     # return "로그인 실패"
    #     # 위처럼 써도 되고 redirect라는 모듈을 가져와 아래 같이 사용해 원래 페이지로 돌아가도록함
    #     redirect("/")
        
    return render_template("second.html")
        
        
# *POST는 localhost:5000/third를 직접주소입력이 아닌 요청 방식(form action='/third')으로만 이동가능하게한다.
@app.route("/third", methods=["post"])
def third():
    _title = request.form["title"]
    _content = request.form["content"]
    print(_title, _content)
    # 웹에 페이지와 변수도 같이 보낸다.
    return render_template("third.html", content=_content, title=_title)


@app.route("/dashboard")
def dashboard():
    print("dashboard")
    
    df = pd.read_csv("../csv/corona.csv")
    #컬럼의 이름을 변경
    df.columns = ["인덱스", "등록일시", "사망자", "확진자", "게시글번호", "기준일", "기준시간", "수정일시", "누적의심자", "누적확진률"]
    #등록일시 기준으로 오름차순 정렬
    df.sort_values("등록일시", inplace = True)
    #일일 확진자, 일일 사망자 라는 파생변수 생성
    df["일일확진자"] = df["확진자"] - df["확진자"].shift()
    df["일일사망자"] = df["사망자"].diff()
    data = df.head(10)
    _cnt = len(data)
    _decide_data = data["일일확진자"].tolist()
    _date_list = data["등록일시"].tolist()
    _death_data = data["일일사망자"].tolist()
    
    return render_template("dashboard.html", cnt=_cnt, date_list=_date_list, decide_data=_decide_data, death_data=_death_data)

#웹서버를 실행하겠다
app.run()


## 실제 서버와 유저간의 데이터 이동
## dict형태의 데이터로 request / response
## request -> 유저가 서버에게 보내는 데이터
## response -> 서버가 유저에게 보내는 데이터
## request {
        # key : value,
        # key2 : value2,
        # args : {
            # ID : input에서 입력한 값(ID),
            # password : input에서 입력한 값(password
                # }
        # }
# request["args"]["ID"] == request.args.get("ID")
        