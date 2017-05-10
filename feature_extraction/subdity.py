import pandas as pd
import os

def Read_subdity(train,train1):
    path_train = '../../now/student_train.csv'
    path_test = '../../now/student_test.csv'
    if os.path.exists(path_train):
        train = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        train = pd.read_csv(path_test)
    else:
        name = ['id','label']
        train = pd.read_table(train, sep = ',', header = None, names = name)
        train.to_csv(train1, index=False)
    return train
    



