
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/corazzon/boostcourse-ds-510/master/data/NHIS_OPEN_GJ_2017.CSV.zip",encoding="cp949")

age_code = {1: '0~4세',
 2: '5~9세',
 3: '10~14세',
 4: '15~19세',
 5: '20~24세',
 6: '25~29세',
 7: '30~34세',
 8: '35~39세',
 9: '40~44세',
 10: '45~49세',
 11: '50~54세',
 12: '55~59세',
 13: '60~64세',
 14: '65~69세',
 15: '70~74세',
 16: '75~79세',
 17: '80~84세',
 18: '85세+'}

#1번
print(pd.pivot_table(df, index=["연령대코드(5세단위)"], values="허리둘레", aggfunc="describe").rename(index=age_code))

#2번
columns = ["음주여부", "흡연상태", "연령대코드(5세단위)", "성별코드"]
df_small = df[columns]
df_corr = df_small.corr()

#3번
pd.crosstab(df["음주여부"],df['흡연상태'])
smoking = {1 : "흡연안함", 2: "끊음", 3: "흡연중"}
drinking = {0: "안마심", 1: "마심"}

df["흡연"]=df["흡연상태"].replace(smoking)
df["음주"]=df["음주여부"].replace(drinking)

#5번
left = (df["시력(좌)"] != 9.9)
right = (df["시력(우)"] != 9.9)

print(df[left&right])