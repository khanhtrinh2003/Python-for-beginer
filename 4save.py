from function.db_function import *
from function.alphas_function import *
import ast
import requests
import datetime
from time import sleep
from config import *
import data_theme
import json

dataset = save_dataset 
sharpe = save_sharpe
fitness = save_fitness

region = 'USA'
universe = 'TOP3000'
sub_neutralization = "INDUSTRY"

user = My_db('user.db')
email=user.read_database_tabe('user')['email'].values[0]
print(email)

data_datasets = user.get_data_CHN(data_theme.datasets, 50)
print('data_datasets = ',len(data_datasets)/10)
print(data_datasets)

def func_save(df,prefix):
    if prefix == '-':
        change = -1
        data=pd.DataFrame(df)
        data['neutralization'] = data.apply(get_neutralization,axis=1)
        data['alpha_code'] = data.apply(get_code,axis=1)
        def new_code(x):
            y=x['alpha_code']
            return f'{prefix}{y}'
        data['code']=data.apply(new_code,axis=1)        
        save(data[['id','code','neutralization']],'unupdated_alpha.csv')
    else:
        data=pd.DataFrame(df)
        save(data,'updated_alpha.csv') 

def retrieve_and_process_data(prefix,universe,date_start,sharpe,fitness):

    done = False
    while not done:
        try:
            offset = '0'
            # Lấy danh sách 10 alpha, neu prefix âm thì nghĩa là alpha performance thấp nhất => đổi dấu thành tốt
            data = Infor().get_data_is(prefix, offset, universe, date_start, sharpe, fitness)
            page = int(data['count']/10)
            data_i = data['results']
            func_save(df=data_i,prefix=prefix)
            # Lấy các danh sách tiếp theo
            for i in range(page):
                offset = str(10*(i+1))
                get_i = False
                while not get_i:
                    try:
                        data_i = Infor().get_data_is(prefix, offset, universe, date_start, sharpe, fitness)['results']
                        print(data_i)
                        func_save(df=data_i,prefix=prefix)
                        get_i = True
                    except Exception as e:
                        print(e)
                        print('Wait i')
            
            done = True
        except Exception as e:
            print(e)
            print('Wait')

while True:
    try: 
        df= pd.read_csv('updated_alpha.csv')
        df['dateCreated']=pd.to_datetime(df['dateCreated'])
        date_start =df.sort_values('dateCreated',ascending=False)['dateCreated'].to_list()[0].strftime('%Y-%m-%d')
    except:
        date_start = (datetime.datetime.utcnow()-datetime.timedelta(hours = 48)).strftime('%Y-%m-%d')
    # Lấy thời điểm 2 ngày trước đó
    
    print(date_start)
    
    print('Save')
    

    # Prefix âm để lấy ra những alpha tệ nhất rồi đổi dấu là xong
    prefix = '-'
    retrieve_and_process_data(prefix,universe,date_start,sharpe,fitness)
    
    # Lấy ra alpha tốt raw
    prefix =''
    retrieve_and_process_data(prefix,universe,date_start,sharpe,fitness)

    
    print('\n')
    print('Update')
    break
    # Cập nhật hết alpha
full_update = False
table_db = 'TOP3000'
region = 'USA'
while not full_update:
    try:
        df_temp = pd.read_csv('unupdated_alpha.csv').drop_duplicates(subset='id',keep='first')
        lines = df_temp[['code','neutralization']].values.tolist()
        if (len(lines)) <1:
            
            break
            # sys.exit('Full Update')
        for i in range(len(lines)):
            alpha_code = lines[i][0].rstrip('\n')
            neutralization = lines[i][1].rstrip('\n')
            raw_alpha = Simulate(universe,region,neutralization).regular(alpha_code)
            df_temp[i+1::].to_csv('unupdated_alpha.csv',index=False) 
            print(raw_alpha)
            save(pd.DataFrame([raw_alpha]),'updated_alpha.csv') 
            print('Done')
        
        full_update = True
        break
    except Exception as e:
        print(e)
        pass

df=pd.read_csv('updated_alpha.csv',converters={'is':ast.literal_eval,'regular':ast.literal_eval}).drop_duplicates('id',keep='first')
df['code']=df.apply(get_code,axis=1)
df['raw']=df.apply(get_raw,axis=1)
df['fail']=df.apply(count_fail,axis=1)
df['sharpe']=df.apply(get_sharpe,axis=1)
df['fitness']=df.apply(get_fitness,axis=1)
df['them']=df.apply(get_result_theme,axis=1)

df[(df['fail']==0)].to_csv('done_alpha.csv',index=False,mode='a')
pd.DataFrame().to_csv('updated_alpha.csv')
