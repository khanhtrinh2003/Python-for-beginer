from hypothesis.optimization import *
from function.alphas_function import *
import ast
import random
def rnd_opt(alpha_code):
    num = random.randint(1,10)
    if num <=5:
        return My_strategy().Strategy_8(alpha_code)
    elif num<=7:
        return My_strategy().Strategy_2(alpha_code)
    elif num<=10:
        return My_strategy().Strategy_9(alpha_code)
    
df=pd.read_csv('updated_alpha.csv',converters={'regular':ast.literal_eval,'is':ast.literal_eval}).drop_duplicates('id',keep='first')
df['code']=df.apply(get_code,axis=1)
df['pass']=df.apply(count_pass,axis=1)
lis=df[df['pass']==5]['code'].to_list()
for i in lis:
    a=Simulate(decay=5).regular(My_strategy().Strategy_8(i))
    if count_pass(a)<6:
        continue
    else:
        pass
