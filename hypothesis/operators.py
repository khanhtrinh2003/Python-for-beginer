#  Simple Operators
# o1="abs(param)"#Absolute value of x
# o2="add(param, y, filter = false), x + y"#Add all inputs (at least 2 inputs required). If filter = true, filter all input nan to 0 before adding
# o3="ceil(param) "#nearest larger integer
# o4="divide(param, y), x / y"#x/y
# o5="exp(param)"#Natural exponential function : e^x
# o6="floor(param)"#nearest smaller integer
# o7="frac(param)"#x – floor(param)  i.e.  fractional component of the input x.
# o8="inverse(param)"#1 / x
o9="log(param)"#Natural logarithm. For example: Log(high/low) uses natural logarithm of high/low ratio as stock weights.
o10="log_diff(param)"#log(current value of input  or x[t] ) - log(previous value of input x[t-1])
# o11="max(param, y, ..)"#maximum value of all inputs; At least 2 inputs are required
# o12="min(param, y ..)"#minimum value of all inputs; At least 2 inputs are required
# o13="multiply(param ,y, ... , filter=false),  x * y"#multiply all inputs; (required 2 or more inputs); filter sets the nan values to 1 
# o14="nan_mask(param, y)"#replace input with NAN if input's corresponding mask value or the second input here, is negative.
# o15="nan_out(param, lower=0, upper=0)"#if (input < lower or input > upper) return NAN, else return input. At least one of "lower", "upper" is required.
# o16="power(param, y)"#input0 ^ input1
o16="power(param, 2)"#input0 ^ input1
o17="purify(param)"#clear infinities (+inf, -inf) by replacing with NaN
# o18="replace(param, target="v1 v2 ..vn", dest="d1,d2,..dn"); "#replace target values in input with destination values; Possible combinations of target value numbers and destination value numbers are ( N target -> N destination ; 1->1 and N->1 replacement); The target and destination values are entered within quotes and are space seperated.
# o19="reverse(param)"#- x
# o20="round(param)"#round input to closest integer.
# o21="round0(param, f=1)"#round input to greatest multiple of f less than input;
o22="sign(param)"#if input = NaN; return NaN else if input > 0, return 1 else if input < 0, return -1 else if input = 0, return 0
# o23="signed_power(param, y)"#input1 > 0, input1^input2; input1 < 0, -1 * input1^input2;
o23="signed_power(param, 2)"#input1 > 0, input1^input2; input1 < 0, -1 * input1^input2;
o24="s_log_1p(param)"#sign(input) * log(1 + abs(input))
o25="sqrt(param)"#square root of x
# o26="subtract(param, y, filter=false), x - y"#input1 - input2. If filter = true, filter all input nan to 0 before subtracting
# o27="to_nan(param, value=0, reverse=false)"#convert value to nan or nan to value if reverse is set as true 
o28="densify(param)"
simple_operators = [o9, o10, o16, o17, o22, o23, o24, o25, o28, "", ""]

# Logical Operators
#input1 and input2logical AND operator returns 1 if both inputs are not 0 and returns 0 otherwise
#input1 or input2logical or operator returns 1 if either input are not 0 and returns 0 otherwise
#input1 equal input2, input1 == input2logical AND operator returns 1 if both inputs are same and returns 0 otherwise
#negate(input)if input = 0 return 0, else return 1
#input1 less input2, input1 < input2if input1 < input2 return 1, else return 0
#if_else(input1, input2, input 3)If (input1 is true)  input2 else input3.
#is_not_nan(input)if (input = NAN) return 1 else return 0
#is_nan(input)if (input == NAN) return 1 else return 0
#is_finite(input)if (input NAN or input h1. INF) return 0else return 1
#is_not_finite(input)if (input NAN or input == INF) return 1 else return 0

