import pandas as pd
import numpy as np
from collections import Counter
import os

def transform(label):
    dic = {}
    for i in range(len(label)):
        dic[label[i]] = i
    return dic

def card(files,files1):
    path_train = '../../now/card_train.csv'
    path_test = '../../now/card_test.csv'
    if os.path.exists(path_train):
        zz = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        zz = pd.read_csv(path_test)
    else:        
        df = pd.read_table(files,sep=',',header=None,encoding='utf-8')
        df.columns = ['id','style','where','mode','time','money','sum']
        del df['style']
        df['date'] = df['time'].str.split(' ').str[0]
        df['hour'] = df['time'].str.split(' ').str[1].str[:2].astype('int') 
        #mode_money = []
        all_popular_place_10 = []
        all_most_sum_30 = []
        all_most_single = []
        user_hour_sum = []
        user_hour_max = []
        user_hour_mean = []
        user_hour_min = []
        user_hour_median = []
        user_hour_var = []
        user_mode_sum = []
        user_mode_max = []
        user_mode_mean = []
        user_mode_min = []
        user_mode_median = []
        user_mode_var = []
        user = pd.unique(df['id'])
        where = pd.unique(df['where'])
        mode = pd.unique(df['mode'])
        df['where'] = df['where'].map(transform(where))
        df['mode'] = df['mode'].map(transform(mode))
        G = df.groupby('id')
        for i in user:
            G_user = G.get_group(i)
            date = len(pd.unique(G_user['date']))
        #    mode_money.append(G_user['sum'].sum()/date)
            zz = Counter(G_user['where'])
            tt = zip(*sorted(zz.items(),key=lambda x:x[1],reverse=True)[:10])[0]
            all_popular_place_10 .append(tt)                    ##用户去过最多前十大地点
            G_sum1 = G_user.groupby('where').sum()
            G_sum1.sort_values('sum',ascending=0,inplace=1)
            all_most_sum_30.append(list(G_sum1.index)[:30])         ##用户花钱最多的30大地点
            G_sum2 = G_user.groupby('where').max()
            G_sum2.sort_values('sum',ascending=0,inplace=1)
            all_most_single.append(list(G_sum2.index)[:10])        ##用户单价最高的10大地点
            G_hour = G_user.groupby('hour')              ##用户24小时时间段花费
            each_user_hour_sum = []
            each_user_hour_max = []
            each_user_hour_mean = []
            each_user_hour_min = []
            each_user_hour_mid = []
            each_user_hour_var = []
            for j in range(6,23):
                try:
                    each_user_hour_sum.append(G_hour.get_group(j)['sum'].sum()/date)
                    each_user_hour_max.append(G_hour.get_group(j)['sum'].max()/date)
                    each_user_hour_mean.append(G_hour.get_group(j)['sum'].mean()/date)
                    each_user_hour_min.append(G_hour.get_group(j)['sum'].min()/date)
                    each_user_hour_mid.append(G_hour.get_group(j)['sum'].median()/date)
                    each_user_hour_var.append(G_hour.get_group(j)['sum'].var()/date)
                except:
                    each_user_hour_sum.append(0)
                    each_user_hour_max.append(0)
                    each_user_hour_mean.append(0)
                    each_user_hour_min.append(0)
                    each_user_hour_mid.append(0)
                    each_user_hour_var.append(0)
            
            user_hour_sum.append(each_user_hour_sum)        
            user_hour_max.append(each_user_hour_max)
            user_hour_mean.append(each_user_hour_mean)
            user_hour_min.append(each_user_hour_min)
            user_hour_median.append(each_user_hour_mid)
            user_hour_var.append(each_user_hour_var)
            
            G_mode = G_user.groupby('mode')
            each_user_mode_sum = []
            each_user_mode_max = []
            each_user_mode_mean = []
            each_user_mode_min = []
            each_user_mode_mid = []
            each_user_mode_var = []
            for k in mode:
                try:
                    each_user_mode_sum.append(G_mode.get_group(k)['sum'].sum()/date)
                    each_user_mode_max.append(G_mode.get_group(k)['sum'].max()/date)
                    each_user_mode_mean.append(G_mode.get_group(k)['sum'].mean()/date)
                    each_user_mode_min.append(G_mode.get_group(k)['sum'].min()/date)
                    each_user_mode_mid.append(G_mode.get_group(k)['sum'].median()/date)
                    each_user_mode_var.append(G_mode.get_group(k)['sum'].var()/date)
                except:
                    each_user_mode_sum.append(0)
                    each_user_mode_max.append(0)
                    each_user_mode_mean.append(0)
                    each_user_mode_min.append(0)
                    each_user_mode_mid.append(0)
                    each_user_mode_var.append(0)
            
            user_mode_sum.append(each_user_mode_sum)        
            user_mode_max.append(each_user_mode_max)
            user_mode_mean.append(each_user_mode_mean)
            user_mode_min.append(each_user_mode_min)
            user_mode_median.append(each_user_mode_mid)
            user_mode_var.append(each_user_mode_var)
                                
        zz = pd.DataFrame()     
        zz['id'] = user  
        #zz['mode_money'] = mode_money   
        zz_user_hour_sum = zip(*user_hour_sum)
        zz_user_hour_max = zip(*user_hour_max)
        zz_user_hour_mean = zip(*user_hour_mean)
        zz_user_hour_min = zip(*user_hour_min)
        zz_user_hour_median = zip(*user_hour_median)
        zz_user_hour_var = zip(*user_hour_var)
        zz_user_mode_sum = zip(*user_mode_sum)
        zz_user_mode_max = zip(*user_mode_max)
        zz_user_mode_mean = zip(*user_mode_mean)
        zz_user_mode_min = zip(*user_mode_min)
        zz_user_mode_median = zip(*user_mode_median)
        zz_user_mode_var = zip(*user_mode_var)
        for i in range(17):
            zz['user_hour_sum'+str(i)] = zz_user_hour_sum[i]
            zz['user_hour_max'+str(i)] = zz_user_hour_max[i]
            zz['user_hour_mean'+str(i)] = zz_user_hour_mean[i]
            zz['user_hour_min'+str(i)] = zz_user_hour_min[i]
            zz['user_hour_median'+str(i)] = zz_user_hour_median[i]
            zz['user_hour_var'+str(i)] = zz_user_hour_var[i]
        for i in range(12):
            zz['user_mode_sum'+str(i)] = zz_user_mode_sum[i]
            zz['user_mode_max'+str(i)] = zz_user_mode_max[i]
            zz['user_mode_mean'+str(i)] = zz_user_mode_mean[i]
            zz['user_mode_min'+str(i)] = zz_user_mode_min[i]
            zz['user_mode_median'+str(i)] = zz_user_mode_median[i]
            zz['user_mode_var'+str(i)] = zz_user_mode_var[i]
            
        zz['hour_money'] = zz[zz.columns[zz.columns.str.contains('sum')]].sum(axis=1)
        for i in zz.columns[zz.columns.str.contains('sum')] :
            zz['rate'+i] = zz[i]/zz['hour_money']
        
        zz['popular_place'] = zz['popular_place'].apply(lambda x:list(eval(x)))
        zz['most_single'] = zz['most_single'].apply(lambda x:eval(x))
        zz['most_sum'] = zz['most_sum'].apply(lambda x:eval(x))
        for i in range(len(zz['popular_place'])):
            if len(zz['popular_place'][i]) != 10:
                zz['popular_place'][i] = zz['popular_place'][i]+np.zeros(10-len(zz['popular_place'][i])).tolist()
            if len(df['most_single'][i]) != 10:
                zz['most_single'][i] = zz['most_single'][i]+np.zeros(10-len(zz['most_single'][i])).tolist()
            if len(df['most_sum'][i]) != 30:
                zz['most_sum'][i] = zz['most_sum'][i]+np.zeros(30-len(zz['most_sum'][i])).tolist()
        
        zz_popular = zip(*list(zz['popular_place']))
        for i in range(len(zz_popular)):
            zz['popular_place'+str(i)] = zz_popular[i]
        
        zz_most_sum = zip(*list(zz['most_sum']))
        for i in range(len(zz_most_sum)):
            zz['most_sum'+str(i)] = zz_most_sum[i]
            
        zz_most_single = zip(*list(zz['most_single']))
        for i in range(len(zz_most_single)):
            zz['most_single'+str(i)] = zz_most_single[i]      
        
        del zz['popular_place']
        del zz['most_single']
        del zz['most_sum']    
        zz.to_csv(files1,index=False)
    return zz   
    

