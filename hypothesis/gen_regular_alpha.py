import sys
sys.path.append("../")

import random
from hypothesis.operators import *

# group = ['sector', 'industry', 'subindustry']

# day = ["5", "10", "20", "30", "40", "60", "63", "90", "100", "120", "126", "150", "180", "200", "240", "250","252", "256", "260", "270", "300", "360", "500"]

day = ["5", "10", "20", "30", "40", "60", "63", "90", "100", "120", "126", "150", "180", "200", "240", "250","252"]

ndays = []
for i in range(len(day)):
    for j in range(len(day)):
        for m in range(1, len(day)):
            for n in range(1, len(day)):
                if max(int(day[i]), int(day[j])) + int(day[m]) + int(day[n])> 800:
                    continue
                ndays.append([])
                ndays[-1].append(day[i])
                ndays[-1].append(day[j])
                ndays[-1].append(day[m])
                ndays[-1].append(day[n])

only_one = simple_operators + complex_operators + cross_sectional_operators + special_operators
inCor = only_one + group_operators + time_series_operators
# quantile = ["0.1","0.2","0.25", "0.3", "0.4", "0.6", "0.7", "0.75", "0.8", "0.85", "0.9", "0.95"]
rank = ['rank', 'group_rank', '']
before_corr = ["ts_delay", "ts_delta", "ts_ir", "ts_max", "ts_mean", "ts_median", "ts_min", "ts_rank","ts_sum","ts_zscore", "ts_arg_min", "ts_arg_max", "", "", "", "", "", "", "", "","", ""]

def get_param(data, rnd_ndays, group, k = 1):
    # if k != 0:
    #     k = random.randint(1,2)
    # if k == 2:
    #     rnd_data = random.choice(data)}/{random.choice(data)
    # else:
    rnd_data = random.choice(data)

    rnd_operator = random.choice(inCor)
    if rnd_operator == "":
        param = rnd_data
    elif rnd_operator in only_one:
        param = rnd_operator.replace("param", rnd_data)
    elif rnd_operator in group_operators:
        rnd_group = random.choice(group)
        param = rnd_operator.replace("param", rnd_data).replace("group", rnd_group)
    else:
        param = rnd_operator.replace("param", rnd_data).replace("ndays", rnd_ndays)
    return param

corr = ["ts_co_kurtosis","ts_co_skewness","ts_corr","ts_corr","ts_corr","ts_corr", "ts_covariance", "ts_covariance", "ts_regression"]
def get_alpha(data1, data2, rank, group):
    # days
    rnd_corr = random.choice(corr)
    rnd_ndays = random.choice(ndays)
    # params
    param1 = get_param(data1, rnd_ndays[0], group)
    param2 = get_param(data2, rnd_ndays[1], group)
    # before
    # rnd_before_corr = random.choice(before_corr)
    rnd_before_corr = ""
    rnd_rank = random.choice(rank)
    # rnd_rank = 'rank'
    if rnd_before_corr == "":
        if rnd_rank == 'rank':
            alpha = f"rank({rnd_corr}({param1},{param2},{rnd_ndays[2]}))"
        elif rnd_rank == '':
            alpha = f"{rnd_corr}({param1},{param2},{rnd_ndays[2]})"
        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_corr}({param1},{param2},{rnd_ndays[2]}),{rnd_group})"
    else:
        if rnd_rank == 'rank':
            alpha = f"rank({rnd_before_corr}({rnd_corr}({param1},{param2},{rnd_ndays[2]}),{rnd_ndays[3]}))"
        elif rnd_rank == '':
            alpha = f"{rnd_before_corr}({rnd_corr}({param1},{param2},{rnd_ndays[2]}),{rnd_ndays[3]})"
        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_before_corr}({rnd_corr}({param1},{param2},{rnd_ndays[2]}),{rnd_ndays[3]}),{rnd_group})"
    return alpha.replace(" ", "").lower()

neu_vector = ["vector_neut", "vector_proj", "regression_neut", "regression_proj"]
def get_neu_vector(data1, data2, rank, group):
    # days
    rnd_ndays = random.choice(ndays)
    # rnd_before_corr = random.choice(before_corr)
    rnd_before_corr = ""
    param1 = get_param(data1, rnd_ndays[0], group)
    param2 = get_param(data2, rnd_ndays[1], group)
    vec_neu = random.choice(neu_vector)
    rnd_rank = random.choice(rank)
    # rnd_rank = 'rank'
    if rnd_before_corr == "":
        if rnd_rank == 'rank':
            alpha = f"rank({vec_neu}({param1},{param2}))"
        elif rnd_rank == '':
            alpha = f'vec_neu({param1},{param2})'
        else:
            rnd_group = random.choice(group) 
            alpha = f"group_rank({vec_neu}({param1},{param2}),{rnd_group})"
    else:
        if rnd_rank == 'rank':
            alpha = f"rank({rnd_before_corr}({vec_neu}({param1},{param2}),{rnd_ndays[3]}))"
        elif rnd_rank == '':
            alpha = f"rnd_before_corr({vec_neu}({param1},{param2}),{rnd_ndays[3]})"
        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_before_corr}({vec_neu}({param1},{param2}),{rnd_ndays[3]}),{rnd_group})"
    return alpha.replace(" ", "").lower()