# Complex Operators
# o28="arc_cos(param)"#if -1 <= x <= 1: arccos(param); else NAN
# o29="arc_sin(param)"#if -1 <= x <= 1: arcsin(param); else NAN
o30="arc_tan(param)"#arctg(param)
# o31="bucket(rank(param), range="0, 1, 0.1" or buckets = "2,5,6,7,10")"#Convert x into index values of customizable buckets. Range is used for equally sized buckets; buckets is used for variable sized buckets. Eg. with range="0.1, 1, 0.1", the vector "0.05, 0.5, 0.9" becomes "0, 4, 8"; with buckets="2, 5, 6, 7, 10", the vector "-1, 3, 6, 8, 12" becomes "0, 1, 2, 4, 5"
# o32="clamp(param, lower = 0, upper = 0, inverse = False, mask = "")"#q = ifelse(param < lower, lower, x); u = ifelse(q > upper, upper, q); v = ifelse(param > lower && x < upper, mask, x); ifelse(inverse, v, u) where mask is 'nearest_bound',  'mean', 'NAN' or any floating point number
# o33="filter(param, h = "1, 2, 3, 4", t="0.5")"#out[t] = h[0]*x[t-1] + h[1]*x[t-2] + ... + t[0]*out[t-1] + t[1]*out[t-2] + …
# o34="keep(param, f, period = 5)"#D = daysfromlastchange(f); u = tradewhen(D <  period, v, D > period); u period must be specified as a keyword argument
# o35="left_tail(param, maximum = 0)"#Nan everything greater than maximum, maximum should be constant.
# o36="pasteurize(param)"#Set to NAN if x is INF or if the underlying instrument is not in the alpha universe
# o37="right_tail(param, minimum = 0)"#Nan everything less than minimum, minimum should be constant.
o38="sigmoid(param)"#1 / (1 + exp(-x))
# o39="tail(param, lower = 0, upper = 0, newval = 0)"#if (x > lower && x < upper) return newval, else return x. Lower, upper, newval should be constants
o40="tanh(param)"#Hyperbolic tangent of x
# o41="trade_when(param, y, z)"#TradeWhen(x=triggerTradeExp, y=alphaExp, z=triggerExitExp). If triggerExitExp > 0, alpha = nan; else if triggerTradeExp > 0, alpha = alphaExp; else, alpha = previousAlpha
complex_operators = [o30, o38, o40, "", ""]


#Cross Sectional Operators
# o42="normalize(param, useStd = false, limit = 0.0)"#Calculates the mean value of all valid alpha values for the di, then subtracts that mean from each element. If useStd= true, calculates the standard deviation of the resulting values and divides each element by it. If limit != 0.0, puts the limit of the resulting alpha values (between -limit to + limit).
o42="normalize(param)"
# o43="one_side(param , side = long )"#shifts all instruments up or down so that the alpha becomes long-only or short-only (if side = short), respectively.
# o44="quantile(param, ndaysriver = gaussian, sigma = 1.0)"#Rank the raw vector, shift the ranked alpha vector, apply distribution ( gaussian , cauchy, uniform ). If driver is uniform, it simply subtract each alpha value with the mean of all alpha values in the alpha vector
o44="quantile(param)"
# o45="rank(param, rate=2)"#ranks the input among all the instruments and returns an equally distributed number between 0.0 and 1.0. For precise sort, use the rate as 0
o45="rank(param)"#ranks the input among all the instruments and returns an equally distributed number between 0.0 and 1.0. For precise sort, use the rate as 0
# o46="rank_by_side(param, rate=2,scale=1)"#rank positive and  negative input seperately, and scale to book; For precise sorting, rate=0 can be used;
# o47="regression_neut(y, param)"#Neutralized output (Y-a-(b*X)) after conducting cross-sectional Regression(Y,X)
# o48="regression_proj(y, param)"#Projected output (a+b*X) where parameters, a and b, are calulcated  after conducting cross sectional regression of (Y,X)
# o49="scale(param, scale=1, longscale=1, shortscale=1)"#scale input to booksize; Alternatively,we can also scale the long positions and short positions to separate scales by mentioning additional parameters to the operator: longscale= long booksize and shortscale=short booksize; 
o49="scale(param)"
# o50="scale_down(param,constant=0)"#(param - min(input)) / (max(input) - min(input))-constant
o50="scale_down(param)"
# o51="truncate(param,maxPercent=0.01)"#pre truncate to max percent
# o52="vector_neut(param, y)"#input1 neutralize to input2
# o53="vector_proj(param, y, filter=false)"#input1 projection to input2
# o54="winsorize(param, std=4)"#make sure that all values are between the lower and upper limits, which are specified as multiple of std
o54 = "winsorize(param)"
o55="zscore(param)"#(param - mean(param)) / stddev(param)
cross_sectional_operators = [o42, o44, o45, o49, o50, o54, o55, "", ""]

