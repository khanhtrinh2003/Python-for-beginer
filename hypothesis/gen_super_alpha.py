
import random

combos = [
    "1",

    "stats = generate_stats(alpha); ts_ir(stats.returns, 500)",
    "stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr",
    "stats = generate_stats(alpha); 1/ts_std_dev(stats.returns,500)",
    "stats = generate_stats(alpha); ts_mean(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_arg_max(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_median(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_max(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_min(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_delay(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_av_diff(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_delta(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_returns(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_weighted_delay(stats.returns, 500)",
    "stats = generate_stats(alpha); ts_arg_min(stats.returns, 500)",

    "stats = generate_stats(alpha); ts_ir(stats.returns, 250)",
    "stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 250); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr",
    "stats = generate_stats(alpha); 1/ts_std_dev(stats.returns,250)",
    "stats = generate_stats(alpha); ts_mean(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_arg_max(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_median(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_max(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_min(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_delay(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_av_diff(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_delta(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_returns(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_weighted_delay(stats.returns, 250)",
    "stats = generate_stats(alpha); ts_arg_min(stats.returns, 250)",
    ]

def rnd_super(os_alpha_id,selectionLimit):
    q = random.randint(1,3)
    if q <=3:
        sample = random.sample(os_alpha_id, selectionLimit)
        selection = f'(name == "{sample[0]}")'
        for item in sample[1:]:
            selection += f' || (name == "{item}")'
        # selection += ')*-turnover'
    elif q <=4:
        sample = random.sample(os_alpha_id, 15)
        selection = f'((name == "{sample[0]}")'
        for item in sample[1:]:
            selection += f' || (name == "{item}")'
        selection += ')*-turnover'


    combo = random.choice(combos)
    return selection,combo
