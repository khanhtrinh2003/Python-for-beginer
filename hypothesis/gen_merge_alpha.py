import random

decay = ["ts_decay_linear", "ts_decay_exp_window", "ts_sum", "hump"]
ndays = ["3", "4", "5", "6", "8", "10", ""]
f = ["0.1", "0.2", "0.25", "0.3", "0.4", "0.5", "0.6", "0.7", "0.75", "0.8", "0.9"]
decays = [0,0,0,0,0,4,5,10]
# group = ['market', 'sector', 'industry', 'subindustry', 'ceil(rank(cap)*10)', 'ceil(rank(divide(debt,equity))*10)']
# rank = ["rank_by_side","rank","group_rank"]

def get_rnd_alpha(lines):
    rnd_alpha = random.choice(lines)
    lines.remove(rnd_alpha)
    # if 'group_neutralize' not in rnd_alpha[0]:
    #     alpha = 'group_neutralize(' + rnd_alpha[0] +','+ rnd_alpha[1] + ')'
    # else:
    alpha = rnd_alpha
    return alpha

def rnd_merge(lines):
    t = random.randint(1,7)
    if t <= 3:
        alpha_code, n_decay = get_alpha_raw_2(lines)
    elif t <= 5:
        alpha_code, n_decay = get_alpha_raw_3(lines)
    elif t <= 7:
        alpha_code, n_decay = get_alpha_raw_4(lines)
    else:
        alpha_code, n_decay = get_alpha_raw_5(lines)        

    return alpha_code, n_decay

def get_alpha_raw_2(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)

    n_decay = random.choice(decays)

    if alpha2[0] != '-':
        alpha2 = f'+{alpha2}'
    combine = alpha1 + alpha2

    return combine.replace(" ", "").lower(), n_decay

def get_alpha_raw_3(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)

    if alpha2[0] != '-':
        alpha2 = f'+{alpha2}'
    if alpha3[0] != '-':
        alpha3 = f'+{alpha3}'
    combine = alpha1 +alpha2+alpha3

    n_decay = random.choice(decays)

    return combine.replace(" ", "").lower(), n_decay

def get_alpha_raw_4(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)
    alpha4 = get_rnd_alpha(lines)

    if alpha2[0] != '-':
        alpha2 = f'+{alpha2}'
    if alpha3[0] != '-':
        alpha3 = f'+{alpha3}'
    if alpha4[0] != '-':
        alpha4 = f'+{alpha4}'
    combine = alpha1 +alpha2+alpha3+alpha4

    n_decay = random.choice(decays)

    return combine.replace(" ", "").lower(), n_decay

def get_alpha_raw_5(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)
    alpha4 = get_rnd_alpha(lines)
    alpha5 = get_rnd_alpha(lines)
    # q = random.randint(1,3)
    # if q == 1:
    #     # to nan
    #     combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+',filter=true)'
    # elif q ==2:
    #     # to nan
    #     combine = 'to_nan('+alpha1+',value=0, reverse=true)+to_nan('+alpha2+',value=0, reverse=true)+to_nan('+alpha3+',value=0, reverse=true)+to_nan('+\
    #         alpha4+',value=0, reverse=true)+to_nan('+alpha5+',value=0, reverse=true)'
    # elif q ==3:
    #     # to nan
    #     combine = 'add(to_nan('+alpha1+',value=0, reverse=true),to_nan('+alpha2+',value=0, reverse=true),to_nan('+alpha3+',value=0, reverse=true),to_nan('+\
    #         alpha4+',value=0, reverse=true),to_nan('+alpha5+',value=0, reverse=true))'
    # elif q == 4:
    #     # no nan
    #     combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5 + ')'
    # else:
    if alpha2[0] != '-':
        alpha2 = f'+{alpha2}'
    if alpha3[0] != '-':
        alpha3 = f'+{alpha3}'
    if alpha4[0] != '-':
        alpha4 = f'+{alpha4}'
    if alpha5[0] != '-':
        alpha5 = f'+{alpha5}'
    combine = alpha1 +alpha2+alpha3+alpha4+alpha5

    n_decay = random.choice(decays)

    return combine.replace(" ", "").lower(), n_decay

