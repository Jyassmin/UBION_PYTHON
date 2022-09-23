#웹서버 Database, Pandas를 결합!
from flask import Flask, render_template, request, redirect
import pymysql
import pandas as pd
import mod_sql

# __name__ : 현재 실행이 되고 있는 파일의 이름(main.py)
app = Flask(__name__)

# api 생성

# localhost:5000/ 를 호출 했을 때 뭔가의 행동을 하겠다.
# 행동을 하는 주체 : 서버
@app.route("/")
def index():
    # return "Hello World"
    # index.html에서 정의한 body를 리턴하여 웹에 표시
    return render_template("index.html")

# 로그인
## 유저의 ID, password 값을 받아와서 sql을 통해 데이터를 확인하여
## 로그인 성공, 실패 여부 확인
@app.route("/login", methods=['post'])
def login():
    _id = request.form["_id"]
    _pass = request.form["_pass"]
    print(_id, _pass)
    ## sql을 통해서 _id, _pass 같은 데이터를 확인
    db = mod_sql.Database()
    sql = """
        select *
        from user_info
        where ID=%s and password=%s
    """
    values = [_id, _pass]
    result = db.executeall(sql, values)
    #웹에는 dataframe형태로 리턴하면 안되기에 __init__.py에서의 executeall의 return을 self.result로 바꾼다.
    
    if result:
        # return render_template("main.html")
        # #페이지로 바로 가지 않고 /main 루트로 가서. sql문을 더 실행하고 결과(sales)를 main.html과 함께 표시
        return redirect("/main")
    else:
        return redirect("/")


@app.route("/main")
def main():
    ## sql 접속
    ## data를 가지고 와서 테이블 형태로 페이지에서 출력
    db = mod_sql.Database()
    sql = """
        select Region, AVG(`Total Cost`) as AVG_Cost
        from `sales records`
        group by Region
        limit 100
    """
    result = db.executeall(sql)
    print(result)
    # html에서, {%%} 안에서는 파이썬코드를 사용할수 있다. ~~ {%`endfor%}. but len함수가 사용이 안되서 route에서 변수(cnt)로 가져옴
    cnt = len(result)
    # result 값을 데이터프레임 변경
    ## region 컬럼의 값을 리스트로 region변수에 삽입
    ## AVG_Cost 컬럼의 값을 리스트 형태로 avg변수에 삽입
    df = pd.DataFrame(result)
    region = df["Region"].to_list()
    avg = df["AVG_Cost"].to_list()
    
    # render_template(템플릿파일 안 파일이름, 해당파일에서 사용할 변수이름=위에서만든 변수) -> 변수를 받아 해당html을 실행
    return render_template("main.html", sales = result, cnt = cnt,
                        region = region, avg = avg)
    

# Database랑 연결하기!
## 회원 정보 추가
## 회원 가입 페이지
@app.route("/signup")
def signup():
    return render_template("signup.html")


# 웹 서버에 호출하는 방식
## get, post
## get : 유저가 데이터를 보낼 때 url에 실어서 보내는 방법 / url으로 웹 직접 접속
### get형식 - 데이터를 받아오는 방법 request.args[key]
## post : 유저가 데이터를 보낼 때 request 메시지 안에 body를 실어서 보내는 방법 / 전에 어떤 페이지를 통해 웹 접속
### post형식 - 데이터를 받아오는 방법 request.form[key]
@app.route("/signup2", methods=["POST"])
def signup2():
    #1)유저가 보낸 데이터를 변수에 삽입을 하는 구간
    _id = request.form["_id"]
    _pass = request.form["_pass"]
    _name = request.form["_name"]
    _birth = request.form["_birth"]
    _phone = request.form["_phone"]
    print(_id, _pass, _name, _birth, _phone)
    
    #2)이 변수들을 sql에 추가
    db = mod_sql.Database()
    sql = """
            insert into user_info
            values (%s, %s, %s, %s, %s)
    """
    values = [_id, _pass, _name, _birth, _phone]
    db.execute(sql, values)
    db.commit()
    db.close()

    #3)로그인 페이지로 이동
    return redirect("/")

# 웹서버 오픈
app.run()

## 파일경로 복사 후 터미널에 실행 cd /Users/kyle/UBION_python/220920
### python.py를 실행하면 서버가열려 해당 주소(http://127.0.0.1:5000/)로 접속 가능