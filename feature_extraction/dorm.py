import pandas as pd
import os

def dorm(train,train1):
    path_train = '../../now/dorm_train.csv'
    path_test = '../../now/dorm_test.csv'
    if os.path.exists(path_train):
        dorm_new = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        dorm_new = pd.read_csv(path_test)
    else:
        dorm = pd.read_table(train,header=0,sep=',',names=['id','time','gate'])
        dorm['date'] = dorm['time'].str.split(' ').str[0]
        dorm['hour'] = dorm['time'].str.split(' ').str[1].str[:2].astype('int') 
        _id = pd.unique(dorm['id'])
        group_id = dorm.groupby('id')
        tt = []
        for i in _id:
            group_idi = group_id.get_group(i)
            date = len(pd.unique(group_idi['date']))
            group_idi.index = range(len(group_idi))
            zz = []
            for j in range(0,24):
                c = float(list(group_idi['hour']).count(j))
                zz.append(c/date)
            tt.append(zz)   
        zip_tt = zip(*tt)
        dorm_new = pd.DataFrame()
        dorm_new['id'] = _id
        for i in range(24):
            dorm_new['hour_'+str(i)] = zip_tt[i]  
        dorm_new.to_csv(train1,index=False)
    return dorm_new

