import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()

sep = ','
target = 'medv'
datapath = ''
#filename = '../Boston.csv'
filename = '../Boston.json'
#df = pd.read_csv(datapath+filename,sep=sep,index_col=None)
df = pd.read_json(filename)
df = df.sample(frac=1.0,random_state=42)
print(df.shape)
df.head(1)

dft = AV.AutoViz(datapath+filename, sep=sep, depVar=target, dfte=df, header=0, verbose=2,
                            lowess=False,chart_format='svg',max_rows_analyzed=1500,max_cols_analyzed=30)