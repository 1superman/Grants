import pandas as pd
import os

def score(train,train1):
    path_train = '../../now/score_train.csv'
    path_test = '../../now/score_test.csv'
    if os.path.exists(path_train):
        train = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        train = pd.read_csv(path_test)
    else:
        name = ['id','academy','rank']
        train = pd.read_table(train, sep = ',', header = None, names = name)
        all_max = []
        for i in sorted(pd.unique(train.academy)):
            all_max.append(train.groupby('academy').get_group(i)['rank'].max())    
        train['max_academy_rank'] = train['academy'].apply(lambda x:all_max[x-1])
        train['all_rank'] = train['academy'].apply(lambda x:sum(all_max)/all_max[x-1]) * train['max_academy_rank'] / train['rank']
        train.to_csv(train1,index=False)
    return train
    
    
    
    

    
    