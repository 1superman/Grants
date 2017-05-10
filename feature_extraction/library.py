import pandas as pd
from dateutil.parser import parse
import os

def library(files,files1):
    path_train = '../../now/library_train.csv'
    path_test = '../../now/library_test.csv'
    if os.path.exists(path_train):
        zz = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        zz = pd.read_csv(path_test)
    else:
        df = pd.read_table(files,header=0,sep=',',names=['id','gate','time'])
        df['date'] = df['time'].str.split(' ').str[0]    #天数
        df['hour'] = df['time'].str.split(' ').str[1].str[:2].astype('int')  #不同时间段
        df['weekday'] = df['date'].apply(lambda x:parse(x).isoweekday())
        user = pd.unique(df['id'])
        hour_div = range(df['hour'].min(),df['hour'].max()+1)
        eve = []
        sum_time = []
        sum_days = []
        weekend_time = []
        all_dif_hour = []
        G = df.groupby('id')
        for i in user:
            G_user = G.get_group(i)
            date = len(pd.unique(G_user['date']))
            dif_hour = []
            for j in hour_div:
                try:
                    dif_hour.append(float(len(G_user[G_user['hour']==j]))/date)
                except:
                    dif_hour.append(0)
            all_dif_hour.append(dif_hour)                       ##不同时段进出次数
            
            eve.append(float(len(G_user[G_user['hour']>5]))/date)                     ##晚上进出总次数
            sum_time.append(float(len(G_user))/date)                             ##进出总次数
            weekend_time.append(float(len(G_user[G_user['weekday']>5]))/date)         ##周末进出总次数
            sum_days.append(float(len(pd.unique(G_user['date'])))/date)
        
        zz = pd.DataFrame()
        zz_hour = zip(*all_dif_hour)
        for i in range(len(hour_div)):
            zz['lib_hour'+str(i)] = zz_hour[i]
        
        zz['id'] = user    
        zz['lib_eve'] = eve
        zz['lib_sum_time'] = sum_time
        zz['lib_sum_days'] = sum_days
        zz['lib_weekend_time'] = weekend_time
        zz.to_csv(files1,index=False)
    return zz
    
     
        
    
