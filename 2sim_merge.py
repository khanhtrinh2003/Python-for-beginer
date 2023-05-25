import sys
import random
import json
import ast
from function.alphas_function import *
from function.db_function import *
from hypothesis.gen_merge_alpha import *

from config import *


region = 'USA'
universe = 'TOP3000'
GROUP = ['INDUSTRY', 'SUBINDUSTRY', 'SECTOR', 'INDUSTRY', 'SUBINDUSTRY', 'SECTOR', 'MARKET']
neutralization = random.choice(GROUP)

sub_corr_all_list = ['0.4', '0.4', '0.5', '0.5', '0.5', '0.6', '0.6', '0.7']
sub_corr_all = 0.6

sub_corr_self_list = ['0.4', '0.4', '0.5']
sub_corr_self = 0.4

sub_shapre = 1
print(sub_shapre)
print('neutralization', neutralization)

df=pd.read_csv('updated_alpha.csv',converters={'is':ast.literal_eval,'regular':ast.literal_eval,'settings':ast.literal_eval})

df['code']=df.apply(get_code,axis=1)
df['raw']=df.apply(get_raw,axis=1)
df['sharpe']=df.apply(get_sharpe,axis=1)
df['neutralization']=df.apply(get_neutralization,axis=1)

lines = df[(df['sharpe']>=sub_shapre) & (df['neutralization']==neutralization)]['code'].to_list()

while True:
    try:
        # Nếu số alphas để merge <11 thì tạo lại list
        neutralization = random.choice(GROUP)
        sub_corr_all = random.choice(sub_corr_all_list)
        sub_corr_self = random.choice(sub_corr_self_list)

        # Simulate alphas
        raw_alpha, n_decay = rnd_merge(lines)
        result = Simulate(universe=universe, region=region, neutralization = neutralization, decay = n_decay).regular(raw_alpha)

        if not result:
            sys.exit('Done')
    except Exception as e:
        pass