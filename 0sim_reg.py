from function.alphas_function import *
from function.db_function import *
from hypothesis.gen_regular_alpha import *
from hypothesis.gen_super_alpha import *
from function.login import *
import data_theme

universe = 'TOP3000'
region = 'USA'
GROUP = ['INDUSTRY', 'SUBINDUSTRY', 'SECTOR', 'INDUSTRY', 'SUBINDUSTRY', 'SECTOR', 'MARKET']
rank = ['rank', 'rank', 'group_rank']
inner_group = ['sector', 'industry', 'subindustry']

data_datasets = My_db('user.db').get_data_US(data_theme.datasets)
print('data_datasets = ',len(data_datasets)/10)
print(data_datasets)

while True:
    try:
        raw_alpha = rnd_reg(data_datasets, data_datasets, rank, inner_group)
        neutralization = random.choice(GROUP)
        result = Simulate(universe=universe,region=region,neutralization=neutralization).regular(raw_alpha)
        if not result:
            sys.exit('Done')
    except Exception as e:
        pass