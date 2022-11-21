import pandas as pd
import numpy as np

# 한글폰트 사용을 위해 설치
# 아래 모듈을 설치하고 불러오면 별도의 한글폰트 설정이 필요 없습니다.
# !pip install koreanize-matplotlib

df = pd.read_csv(
    "https://raw.githubusercontent.com/corazzon/boostcourse-ds-510/master/data/online_oversea_sale_202210.csv.zip", 
    encoding="cp949")

#1번
df = df.rename(columns= {"데이터" : "백만"})
Year = []
Quarter=[]

for i in df["시점"]:
        Year.append(i[0:4])
df["연도"] = Year

for i in df["시점"]:
        Quarter.append(i[5])
df["분기"] = Quarter

print(df.describe())

#2번
print(df.pivot_table(index="국가(대륙)별",columns="연도",values="백만",aggfunc = "sum"))

#3번
print(df.groupby(["상품군별","국가(대륙)별"])["백만"].sum())