def get_alpha_raw_6(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)
    alpha4 = get_rnd_alpha(lines)
    alpha5 = get_rnd_alpha(lines)
    alpha6 = get_rnd_alpha(lines)

    q = random.randint(1,3)
    if q == 1:
        # to nan
        combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+','+alpha6+',filter=true)'
    # elif q ==2:
    #     # to nan
    #     combine = 'to_nan('+alpha1+',value=0, reverse=true)+to_nan('+alpha2+',value=0, reverse=true)+to_nan('+alpha3+',value=0, reverse=true)+to_nan('+\
    #         alpha4+',value=0, reverse=true)+to_nan('+alpha5+',value=0, reverse=true)+to_nan('+alpha6+',value=0, reverse=true)'
    # elif q ==3:
    #     # to nan
    #     combine = 'add(to_nan('+alpha1+',value=0, reverse=true),to_nan('+alpha2+',value=0, reverse=true),to_nan('+alpha3+',value=0, reverse=true),to_nan('+\
    #         alpha4+',value=0, reverse=true),to_nan('+alpha5+',value=0, reverse=true),to_nan('+alpha6+',value=0, reverse=true))'
    # elif q == 4:
    #     # no nan
    #     combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+','+alpha6 + ')'
    else:
        if alpha2[0] != '-':
            alpha2 = f'+{alpha2}'
        if alpha3[0] != '-':
            alpha3 = f'+{alpha3}'
        if alpha4[0] != '-':
            alpha4 = f'+{alpha4}'
        if alpha5[0] != '-':
            alpha5 = f'+{alpha5}'
        if alpha6[0] != '-':
            alpha6 = f'+{alpha6}'

        combine = alpha1 +alpha2+alpha3+alpha4+alpha5+alpha6

    return combine.replace(" ", "").lower(), 0      

def get_alpha_raw_7(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)
    alpha4 = get_rnd_alpha(lines)
    alpha5 = get_rnd_alpha(lines)
    alpha6 = get_rnd_alpha(lines)
    alpha7 = get_rnd_alpha(lines)

    q = random.randint(1,3)
    if q == 1:
        # to nan
        combine = f'add({alpha1},{alpha2},{alpha3},{alpha4},{alpha5},{alpha6},{alpha7},filter=true)'
    # elif q ==2:
    #     # to nan
    #     combine = 'to_nan('+alpha1+',value=0, reverse=true)+to_nan('+alpha2+',value=0, reverse=true)+to_nan('+alpha3+',value=0, reverse=true)+to_nan('+\
    #         alpha4+',value=0, reverse=true)+to_nan('+alpha5+',value=0, reverse=true)+to_nan('+alpha6+',value=0, reverse=true)+to_nan('+\
    #         alpha7+',value=0, reverse=true)'
    # elif q ==3:
    #     # to nan
    #     combine = 'add(to_nan('+alpha1+',value=0, reverse=true),to_nan('+alpha2+',value=0, reverse=true),to_nan('+alpha3+',value=0, reverse=true),to_nan('+\
    #         alpha4+',value=0, reverse=true),to_nan('+alpha5+',value=0, reverse=true),to_nan('+alpha6+',value=0, reverse=true),to_nan('+\
    #         alpha7+',value=0, reverse=true))'
    # elif q == 4:
    #     # no nan
    #     combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+','+alpha6+','+alpha7 + ')'
    else:
        if alpha2[0] != '-':
            alpha2 = f'+{alpha2}'
        if alpha3[0] != '-':
            alpha3 = f'+{alpha3}'
        if alpha4[0] != '-':
            alpha4 = f'+{alpha4}'
        if alpha5[0] != '-':
            alpha5 = f'+{alpha5}'
        if alpha6[0] != '-':
            alpha6 = f'+{alpha6}'
        if alpha7[0] != '-':
            alpha7 = f'+{alpha7}'

        combine = alpha1 +alpha2+alpha3+alpha4+alpha5+alpha6+alpha7

    return combine.replace(" ", "").lower(), 0    

