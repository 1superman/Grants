import pandas as pd

def oversample(tr):
    Oversampling1000 = tr.loc[tr.label == 1000]
    Oversampling1500 = tr.loc[tr.label == 1500]
    Oversampling2000 = tr.loc[tr.label == 2000]
    
    for i in range(5):
        tr = tr.append(Oversampling1000)
    for j in range(8):
        tr = tr.append(Oversampling1500)
    for k in range(10):
        tr = tr.append(Oversampling2000)
    return tr
    
def f1(preds,dtrain):
    gaps = pd.Series(dtrain.values)
    preds = pd.Series(preds)
    num = len(gaps)
    f1 = 0
    for i in [1000,1500,2000]:
        s = float(len(preds[gaps==preds][preds==i]))
        ss = list(gaps).count(i)
        if ss == 0:
            pre = 0
        else:
            pre = s/ss
        rec = s/num
        if pre+rec==0:
            f1 += 0
        else:
            f1 += 2*pre*rec/(pre+rec)/4
    return f1/3