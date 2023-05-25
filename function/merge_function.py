import sys
sys.path.append("../")

import pandas as pd
import numpy as np

from function.alphas_function import *

def convert_str_to_list(val):
    if isinstance(val, str):
        return [val]
    return val

def measure_corr(pnl):
    max_pnl = 100000000
    num_ser = len(pnl)
    step = max_pnl/num_ser
    pnl_stand =np.arange(0,max_pnl,step)       
    cor_res = pnl.corrwith(pd.DataFrame(pnl_stand)[0])
    return cor_res

def measure_r_abs(pnl):
    max_pnl = 100000000
    num_ser = len(pnl)
    step = max_pnl/num_ser
    pnl_stand =np.arange(0,max_pnl,step)       
    r_abs_res = abs((pnl).sum()/(pnl_stand).sum())
    return r_abs_res    

def sum_df(x):
    try:
        return x.sum(axis=1)
    except:
        return x

def merge_good_bad(good,bad,pnl,file="merge_res_temp.csv"):
    res = []
    temp=[]
    temp1=[]
    for i in range(len(good)):
        for j in range(len(bad)):            
            temp.extend(convert_str_to_list(good[i]))
            temp.extend(convert_str_to_list(bad[j]))
            temp = sorted(temp)
            if temp not in temp1:
                me = pd.DataFrame((sum_df(pnl[good[i]])-sum_df(pnl[bad[j]]))/len(temp))
                me_cor =measure_corr(me)[0]       
                me_r_abs = measure_r_abs(me)[0] 
                a={"id":temp,"after_correlation":me_cor, "after_r_abs":me_r_abs}
                temp1.append(temp)            
                save(a,file)    
            temp=[]

def merge_good(good1,good2,pnl,file="merge_res_temp.csv"):
    res = []
    temp=[]
    temp1=[]
    for i in range(len(good1)):
        for j in range(len(good2)):            
            temp.extend(convert_str_to_list(good1[i]))
            temp.extend(convert_str_to_list(good2[j]))
            temp = sorted(temp)
            if temp not in temp1:
                me = pd.DataFrame((sum_df(pnl[good1[i]])+sum_df(pnl[good2[j]]))/len(temp))
                me_cor =measure_corr(me)[0]       
                me_r_abs = measure_r_abs(me)[0] 
                a={"id":temp,"after_correlation":me_cor, "after_r_abs":me_r_abs}
                temp1.append(temp)            
                save(a,file)    
            temp=[]

def merge_bad(bad1,bad2,pnl,file="merge_res_temp.csv"):
    res = []
    temp=[]
    temp1=[]
    for i in range(len(bad1)):
        for j in range(len(bad2)):            
            temp.extend(convert_str_to_list(bad1[i]))
            temp.extend(convert_str_to_list(bad2[j]))
            temp = sorted(temp)
            if temp not in temp1:
                me = pd.DataFrame((sum_df(pnl[bad1[i]])+sum_df(pnl[bad2[j]]))/len(temp))
                me_cor =measure_corr(me)[0]       
                me_r_abs = measure_r_abs(me)[0] 
                a={"id":temp,"after_correlation":me_cor, "after_r_abs":me_r_abs}
                temp1.append(temp)            
                save(a,file)    
            temp=[]

