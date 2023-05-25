# General
universe = 'TOP3000'
neutralization = 'INDUSTRY'

GROUP = ['MARKET', 'SECTOR', 'INDUSTRY', 'SUBINDUSTRY']

# Sub
# sub_corr_all = '0.4'
# sub_shapre = '0.65'
# sub_long_short = '80'
# sub_error = '-1'
# sub_user_old = 'no'
# sub_only_rank = 'no'
# sub_scale = 'yes'

sub_sharpe_two = '0.6'
sub_long_short_two = '50'

max_sim = 100000

# Save
import datetime
save_dataset = 'MIX'
save_sharpe = '0.7'
save_fitness = '0.4'
# date_start = '2019-08-11'
date_start = (datetime.datetime.utcnow()-datetime.timedelta(hours = 29)).strftime('%Y-%m-%d')

# date_start = (datetime.datetime.utcnow()-datetime.timedelta(hours = 53)).strftime('%Y-%m-%d')

# Sim

# Submit
submit_date_start = (datetime.datetime.utcnow()-datetime.timedelta(hours = 24*7)).strftime('%Y-%m-%d')

submit_fitness = '1'
submit_only_one = 'yes'
submit_prod_corr = 0.6
submit_self_corr = 0.5
hidden = "no"


submit_prod_corr_2 = 0.6
submit_self_corr_2 = 0.6
hidden_y = "yes"

submit_prod_corr_3 = 0.7
submit_self_corr_3 = 0.7

submit_prod_corr_4 = 1
submit_self_corr_4 = 1

# theme
sub_corr_all_list = ['0.5', '0.6', '0.7']
sub_corr_all = '0.7'

sub_corr_self_list = ['0.4', '0.5']
sub_corr_self = '0.4'

sub_shapre = '0.7'

# sub_shapre = '0.6'
sub_long_short = '600'
sub_long_short_x2 = '600'
sub_error = '-1'
sub_user_old = 'no'
sub_only_rank = 'yes'
sub_scale = 'no'
sub_theme = 'no'
sub_shapre_2 = '0.65'
sub_neutralization = 'INDUSTRY'