time_series_operators_befor = [o75, o78, o79, o80, o81, o89, o90, o91, o92, o93, o94, o95, o96, o97, o98, o99, o100, o106, o108, o109, o110, o111, o113, o116, "", "", "", "", ""]
def get_simple_alpha(data1, data2, rank, group):
    # days
    rnd_ndays = random.choice(ndays)
    rnd_before_corr = random.choice(before_corr)
    param1 = get_param(data1, rnd_ndays[0], group)
    param2 = get_param(data2, rnd_ndays[1], group)
    # vec_neu = random.choice(neu_vector)
    rnd_rank = random.choice(rank)
    # rnd_rank = 'rank'
    if rnd_before_corr == "":
        if rnd_rank == 'rank':
            alpha = f"rank({param1}/{param2})"
        # elif rnd_rank == '':
        #     alpha = vec_neu}({param1},{param2})'
        else:
            rnd_group = random.choice(group) 
            alpha = f"group_rank({param1}/{param2},{rnd_group})"
    else:
        if rnd_rank == 'rank':
            alpha = f"rank({rnd_before_corr}({param1}/{param2},{rnd_ndays[3]}))"

        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_before_corr}({param1}/{param2},{rnd_ndays[3]}),{rnd_group})"
    return alpha.replace(" ", "").lower()

def get_single_data(data1, data2, rank, group):
    # days
    rnd_ndays = random.choice(ndays)
    rnd_before_corr = random.choice(before_corr)
    param1 = get_param(data1, rnd_ndays[0], group)
    # param2 = get_param(data2, rnd_ndays[1], group)
    # vec_neu = random.choice(neu_vector)
    rnd_rank = random.choice(rank)
    # rnd_rank = 'rank'
    if rnd_before_corr == "":
        if rnd_rank == 'rank':
            alpha = f"rank({param1})"
        # elif rnd_rank == '':
        #     alpha = vec_neu}({param1},{param2})'
        else:
            rnd_group = random.choice(group) 
            alpha = f"group_rank({param1},{rnd_group})"
    else:
        if rnd_rank == 'rank':
            alpha = f"rank({rnd_before_corr}({param1},{rnd_ndays[3]}))"
        # elif rnd_rank == '':
        #     alpha = rnd_before_corr}({vec_neu}({param1},{param2}),{rnd_ndays[3]})"
        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_before_corr}({param1},{rnd_ndays[3]}),{rnd_group})"
    return alpha.replace(" ", "").lower()

corr_3 = ['ts_triple_corr', 'ts_partial_corr']
def get_three_param(data1, data2, rank, group):
    rnd_corr = random.choice(corr_3)
    rnd_ndays = random.choice(ndays)
    param1 = get_param(data1, rnd_ndays[0], group, k =1)
    param2 = get_param(data2, rnd_ndays[1], group, k =1)
    param3 = get_param(data2, random.choice(day),group, k=1)
    # param1 = random.choice(data1)
    # param2 = random.choice(data2)
    # param3 = random.choice(data2)
    # rnd_before_corr = random.choice(before_corr)
    rnd_before_corr = ""
    rnd_rank = random.choice(rank)
    # rnd_rank = 'rank'
    # if rnd_before_corr == "ts_percentage":
    #     rnd_quantile = random.choice(quantile)
    #     if rnd_rank == 'rank':
    #         alpha = "rank({rnd_before_corr}({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_ndays[3]},percentage={rnd_quantile})"
    #     elif rnd_rank == '':
    #         alpha = rnd_before_corr}({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_ndays[3]},percentage={rnd_quantile})"
    #     else:
    #         rnd_group = random.choice(group)
    #         alpha = "group_rank({rnd_before_corr}({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_ndays[3]},percentage={rnd_quantile}),{rnd_group})"
    if rnd_before_corr == "":
        if rnd_rank == 'rank':
            alpha = f"rank({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}))"
        elif rnd_rank == '':
            alpha = f"{rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]})"
        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_group})"
    else:
        if rnd_rank == 'rank':
            alpha = f"rank{rnd_before_corr}({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_ndays[3]}))"
        elif rnd_rank == '':
            alpha = f"{rnd_before_corr}({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_ndays[3]})"
        else:
            rnd_group = random.choice(group)
            alpha = f"group_rank({rnd_before_corr}({rnd_corr}({param1},{param2},{param3},{rnd_ndays[2]}),{rnd_ndays[3]}),{rnd_group})"
    # print(alpha)
    return alpha.replace(" ", "").lower()

def rnd_reg(data1, data2, rank, group):
    t = random.randint(1, 10)
    # return get_three_param(data1, data2, rank, group)   
    # return get_simple_alpha(data1, data2, rank, group)
    if t <= 3:
        return get_single_data(data1, data2, rank, group)    
    if t <= 6:
        return get_simple_alpha(data1, data2, rank, group)    
    elif t == 7:
        return get_alpha(data1, data2, rank, group)
    elif t == 8:
        return get_neu_vector(data1, data2, rank, group)
    else:
        return get_three_param(data1, data2, rank, group)