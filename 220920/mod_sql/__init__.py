import pymysql
import pandas as pd

class Database():
    #클래스 안의 모든 함수에 적용가능한 변수. 이거는 self필요없음
    _db = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "9202",
        db = "ubion",
        port = 3306
    )
    cursor = _db.cursor(pymysql.cursors.DictCursor)

    #삽입 후 커밋
    def execute(self, sql, values=[]):
        self.cursor.execute(sql, values)
        
    def commit(self):
        self._db.commit()
    
    #삽입 후 DF반환
    def executeall(self, sql, values=[]):
        self.cursor.execute(sql, values)
        self.result = self.cursor.fetchall()
        # return pd.DataFrame(self.result) #웹에서는 df형태로 리턴하지 않는다.
        return self.result
    
    def close(self):
        self._db.close()
    