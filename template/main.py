from flask import Flask, render_template, request, redirect
import pandas as pd

## Class 생성
app = Flask(__name__)

@app.route("/")     #127.0.0.1:5000/ 로 접속(요청)했을 때 아래의 함수를 실행한다.
def index():
    ## index.html 그래프를 그리기 위해서 필요한 변수 값
    ## x_pos, y_pos, labels 리턴
    # _x = [1,2,3,4,5]
    # _y = [40,20,10,40,50]
    _labels = "라벨"
    
    # 코로나 데이터를 로드
    # 일일 확진자 파생변수
    # x축에는 등록일시
    # y축에는 일일확진자
    df = pd.read_csv("../csv/corona.csv")
    df.columns = ["인덱스", "등록일시", "사망자", "확진자", "게시글번호", "기준일", "기준시간", "수정일시", "누적의심자", "누적확진률"]
    df.sort_values("등록일시", inplace = True)
    df["일일확진자"] = df["확진자"].diff().fillna(0)
    df_2 = df.tail(50)
    
    _x = df_2["등록일시"].tolist()
    _y = df_2["일일확진자"].tolist()
    data = df_2.to_dict()
    ### [ {열1:2, 열2:4}, {열1:4, 열2:8}, ...] -> data[1]["열2"]는 8이다.
    cnt = len(df_2)
    columns = df_2.columns
    c_cnt = len(columns)    
    
    return render_template("index.html", x_pos=_x, y_pos=_y, labels=_labels,
                           cnt = cnt, data=data, c_cnt=c_cnt, columns=columns)
    

@app.route("/index2")     #127.0.0.1:5000/ 로 접속(요청)했을 때 아래의 함수를 실행한다.
def index2():
    ## index.html 그래프를 그리기 위해서 필요한 변수 값
    ## x_pos, y_pos, labels 리턴
    # _x = [1,2,3,4,5]
    # _y = [40,20,10,40,50]
    _labels = "라벨"
    
    # 코로나 데이터를 로드
    # 일일 확진자 파생변수
    # x축에는 등록일시
    # y축에는 일일확진자
    df = pd.read_csv("../csv/corona.csv")
    df.columns = ["인덱스", "등록일시", "사망자", "확진자", "게시글번호", "기준일", "기준시간", "수정일시", "누적의심자", "누적확진률"]
    df.sort_values("등록일시", inplace = True)
    df["일일확진자"] = df["확진자"].diff().fillna(0)
    df["일일사망자"] = df["사망자"].diff().fillna(0)
    
    df_2 = df.tail(50)
    
    _x = df_2["등록일시"].tolist()
    _y = df_2["일일확진자"].tolist()
    _y_index2 = df_2["일일사망자"].tolist()
    data = df_2.to_dict()
    ### [ {열1:2, 열2:4}, {열1:4, 열2:8}, ...] -> data[1]["열2"]는 8이다.
    cnt = len(df_2)
    columns = df_2.columns
    c_cnt = len(columns)    
    
    return render_template("index_copy.html", x_pos=_x, y_pos=_y, labels=_labels,
                           cnt = cnt, data=data, c_cnt=c_cnt, columns=columns,
                           y_pos_index2 = _y_index2)


app.run()