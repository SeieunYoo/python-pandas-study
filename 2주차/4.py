import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/corazzon/boostcourse-ds-510/master/data/medical_201909.csv.zip", low_memory=False)

#시도명,상권업종소분류명 만 데이터 가져오기
df = df[["시도명","상권업종소분류명"]] #여기까지는 미션1번과 똑같음

#상권업종소분류명이 동물병원인 것만 가져오기
df = df[df.상권업종소분류명 == "노인/치매병원"]

#각 시도명 별로 약국 개수를 구해야하므로 value_counts 활용
print(df)