#Group Operators
# o56="group_backfill(param, group, d, std = 4.0)"#remove each nan in x by:  selecting set of all same-group non-nan x values during last d days winsorize said set at std  calculate mean value of resulting set and replace nan with it
# o57="group_count(param, group, ignoreNanInput=False)"#Gives the number of instruments in the same group (e.g. sector) which have valid values of x. When x is not specified, gives the number of instruments in each group (without regard for whether any particular field has valid data). If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the count valid value of that group  in output.
# o58="group_extra(param, weight, group)"#Replaces NAN values by their corresponding group means.
# o59="group_max(param, group, ignoreNanInput=False)"#Maximum of x for all instruments in the same group. If ignoreNanInput is False, default will keep same nan in output as input.(Default is False). If ignoreNanInput is True, it will keep the max value of that group in output.
# o60="group_mean(param, weight, group, ignoreNanInput=False)                                                                                                             "#All elements in group equals to the mean value of the group.  Mean=sum(data*weight) / sum(weight) in each group. If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the mean value of that group in output.
# o61="group_median(param, group, ignoreNanInput=False)"#All elements in group equals to the median value of the group.  If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the median value of that group in output.
# o62="group_min(param, group, ignoreNanInput=False)"#All elements in group equals to the min value of the group. If ignoreNanInput is False, default will keep same nan in output as input(Default is False) If ignoreNanInput is True, it will keep the min value of that group in output.
# o63="group_neutralize(param, group)"#Neutralizes Alpha x against groupings specified by group, which can be any classifier such as subindustry, industry, sector or a constant.  
# o64="group_normalize(param, group, constantCheck=False, tolerance=0.01, scale=1)"#Normalizes input such that each group's absolute sum is 1; out = input / absolute_sum in each group. Tolerance: constant-ness tolerance.  ConstantCheck: If sanity check fails it assigns NaN to output. Currently two sanity checks are done. First one is to check whether all numbers in a group is the same. Second one is to check all numbers in a group almost same (uses tolerance). The latter one checks constant-ness as an absolute difference if (group max - group min) < abs(group min) * tolerance; then it is constant.  Scale: Output scaling factor. Output = input / absolute_sum * scale for each group.  
o64="group_normalize(param, group)"#Normalizes input such that each group's absolute sum is 1; out = input / absolute_sum in each group. Tolerance: constant-ness tolerance.  ConstantCheck: If sanity check fails it assigns NaN to output. Currently two sanity checks are done. First one is to check whether all numbers in a group is the same. Second one is to check all numbers in a group almost same (uses tolerance). The latter one checks constant-ness as an absolute difference if (group max - group min) < abs(group min) * tolerance; then it is constant.  Scale: Output scaling factor. Output = input / absolute_sum * scale for each group.  
# o65="group_percentage(param, group, percentage=p%, ignoreNanInput=False)"#All elements in group equals to the value over the percentage of the group Percentage = 0.5 this value is equal to groupmedian(param,group) If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the percentage value of that group  in output.
# o66="group_rank(param, group, ignoreNanInput=False)"#Each elements in a group is assigned the corresponding rank in this group If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the 0 value of that group  in output.
o66="group_rank(param, group)"#Each elements in a group is assigned the corresponding rank in this group If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the 0 value of that group  in output.
o67="group_scale(param, group)"#(param - groupmin)/(groupmax - groupmin)
# o68="group_stddev(param, group, ignoreNanInput=False)"#All elements in group equals to the stddev of the group. If ignoreNanInput is False, nan data will be keep in output as input (Default is False). If ignoreNanInput is True, it will keep the standard deviation of that group in output.
# o69="group_sum(param, group, ignoreNaNInput=False)"#Sum of x for all instruments in the same group. If ignoreNanInput is False, default will keep same nan in output as input (Default is False). If ignoreNanInput is True, it will keep the sum of that group in output.
o70="group_zscore(param, group)"#ZScore = (data - mean) / StdDev of x for each instrument within its group.
group_operators = [o64, o66, o67, o70, "", ""]



