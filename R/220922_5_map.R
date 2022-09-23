# 지도 시각화
# 패키지설치
install.packages('ggiraphExtra')
library(ggiraphExtra)
library(dplyr)
library(ggplot2)
library(tibble)

# 미국 주 별 강력범죄율
View(USArrests)

# tibble 패키지에 있는 rownames_to_column 이용해
# 인덱스의 값은 컬럼으로 이름을 부여
crime = rownames_to_column(USArrests, var='state')
head(crime, 1)

# 소문자로 변경
crime$state = tolower(crime$state)
head(crime)

# map 데이터를 가지고 오기 위해서 패키지
install.packages('maps')
library(maps)

# 미국 맵 데이터를 변수에 지정
states_map = map_data('state')
head(states_map)

ggChoropleth(
  data = crime,           # 지도에 표현할 데이터
  aes(fill = Murder,      # 지도에 채울 데이터의 수치
      map_id = state),    # 지역의 기준 변수
  map = states_map,       # 지도 데이터
  interactive = T         # 이걸 추가하면 여기가 어딘지, 수치가 얼만지 나옴
  # 인터렉티브 여부
)


#------------------------------------------------

install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")
library(kormaps2014)
## korpop1 : 시도별 인구 데이터
## kormap1 : 시도별 지도 데이터

str(korpop1)
View(korpop1)
str(kormap1)

korpop1 = rename(korpop1,
                 pop = 총인구_명,
                 name = 행정구역별_읍면동)

ggChoropleth(
  data = korpop1,
  aes(fill = pop,
      map_id = code,
      tooltip = name),
  map = kormap1,
  interactive = T)
