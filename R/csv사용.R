#csv 파일로드
df = read.csv("./csv/csv_exam.csv")
df

head(df)
head(df, 2)

tail(df)
tail(df, 2)

#엑셀의 형태와 마찬가지의 뷰어창에 데이터 프레임을 확인
view(df)

#데이터프레임의 크기(행,열)를 출력
dim(df)

#데이터프레임의 속성 값을 출력
str(df)

#컬럼의 데이터의 개수를 출력
table(df$class)

# 통계 요약 정보 출력
summary(df)
summary(df$math)


#----------------------------------------------


#dplyr 패키지 설치
install.packages("dplyr")
##dplyr 패키지 로드
library(dplyr)

df_raw = data.frame(var1 = c(1, 2, 1),
                    var2 = c(2, 3, 5))
df_raw

#rename(데이터프레임명, 새컬럼명=변경이될 컬럼명)
rename(df_raw, v2= var2) #출력만 하는거지 기본것 수정은x
df_raw

#파생변수 생성
df_raw$sum = df_raw$var1 + df_raw$var2
df_raw

#if문을 이용해서 파생변수
## sum의 값이 5보다 크면 pass 아니면 fail
df_raw$res = ifelse(df_raw$sum > 5, "pass", "fail")
df_raw

## 다중 if문을 사용하려면?
## sum의 값이 5보다 크면 "pass", 5이면 "hold", 작으면 "fail"
df_raw$res = ifelse(df_raw$sum >5, "pass", ifelse(df_raw$sum==5, "hold", "fail"))
df_raw


#---------------------------------------


#dplyr패키지에 있는 내장 함수들 사용
# ctrl + shift + m  = %>% 
df
## filter() : 필터링 기능
df %>% filter(class==1)
## arrange() : 정렬을 변경
df %>% arrange(math)
## desc나 음수형태로 변경하여 사용하면 내림차순 정렬
df %>% arrange(desc(math))
df %>% arrange(-math)

## 정렬의 기준을 여러개
df %>% arrange(class, math)
## 클래스를 기준으로 오름차수느 수학 성적 기준으로 내림차순
df %>% arrange(class, -math)


# 특정 컬럼만 선택하여 출력
df %>% select(class)
df %>% select(class, math, english)
## 특정 컬럼만 삭제하여 출력
df %>% select(-class)
# 컬럼의 범위 지정
df %>% select(class : english)

# 새로운 컬럼을 추가하는 함수
df %>% mutate(total = math+english+science,
              mean = total/3)


# group_by(), summarise() 그룹화
df %>% group_by(class) %>%  summarise(mean_math = mean(math),
                                      mean_english = mean(english))

# df 데이터프레임에서 class를 기준으로 내림차순 정렬 ->
## class, english 컬럼만 출력
order(df, class)
df %>%  select(
  
# join함수를 사용
df_1 = data.frame(id = 1:5, score = c(80,70,80,90,95))
df_2 = data.frame(id = 1:5, weight = c(80,70,75,90,95))
df_3 = data.frame(id = 1:3, class = c(1,1,2))

## inner_join() -> 교집합
inner_join(df_1, df_2, by="id")
inner_join(df_1, df_3, by="id")

## right_join()
right_join(df_1, df_2, by="id")
right_join(df_1, df_3, by="id")

#bind_rows() 데이터프레임에 행을 추가하는 함수
## 데이터프레임에 유니언 결합

