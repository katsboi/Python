import pandas as pd
import plotly.express as px

df=pd.read_csv('data.csv')
fig=px.sunburst(df, path=["Country","2003"], values='Population')
fig.show()