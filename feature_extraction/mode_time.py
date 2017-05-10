import pandas as pd
import os

def Sum_type(train0_card,files):
    path_train = '../../now/mode_time_train.csv'
    path_test = '../../now/mode_time_test.csv'
    if os.path.exists(path_train):
        df = pd.read_csv(path_train)
    elif os.path.exists(path_test):
        df = pd.read_csv(path_test)
    else:
        student = train0_card['id'].unique()
        G = train0_card.groupby('id')
        mode_all_mean = []
        mode_all_max = []
        mode_all_min = []
        for i in student:
            mode_mean = []
            mode_max = []
            mode_min = []
            Gi = G.get_group(i)
    #        modei = sorted(Gi['mode'].unique())
            G1 = Gi.groupby('mode')
            for j in range(12):
                mode_sumi = []
                try:
                    Gj = G1.get_group(j)
                except:
                    mode_mean.append(0)
                    mode_max.append(0)
                    mode_min.append(0)
                    continue
    #            year = sorted(Gj['year'].unique())
    #            month = sorted(Gj['month'].unique())
                G2 = Gj.groupby(['year','month'])
                n = 0
                for y in [2013,2014,2015]:
                    for m in range(1,13):
                        try:
                            Gm = G2.get_group((y,m))
                            mode_sumi.append(len(Gm))
                            n += 1
                        except:
                            mode_sumi.append(0)
                mode_mean.append(sum(mode_sumi)/n)
                mode_max.append(max(mode_sumi))
                mode_min.append(min(mode_sumi))
            mode_all_mean.append(mode_mean)
            mode_all_max.append(mode_max)
            mode_all_min.append(mode_min)
        df = pd.DataFrame()
        df['id'] = student
        df['mode_time_mean'] = mode_all_mean
        df['mode_time_max'] = mode_all_max
        df['mode_time_min'] = mode_all_min
        z_mode_max = zip(*df['mode_time_max'])
        z_mode_mean = zip(*df['mode_time_mean'])
    #    z_mode_min = zip(*train['style_min'])
        for i in range(len(z_mode_mean)):
            df['mode_time_mean'+str(i)] = z_mode_mean[i]
            df['mode_time_max'+str(i)] = z_mode_max[i]
    #        train['style_min'+str(i)] = z_mode_min[i]
        del df['mode_time_max'], df['mode_time_mean'], df['mode_time_min'] 
        df.to_csv(files,index=False)
    return df


