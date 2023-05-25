import sys
import pandas as pd
import ast
from function.alphas_function import *
from function.db_function import *

from config import *
import json
from datetime import datetime
from datetime import timedelta

k = 0
max_submit = 6
hidden = 'no'
submit_fitness = '1'
submit_prod_corr = 0.7
submit_self_corr = 0.7

# Lấy thời điểm cách 4 tuần kể tư hôm nay
last_update = datetime.now() - timedelta(weeks = 4)
date_start = last_update.strftime('%Y-%m-%d')
last_update = last_update.strftime('%Y-%m-%dT00:00:00-00:00')
page = 0

df=pd.read_csv('done_alpha.csv',converters={'is':ast.literal_eval,'regular':ast.literal_eval}).drop_duplicates('id',keep='first')

raw1 = df[(df['dateCreated']>last_update)&(df['fail']!=0)&(df['raw']==1)].sort_values(['sharpe','them'],ascending=False)['id'].to_list()
raw2 = df[(df['dateCreated']>last_update)&(df['fail']!=0)&(df['raw']==2)].sort_values(['sharpe','them'],ascending=False)['id'].to_list()
raw3 = df[(df['dateCreated']>last_update)&(df['fail']!=0)&(df['raw']==3)].sort_values(['sharpe','them'],ascending=False)['id'].to_list()
rawo = df[(df['dateCreated']>last_update)&(df['fail']!=0)&(df['raw']>=4)].sort_values(['sharpe','them'],ascending=False)['id'].to_list()

while k<=max_submit:
    try:
        for i in raw1:     
        # Neu la raw alpha
            print('Code Raw: ', df[df['id']==i]['code'].values[0])
            print('Sharpe: ', df[df['id']==i]['sharpe'].values[0])
            print('Fitness:', df[df['id']==i]['fitness'].values[0])
            prod_corr = abs(Infor().get_prod_corr(i))
            self_corr = abs(Infor().get_self_corr(i))
            print(f'Prod correlation: {prod_corr}')
            print(f'Self correlation: {self_corr}')
            if (prod_corr<=submit_prod_corr)&(self_corr<=submit_self_corr):
                k = Infor().submit(i, k)
                print('done')
                if k >= max_submit:
                    sys.exit("Done")
            else:
                pass
            Infor().hidden_alpha(i)
            df[df['id']!=i].to_csv('done_alpha.csv',index=False)
        for i in raw2:     
        # Neu la raw alpha
            print('Code Raw: ', df[df['id']==i]['code'].values[0])
            print('Sharpe: ', df[df['id']==i]['sharpe'].values[0])
            print('Fitness:', df[df['id']==i]['fitness'].values[0])
            print(f'Prod correlation: {Infor().get_prod_corr(i)}')
            print(f'Self correlation: {Infor().get_self_corr(i)}')
            prod_corr = abs(Infor().get_prod_corr(i))
            self_corr = abs(Infor().get_self_corr(i))
            print(f'Prod correlation: {prod_corr}')
            print(f'Self correlation: {self_corr}')
            if (prod_corr<=submit_prod_corr)&(self_corr<=submit_self_corr):
                k = Infor().submit(i, k)
                if k >= max_submit:
                    sys.exit("Done")
            else:
                pass
            Infor().hidden_alpha(i)
            df[df['id']!=i].to_csv('done_alpha.csv',index=False)

        for i in raw3:     
        # Neu la raw alpha
            print('Code Raw: ', df[df['id']==i]['code'].values[0])
            print('Sharpe: ', df[df['id']==i]['sharpe'].values[0])
            print('Fitness:', df[df['id']==i]['fitness'].values[0])
            print(f'Prod correlation: {Infor().get_prod_corr(i)}')
            print(f'Self correlation: {Infor().get_self_corr(i)}')
            prod_corr = abs(Infor().get_prod_corr(i))
            self_corr = abs(Infor().get_self_corr(i))
            print(f'Prod correlation: {prod_corr}')
            print(f'Self correlation: {self_corr}')
            if (prod_corr<=submit_prod_corr)&(self_corr<=submit_self_corr):
                k = Infor().submit(i, k)
                if k >= max_submit:
                    sys.exit("Done")
            else:
                pass
            Infor().hidden_alpha(i)
            df[df['id']!=i].to_csv('done_alpha.csv',index=False)

        for i in rawo:     
        # Neu la raw alpha
            print('Code Raw: ', df[df['id']==i]['code'].values[0])
            print('Sharpe: ', df[df['id']==i]['sharpe'].values[0])
            print('Fitness:', df[df['id']==i]['fitness'].values[0])
            print(f'Prod correlation: {Infor().get_prod_corr(i)}')
            print(f'Self correlation: {Infor().get_self_corr(i)}')
            prod_corr = abs(Infor().get_prod_corr(i))
            self_corr = abs(Infor().get_self_corr(i))
            print(f'Prod correlation: {prod_corr}')
            print(f'Self correlation: {self_corr}')
            if (prod_corr<=submit_prod_corr)&(self_corr<=submit_self_corr):
                k = Infor().submit(i, k)
                if k >= max_submit:
                    sys.exit("Done")
            else:
                pass
            Infor().hidden_alpha(i)
            df[df['id']!=i].to_csv('done_alpha.csv',index=False)

    except Exception:
        pass