def get_alpha_raw_8(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)
    alpha4 = get_rnd_alpha(lines)
    alpha5 = get_rnd_alpha(lines)
    alpha6 = get_rnd_alpha(lines)
    alpha7 = get_rnd_alpha(lines)
    alpha8 = get_rnd_alpha(lines)

    q = random.randint(1,3)
    if q == 1:
        # to nan
        combine = f'add({alpha1},{alpha2},{alpha3},{alpha4},{alpha5},{alpha6},{alpha7},{alpha8},filter=true)'
    # elif q ==2:
    #     # to nan
    #     combine = 'to_nan('+alpha1+',value=0, reverse=true)+to_nan('+alpha2+',value=0, reverse=true)+to_nan('+alpha3+',value=0, reverse=true)+to_nan('+\
    #         alpha4+',value=0, reverse=true)+to_nan('+alpha5+',value=0, reverse=true)+to_nan('+alpha6+',value=0, reverse=true)+to_nan('+\
    #         alpha7+',value=0, reverse=true)+to_nan('+ alpha8+',value=0, reverse=true)'
    # elif q ==3:
    #     # to nan
    #     combine = 'add(to_nan('+alpha1+',value=0, reverse=true),to_nan('+alpha2+',value=0, reverse=true),to_nan('+alpha3+',value=0, reverse=true),to_nan('+\
    #         alpha4+',value=0, reverse=true),to_nan('+alpha5+',value=0, reverse=true),to_nan('+alpha6+',value=0, reverse=true),to_nan('+\
    #         alpha7+',value=0, reverse=true),to_nan('+ alpha8+',value=0, reverse=true))'
    # elif q == 4:
    #     # no nan
    #     combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+','+alpha6+','+alpha7+','+ alpha8 + ')'
    else:
        if alpha2[0] != '-':
            alpha2 = f'+{alpha2}'
        if alpha3[0] != '-':
            alpha3 = f'+{alpha3}'
        if alpha4[0] != '-':
            alpha4 = f'+{alpha4}'
        if alpha5[0] != '-':
            alpha5 = f'+{alpha5}'
        if alpha6[0] != '-':
            alpha6 = f'+{alpha6}'
        if alpha7[0] != '-':
            alpha7 = f'+{alpha7}'
        if alpha8[0] != '-':
            alpha8 = f'+{alpha8}'
        combine = alpha1 +alpha2+alpha3+alpha4+alpha5+alpha6+alpha7+ alpha8
    n_decay = random.choice(decays)
    return combine.replace(" ", "").lower(), n_decay

def get_alpha_raw_10(lines):
    alpha1 = get_rnd_alpha(lines)
    alpha2 = get_rnd_alpha(lines)
    alpha3 = get_rnd_alpha(lines)
    alpha4 = get_rnd_alpha(lines)
    alpha5 = get_rnd_alpha(lines)
    alpha6 = get_rnd_alpha(lines)
    alpha7 = get_rnd_alpha(lines)
    alpha8 = get_rnd_alpha(lines)
    alpha9 = get_rnd_alpha(lines)
    alpha10 = get_rnd_alpha(lines)

    q = random.randint(1,3)
    if q == 1:
        # to nan
        combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+','+alpha6+','+alpha7+','+ alpha8+','+ alpha9+','+ alpha10+',filter=true)'
    # elif q ==2:
    #     # to nan
    #     combine = 'to_nan('+alpha1+',value=0, reverse=true)+to_nan('+alpha2+',value=0, reverse=true)+to_nan('+alpha3+',value=0, reverse=true)+to_nan('+\
    #         alpha4+',value=0, reverse=true)+to_nan('+alpha5+',value=0, reverse=true)+to_nan('+alpha6+',value=0, reverse=true)+to_nan('+\
    #         alpha7+',value=0, reverse=true)+to_nan('+ alpha8+',value=0, reverse=true)+to_nan('+ alpha9+',value=0, reverse=true)+to_nan('+ alpha10+',value=0, reverse=true)'
    # elif q ==3:
    #     # to nan
    #     combine = 'add(to_nan('+alpha1+',value=0, reverse=true),to_nan('+alpha2+',value=0, reverse=true),to_nan('+alpha3+',value=0, reverse=true),to_nan('+\
    #         alpha4+',value=0, reverse=true),to_nan('+alpha5+',value=0, reverse=true),to_nan('+alpha6+',value=0, reverse=true),to_nan('+\
    #         alpha7+',value=0, reverse=true),to_nan('+ alpha8+',value=0, reverse=true),to_nan('+ alpha9+',value=0, reverse=true),to_nan('+ alpha10+',value=0, reverse=true))'
    # elif q == 4:
    #     # no nan
    #     combine = 'add('+alpha1 +','+alpha2+','+alpha3+','+alpha4+','+alpha5+','+alpha6+','+alpha7+','+ alpha8 + ','+ alpha9 + ','+ alpha10 + ')'
    else:
        if alpha2[0] != '-':
            alpha2 = f'+{alpha2}'
        if alpha3[0] != '-':
            alpha3 = f'+{alpha3}'
        if alpha4[0] != '-':
            alpha4 = f'+{alpha4}'
        if alpha5[0] != '-':
            alpha5 = f'+{alpha5}'
        if alpha6[0] != '-':
            alpha6 = f'+{alpha6}'
        if alpha7[0] != '-':
            alpha7 = f'+{alpha7}'
        if alpha8[0] != '-':
            alpha8 = f'+{alpha8}'
        if alpha9[0] != '-':
            alpha9 = f'+{alpha9}'
        if alpha10[0] != '-':
            alpha10 = f'+{alpha10}'
        combine = alpha1 + alpha2 + alpha3 + alpha4 + alpha5 + alpha6 + alpha7 + alpha8 + alpha9 + alpha10
    n_decay = random.choice(decays)
    return combine.replace(" ", "").lower(), n_decay    