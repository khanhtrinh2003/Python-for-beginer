# My modules
from function.alphas_function import *
from function.db_function import *

from hypothesis.gen_super_alpha import *

from config import *

universe = 'TOP3000'
region = 'USA'

GROUP = ['INDUSTRY', 'SUBINDUSTRY', 'SECTOR', 'INDUSTRY', 'SUBINDUSTRY', 'SECTOR', 'MARKET']
neutralization = "INDUSTRY"
# combos = ["1"]
offset = '0'
done = False

while not done:
    try:
        # Lấy data lần đầu
        offset = '0'
        data = Infor().get_data_os(offset, region)
        print(data['count'])
        page = int(data['count']/10)
        data = data['results']

        # Lấy data những trang sau
        for i in range(page):
            offset = str(10*(i+1))
            get_i = False
            while not get_i:
                try:
                    data_i = Infor().get_data_os(offset, region)['results']
                    data += data_i
                    get_i = True
                except Exception as e:
                    print(e)
                    print('Wait i')
                    pass

        done = True
    
    # Hiển thị tên lỗi
    except Exception as e:
        print(e)
        print('Wait')
        pass
print('Done')

df = pd.DataFrame(data)
df['sharpe']=df.apply(get_sharpe,axis=1)

new_data=df[(df['dateCreated']>='2022-01-01T00:00:00-00:00')&(df['sharpe']>=1.58)]['id'].to_list()

unamed = df[df['name'].isna()]['id']
for item in unamed:
    Infor().save_name(item)
    print(item)

print(len(new_data))

decays = [0,0,0,0,4,5,10]
while True:
    try:
        # Alpha
        selectionLimit = random.randint(10,15)
        selection, combo = rnd_super(new_data,selectionLimit)
        neutralization = random.choice(GROUP)
        n_decay = random.choice(decays)

        result = Simulate(universe, region, neutralization, n_decay).super(combo, selection, selectionLimit)
        print(result)
        
        if not result:
            sys.exit('Done')
    except Exception as e:
        print(e)
        pass