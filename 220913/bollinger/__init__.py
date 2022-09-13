import pandas as pd
import numpy as np

class Bollinger():
    def __init__(self, df, col):
        self.df = df
        self.col = col
    
    # - 5. 이동평균선, 상단밴드, 하단밴드, trade="" 생성함수 생성
    def add_bollinger(self):
        self.df["center"] = self.df[self.col].rolling(20).mean()
        self.df["ub"] = self.df["center"] + 2 * self.df[self.col].rolling(20).std()
        self.df["lb"] = self.df["center"] - 2 * self.df[self.col].rolling(20).std()
        self.df["trade"] = ""
        return self.df
        
    # - 6. 시작시간은 인자값으로 받아와서 데이터의 개수 필터링
    def starttime(self, start_time):
        self.df = self.df.loc[start_time:]
        
        return self.df
    
    # - 7. 구매 상태를 삽입 함수 생성
    def buy_state(self):
        for i in self.df.index:
            if self.df.loc[i, self.col] > self.df.loc[i,"ub"]:
                self.df.loc[i, "trade"] = ""
        
            elif self.df.loc[i, "lb"] > self.df.loc[i,self.col]:
                    self.df.loc[i, "trade"] = "buy"
            
            elif self.df.loc[i, "ub"] >= self.df.loc[i,self.col] and \
                    self.df.loc[i, self.col] >= self.df.loc[i, "lb"]:
                
                    if self.df.shift(1).loc[i, "trade"] == "buy":
                        self.df.loc[i, "trade"] = "buy"
                    else:
                        self.df.loc[i, "trade"] = ""
                
        return self.df.value_counts("trade")

# - 8. 손익 계산 함수 생성
    def total_rtn(self):
        self.rtn = 1.0
        self.df["return"] = 1
        self.buy = 0.0
        self.sell = 0.0
        for i in self.df.index:
        # 구매하는 경우(구매한 날) (buy가 없다가 생긴날)
            if self.df.loc[i, "trade"] == "buy" and self.df.shift(1).loc[i, "trade"] == "":
                self.buy = self.df.loc[i, self.col]
                print("진입일 : ", i, "진입 가격 : ", self.buy)
        
            # 매도하는 경우
            elif self.df.loc[i, "trade"] == "" and self.df.shift(1).loc[i, "trade"] == "buy":
                self.sell = self.df.loc[i, self.col]
                self.rtn = (self.sell - self.buy) / self.buy + 1 # 손익 계산
                self.df.loc[i, "return"] = self.rtn
                print("청산일 : ", i, "진입 가격 : ", self.buy, "청산 가격 : ", self.sell, "| return : ", round(self.rtn,4))
                print("----------------------")
            
            # buy, sell 변수 초기화
            if self.df.loc[i, "trade"] == "":
                self.buy = 0.0
                self.sell = 0.0
