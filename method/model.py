import numpy as np
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

def learn(x, y, test_x, random_state, classifier):
    # set sample weight
    x.index = range(len(x))
    y.index = range(len(y))
    if classifier == 'GDBT':
        weight_list = []
        for j in range(len(y)):
            if y[j] == 0:
                weight_list.append(0.7)
            if y[j] == 1000:
                weight_list.append(5.9)
            if y[j] == 1500:
                weight_list.append(8)
            if y[j] == 2000:
                weight_list.append(10)    
        clf = GradientBoostingClassifier(loss='deviance', n_estimators=44,
#                                         verbose=2017,
                                         learning_rate=0.1,
                                         max_depth=7, random_state=random_state,
                                         min_samples_split=200,
                                         min_samples_leaf=250,
                                         subsample=1.0,
                                         max_features='sqrt').fit(x, y, weight_list)
                                            
    if classifier == 'XGB':
        weight_list = []
        for j in range(len(y)):
            if y[j] == 0:
                weight_list.append(1)
            if y[j] == 1000:
                weight_list.append(13)
            if y[j] == 1500:
                weight_list.append(20)
            if y[j] == 2000:
                weight_list.append(26)
    
        clf = XGBClassifier(objective="multi:softmax", max_depth=3,
                                    learning_rate=0.1, n_estimators=30,
                                    colsample_bytree=0.09, subsample=1,
                                    min_child_weight=1, gamma=0.1,
                                    seed=random_state, reg_alpha=0,
                                    reg_lambda=1).fit(np.asarray(x), np.asarray(y),np.asarray(weight_list))
  
    if classifier == 'RF':   
        x.astype('int')
        y.astype('int')
        weight_0_rf = 4.40 
        weight_1000_rf = 59 
        weight_1500_rf = 111 
        weight_2000_rf = 130                                                         
        cw_rf = {0: weight_0_rf, 1000: weight_1000_rf, 1500: weight_1500_rf, 2000: weight_2000_rf}

        clf = RandomForestClassifier(n_jobs=-1,
                                 n_estimators=750,
                                 max_depth=50, random_state=random_state,
                                 min_samples_split=50,
                                 min_samples_leaf=20,
                                 max_features='sqrt',
                                 max_leaf_nodes=None,
                                 criterion='gini',
#                                 min_impurity_split=1e-7,
                                 class_weight=cw_rf).fit(x, y)
                                 
    prediction_list = clf.predict(test_x)
    prediction_proba_list = clf.predict_proba(test_x)
    return prediction_list, prediction_proba_list