import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/corazzon/boostcourse-ds-510/master/data/medical_201909.csv.zip", low_memory=False)

#데이터 가져오기
df = df[["시도명","상권업종중분류명","상권업종소분류명","시군구명"]] #여기까지는 미션1번과 똑같음

#서울특별시에 위치한 병원만 인덱싱
df_all_seoul = df[(df.상권업종중분류명 == "병원") & (df["시도명"] == "서울특별시")]

#서울특별시에 위치한 피부나 성형이 들어간 병원
df_seoul_hospital = df_all_seoul[(df_all_seoul["상권업종소분류명"].str.contains("피부|성형"))]

#참고로 리스트끼리는 연산이 안됨(데이터프레임이나 시리즈 형태만 가능), value_counts()를 통해서 시군구명 마다의 빈도수를 구해줌
hospital = df_seoul_hospital["시군구명"].value_counts()
all = df_all_seoul["시군구명"].value_counts()

print((hospital/all).round(2).sort_values(ascending=False))