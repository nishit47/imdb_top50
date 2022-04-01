import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv("imdb.csv")

profile=ProfileReport(df)
profile.to_file(output_file="Report.html")