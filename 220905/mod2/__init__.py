import pandas as pd

class Class_df():
    def __init__(self, _path):
        self.df = pd.read_csv(_path)

    def change(self, _column):
        #공백제거,대문자화
        self.df[_column] = self.df[_column].str.replace(" ", "")
        self.df[_column] = self.df[_column].str.upper()
        return self.df

    def review(self):   
        #왠진 모르지만 클래스에서 얻는 df는 이름만으로는 출력이 안되기에 return해주는 함수 만듬
        return self.df
    
    def type_datetime(self, _column):
        self.df[_column] = pd.to_datetime(self.df[_column])
        return self.df
    
    def add_timecolumns(self, _column):
        self.df["year"] = pd.to_datetime(self.df[_column]).dt.strftime("%Y")
        self.df["month"] = pd.to_datetime(self.df[_column]).dt.strftime("%m")
        self.df["day"] = pd.to_datetime(self.df[_column]).dt.strftime("%d")
        return self.df
