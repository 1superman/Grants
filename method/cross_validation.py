import pandas as pd
from function import f1
from sklearn.cross_validation import train_test_split
from model import learn
import numpy as np

def get_score(data):
    target = 'label'
    feature = [x for x in data.columns if x not in [target,'id']]    
    score_list = []
    for i in range(5):
        x_train, x_test, y_train, y_test = train_test_split(data[feature],data[target],test_size=0.4,random_state=1)  
        pred_proba_gdt = 0
        pred_proba_xgb = 0
        pred_proba_rf = 0
#        ff = []     
        for i in range(5):
            pred_proba_gdt += learn(x_train, y_train, x_test, i, 'GDBT')[1]
            pred_proba_xgb += learn(x_train, y_train, x_test, i, 'XGB')[1]
            pred_proba_rf += learn(x_train, y_train, x_test, i, 'RF')
            
        pred_proba = pred_proba_gdt+pred_proba_rf*1.5+pred_proba_xgb*2.0    
        pred_max = np.max(pred_proba,axis=1)
        zipa = zip(*pred_proba)
        zz = pd.DataFrame()
        zz['max'] = pred_max
        zz['p0'] = (zipa[0]/zz['max']).astype('int')*0
        zz['p1000'] = (zipa[1]/zz['max']).astype('int')*1000
        zz['p1500'] = (zipa[2]/zz['max']).astype('int')*1500
        zz['p2000'] = (zipa[3]/zz['max']).astype('int')*2000
        zz['label'] = zz['p0']+zz['p1000']+zz['p1500']+zz['p2000']
        pred = zz['label'].values
        score = f1(pred,y_test)
        print 'final_score : '+str(i), score
        score_list.append(score)
    return score_list
        