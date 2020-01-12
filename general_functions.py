import pandas as pd
import numpy as np
def basic_exploration(df):

    #df.shape('row','column')
    #print("Row:{},Cols:{}".format(df.shape[0].str),(df.shape[1]))
    #info
    print(df.info())
    #numeric columns
    print(df.describe())
    #all columns
    print(df.describe(include='object'))
    #null value
    null_df=pd.DataFrame(df.isnull().sum())
    null_df.columns=['Count']
    print(null_df[null_df['Count']>0])
    #Outlier
    def outlier(x):
        q75=np.nanpercentile(x,75)
        q25=np.nanpercentile(x,25)
        iqr=q75-q25
        up_b=q75+(1.5*iqr)
        lo_b=q25-(1.5*iqr)
        return[i for i in x if i>up_b or i<lo_b]
       
    df_n=df.select_dtypes(exclude='object')
    for i in df_n:
        f=outlier(df_n[i])
        print(f)

    


