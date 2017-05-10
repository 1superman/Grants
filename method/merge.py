import pandas as pd
import os

def merge(files):
    df1 = pd.read_csv('../now/card_'+files+'.csv')
    df2 = pd.read_csv('../now/borrow_'+files+'.csv')
    df3 = pd.read_csv('../now/library_'+files+'.csv')
    df4 = pd.read_csv('../now/dorm_'+files+'.csv')
    df5 = pd.read_csv('../now/score_'+files+'.csv')
    df6 = pd.read_csv('../now/student_'+files+'.csv')  
    df = pd.merge(df6,df1,on='id',how='left')
    df = pd.merge(df,df2,on='id',how='left')
    df = pd.merge(df,df3,on='id',how='left')
    df = pd.merge(df,df4,on='id',how='left')
    df = pd.merge(df,df5,on='id',how='left')
    df = df.fillna(0)
    return df
    
def rate(files):
    path_train = '../../now/final_train.csv'
    path_test = '../../now/final_test.csv'
    if os.path.exists(path_train):
        df = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        df = pd.read_csv(path_test)
    else:
        df = merge(files)
        for i in df.columns[57:]:
            df['rate_'+i] = df[i]/df[i].sum()
        df.to_csv('../now/final_'+files+'.csv',index=False)
    return df

