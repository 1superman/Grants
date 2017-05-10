import pandas as pd
import numpy as np
import os

## 是否借书、借书数量
def borrow(files,files1):
    path_train = '../../now/borrow_train.csv'
    path_test = '../../now/borrow_test.csv'
    if os.path.exists(path_train):
        tt = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        tt = pd.read_csv(path_test)
    else:
        df = pd.read_table(files,sep=',',header=None,names=['id','time','book','number'])
        set_user = pd.unique(df['id'])
        zz = []
        G = df.groupby('id')
        for i in set_user:
            zz.append(len(G.get_group(i)))
        tt = pd.DataFrame()
        tt['id'] = set_user
        tt['if_borrow'] = np.ones(len(tt))
        tt['sum_borrow'] = zz
        tt.to_csv(files1,index=False)
    return tt



