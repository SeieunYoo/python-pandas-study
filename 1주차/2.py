import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/healthexp.csv")

#연도,나라,기대수명만 가져오기
df = df[["Year", "Country" ,"Life_Expectancy"]]

#Year 가 2011보다 크거나 같은 것만 가져오기
df = df[df.Year >= 2011]

#행 :Year / 열 : Country
print(pd.pivot_table(df, index = "Year" ,columns="Country"))