#Time Series Operators
# o72="ema_decay(param, k=0.5)"#x * k + tsdelay (param, 1) * (1 - k). If not specified, by default k = 0.5
# o73="hump(param, hump = 0.01)"#hump must be specified as a keyword argument ifelse(abs(param – tsdelay(hump(param, 1)) < threshold, tsdelay(hump(param), 1), tsdelay(hump(param), 1) + thr * sign(param - tsdelay(hump(param), 1)), where thr = hump * BookSizeX / 2  BookSizeX = groupsum(pasteurize(abs(param), market)
# o74="hump_decay(param, p=0)"#if abs(tsdelta(param,1))> p: x; else tsdelta(param,1)
o75="inst_tvr(param, ndays)"#total trading value / total holding value in the past d days
# o76="jump_decay(param, ndays, sensitivity=0.5, force=0.1)"#If there is a huge jump in current data compare to previous one, apply force: jumpdecay(param) = abs(param-tsdelay(param, 1)) > sensitivity * tsstddev(param,d) ? tsdelay(param,1) + tsdelta(param, 1) * force : x
# o77="kth_element(param, ndays, k=0)"#returns k-th value of input by looking through lookback days. This operator can be used to backfill missing data if k=1.
o78="last_diff_value(param, ndays)"#last x value not equal to current x value from last d days
o79="ts_arg_max(param, ndays)"#it returns the relative index of the max value in the time series for the past d days.  If the current day has the max value for the past ddays, it returns 0.  If previous day has the max value for the past d days, it returns 1.  If all values in the past d days are NaN, it returns 0.
o80="ts_arg_min(param, ndays)"#it returns the relative index of the min value in the time series for the past d days.  If the current day has the min value for the past d days, it returns 0.  If previous day has the min value for the past d days, it returns 1.  If all values in the past d days are NaN, it returns 0.
o81="ts_av_diff(param, ndays)"#x - tsmean(param, ndays), but deals with NaNs carefuly
# o82="ts_co_kurtosis(y, param, ndays)"#return cokurtosis of y and x for the past d days
# o83="ts_corr(param, y, d)"#return correlation of x and y for the past d days
# o84="ts_co_skewness(y, param, ndays)"#return coskewness of y and x for the past d days
# o85="ts_count_nans(param ,d)"#return the number of NaN values in x for the past d days
# o86="ts_covariance(y, param, ndays)"#covariance of y and x for the past d days
# o87="ts_decay_exp_window(param, ndays, factor = 1, nan = True)"#return exponential decay of x with smoothing factor for the past d days;  nan parameter True means convert result to nan if all values are nan
# o88="ts_decay_linear(param, ndays, nan = true, dense = false)"#the linear decay on x for the past d days. 'nan' parameter shows whether convert result to nan if all time series is nan.  If not specified, by default 'nan' parameter is 'true'. 'Dense' parameter defines the mode: by default operator works in sparse mode. In sparse mode, when an alpha component is nan, we treat nan as zero. In dense mode we do not.
o89="ts_delay(param, ndays)"#x value d days ago
o90="ts_delta(param, ndays)"#x - tsdelay(param, ndays)
o91="ts_ir(param, ndays)"#tsmean(param, ndays) / tsstddev(param, ndays)
o92="ts_kurtosis(param, ndays)"#kurtosis of x for the last d days.
o93="ts_max(param, ndays)"#max value of x for the past d days
o94="ts_max_diff(param, ndays)"#x - tsmax(param, ndays)
# o95="ts_mean(param, ndays, nan = true)"#average value of x for the past d days. 'nan' parameter shows whether convert result to nan if all time series is nan.  If not specified, by default 'nan' parameter is 'true'. 
o95="ts_mean(param, ndays)"
o96="ts_median(param, ndays)"#median value of x for the past d days
o97="ts_min(param, ndays)"#min value of x for the past d days
o98="ts_min_diff(param, ndays)"#x - tsmin(param, ndays)
# o99="ts_min_max_cps(param, ndays, f = 2)"#(tsmin(param, ndays) + tsmax(param, ndays)) - f * x. If not specified, by default f = 2
o99="ts_min_max_cps(param, ndays)"#(tsmin(param, ndays) + tsmax(param, ndays)) - f * x. If not specified, by default f = 2
o100="ts_min_max_diff(param, ndays)"#x - f * (tsmin(param, ndays) + tsmax(param, ndays)). If not specified, by default f = 0.5
# o100="ts_min_max_diff(param, ndays, f = 0.5)"#x - f * (tsmin(param, ndays) + tsmax(param, ndays)). If not specified, by default f = 0.5
# o101="ts_moment(param, ndays, k=0)"#return kth central moment of x for the past d days; k = 1, 2, 3…
# o102="ts_partial_corr(param, y, z, d)"#return partial correlation of x, y, z for the past d days.
# o103="ts_percentage(param,ndays,quantile)"#return percentile value of x for the past d days
# o104="ts_poly_regression(y, param, ndays, k = 1)"#given regression Ey = x + x^2 + … + x^k over d days, output is y - Ey k must be specified as a keyword argument
# o105="ts_product(param, ndays, nan = True)"#product of x for the past d days; nan parameter True means convert result to nan if all values are nan
# o106="ts_rank(param, ndays, constant = 0)"#Rank the values of x for each instrument over the past d days, then return the rank of the current value + constant: tsrank(param, ndays) + constant. If not  specified, by default, constant = 0.
o106="ts_rank(param, ndays)"#Rank the values of x for each instrument over the past d days, then return the rank of the current value + constant: tsrank(param, ndays) + constant. If not  specified, by default, constant = 0.
# o107="ts_regression(y, param, ndays, lag = 0, rettype = 0)"#given linear regression Ey = b * tsdelay(param, lag) + a, output is (based on retttype): 0: y - Ey, 1: a, 2: b, 3: Ey … ; additional rettype values are present on "detailed descriptions" page
# o108="ts_returns (param, ndays, mode = 1)"#mode == 1: (param – tsdelay(param, ndays )) / tsdelay(param, ndays) mode == 2: (param – tsdelay(param, ndays )) / ((param + tsdelay(param, ndays))/2)
o108="ts_returns(param, ndays)"#mode == 1: (param – tsdelay(param, ndays )) / tsdelay(param, ndays) mode == 2: (param – tsdelay(param, ndays )) / ((param + tsdelay(param, ndays))/2)
# o109="ts_scale(param, ndays, constant = 0)"#(param - tsmin(param, ndays)) / (tsmax(param, ndays) - tsmin(param, ndays)) + constant
o109="ts_scale(param, ndays)"#(param - tsmin(param, ndays)) / (tsmax(param, ndays) - tsmin(param, ndays)) + constant
o110="ts_skewness(param, ndays)"#return skewness of x for the past d days.
o111="ts_stddev(param, ndays)"#return standard deviation of x for the past d days
# o112="ts_step(1), step(1)"#returns days' counter
# o113="ts_sum(param, ndays, nan = true)"#sum values of x for the past d days. 'nan' parameter shows whether convert result to nan if all time series is nan.  If not specified, by default 'nan' parameter is 'true'.
o113="ts_sum(param, ndays)"#sum values of x for the past d days. 'nan' parameter shows whether convert result to nan if all time series is nan.  If not specified, by default 'nan' parameter is 'true'.
# o114="ts_theilsen(param, y, d)"#Theil Sen slope estimator of inputs for the past n days.
# o115="ts_triple_corr(param, y, z, d)"#return triple correlation of x, y, z for the past d days.
o116="ts_zscore(param, ndays)"#(param - tsmean(param,d)) / tsstddev(param,d)
time_series_operators = [o75, o78, o79, o80, o81, o89, o90, o91, o92, o93, o94, o95, o96, o97, o98, o99, o100, o106, o108, o109, o110, o111, o113, o116, "", "", ""]


#Special Operators
# o117="convert(param, mode = "dollar2share")"#convert dollars to share or share to dollar when mode = "share2dollar"
o118="inst_pnl(param)"#generate pnl per instruments
o71="days_from_last_change(param)"#amount of days since last change of x
o119="ts_weighted_delay(param)"
special_operators = [o118, o71, o119, ""]