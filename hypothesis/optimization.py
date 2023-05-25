class TA():
    def __init__(self, alpha):
        self.alpha = alpha
        
    def mae(self):
        '''#Moving Average Envelopes'''
        return f"alpha = {self.alpha}; s = ts_mean(close,20); le1 = s * 0.95; le2 = s * 0.9; le3 = s * 0.85; le4 = s * 0.8; le5 = s * 0.75; le6 = s * 0.70; low < le6? alpha + 0.5*abs(alpha):low < le5? alpha + 0.4*abs(alpha) :low < le4? alpha + 0.32*abs(alpha):low < le3? alpha + 0.25*abs(alpha) :low < le2? alpha + 0.2*abs(alpha):low < le1? alpha+0.1*abs(alpha):alpha"

    def rsi(self):
        '''# Relative Strength Index '''
        return f"alpha = {self.alpha};RSI = (100 - 100 / (1 + ts_sum((ts_delta(close,1) > 0 ? ts_delta(close,1) : 0), 14) / ts_sum((ts_delta(close,1)< 0 ? - ts_delta(close,1) : 0), 14)));SRSI = (RSI-ts_min(RSI,14))/(ts_max(RSI,14)-ts_min(RSI,14)); SRSI <0.1 ? alpha+0.1*abs(alpha) : alpha"

    def kst(self):
        '''# Pring's Know Sure Thing (KST)'''
        return f"alpha ={self.alpha};RCMA1 = ts_decay_linear(ts_delta(close, 10), 10);RCMA2 = ts_decay_linear(ts_delta(close, 15), 10);RCMA3 = ts_decay_linear(ts_delta(close, 20), 10);RCMA4 = ts_decay_linear(ts_delta(close, 30), 15);KST = (RCMA1 * 1) + (RCMA2 * 2) + (RCMA3 * 3) + (RCMA4 * 4);SIG = ts_decay_linear(KST, 9); KST < SIG ? alpha + 0.1 * abs(alpha): alpha"
    
    def macd(self):
        '''# MACD (Moving Average Convergence/Divergence Oscillator)'''
        return f"alpha ={self.alpha};EMA_12=(close-ts_delay((ts_sum(close,12)/12),1))*0.1538+ts_delay((ts_sum(close,12)/12),1);EMA_26=(close-ts_delay((ts_sum(close,26)/26),1))*0.0741+ts_delay((ts_sum(close,26)/26),1); MACD=EMA_12-EMA_26; MACD<0?alpha+0.1*abs(alpha):alpha"

    def macd_his(self):
        '''# MACD Histogram'''
        return f"alpha ={self.alpha};EMA12=ts_decay_linear(close,12);EMA26=ts_decay_linear(close,26);MACDLine =  EMA12 - EMA26;SignalLine=ts_decay_linear(MACDLine,9);MACDHistogram = MACDLine - SignalLine; MACDHistogram > 0? alpha + 0.1*abs(alpha):alpha"

    def std(self):
        '''# Standard Deviation (Volatility)'''
        return f"alpha ={self.alpha}; ts_std_dev(close,20)/(ts_sum(close,20)/20)<0.2? alpha + 0.1*abs(alpha):alpha"

    def arron(self):
        '''# Aroon'''
        return f"alpha ={self.alpha}; AROUP = (25 - ts_arg_max(high, 25))/25; ARODO = (25 - ts_arg_min(low, 25))/25;REL = AROUP/ARODO; REL > 0.7 ? alpha + 0.1 * abs(alpha):alpha"

    def cmf(self):
        '''# Chaikin Money Flow (CMF)'''
        return f"alpha ={self.alpha}; MFM = ((close-low)-(high-close))/(high-low);MFV = MFM*volume;CFM = ts_sum(MFV,20)/ts_sum(volume,20); CFM > 0? alpha + 0.1*abs(alpha):alpha"

    def williams(self):
        '''# Williams %R'''
        return f"alpha ={self.alpha}; R = (ts_max(high,14)-close)/(ts_max(high,14)-ts_min(low,14))*(-100);R >-50? alpha+0.1*abs(alpha):alpha"
    
    def price_relative(self):
        '''# Price Relative / Relative Strength'''
        return f"alpha ={self.alpha}; REL = cap/group_sum(cap, market);SIG = ts_decay_linear(REL, 150);REL < SIG ? alpha + 0.1 * abs(alpha): alpha"        

    def rising_star(self):
        '''# Rising star'''
        return f'alpha ={self.alpha}; lastSAR = ts_delay(close,1) - 0.5*ts_std_dev(close,5);RisingSAR = lastSAR + 0.02*max(ts_sum(high>ts_max(high,5),20),10)*(ts_max(high,20)-lastSAR); close< RisingSAR ? alpha + 0.1*abs(alpha):alpha'

    def atr(self):
        '''# Average True Range (ATR)'''
        return f'alpha ={self.alpha}; TR = max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1)));ATR14 = ts_mean(TR,14); SMA20 = ts_mean(close,20); (ATR14/SMA20*100<4)?alpha+0.1*abs(alpha):alpha'

    def emv(self):    
        '''# Ease of Movement (EMV)'''
        return f'alpha ={self.alpha}; DistanceMoved = (high + low)/2-ts_delay((high + low)/2,1);BoxRatio = ((volume/100000000)/(high - low));EMV = DistanceMoved/BoxRatio;SMAEMA = ts_mean(EMV,14); SMAEMA > 0 ?alpha + 0.1*abs(alpha):alpha'

    def force_index(self):
        '''# Force Index'''
        return f'alpha ={self.alpha}; ForceIndex = (close-ts_delay(close,1))*volume;ForceIndex14 = ts_decay_linear(ForceIndex,14); ForceIndex14 > 0 ?alpha + 0.1*abs(alpha):alpha'

    def mass_index(self):    
        '''# Mass Index'''
        return f'alpha ={self.alpha}; DistanceMoved = high - low; SMA9 = ts_mean(DistanceMoved,9); SMA9ofSMA9 = ts_mean(SMA9,9); RatioofSMAs = SMA9/SMA9ofSMA9; MassIndex = ts_sum(RatioofSMAs,25); MassIndex < 26.5?alpha + 0.1*abs(alpha):alpha'

    def ulcer_index(self):
        '''# Ulcer Index'''
        return f'alpha ={self.alpha}; PD = (close-ts_max(close,14))/ts_max(close,14);SA = ts_mean(PD^2,14);UI = SA^0.5;UI < 10? alpha +0.1*abs(alpha) :alpha'    

    def ichimoku_cloud(self):
        '''# Ichimoku Cloud'''
        return f"alpha ={self.alpha}; bl = (ts_max(high, 26) - ts_min(low, 26))/2; close > bl ? alpha + 0.1 * abs(alpha): alpha"

    def keltner_channels(self):
        '''# Keltner Channels'''
        return f"alpha ={self.alpha}; TR = max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1))); ATR = ts_mean(TR,10); EMA = ts_decay_linear(close,20); LC = EMA - 2*ATR; low < LC ? alpha + 0.1*abs(alpha):alpha"

    def price_channels(self):
        '''# Price Channels'''
        return f'alpha ={self.alpha}; ll = ts_decay_linear(low, 20); (close < ll && ts_delta(close,1) > 0) ? alpha + 0.1 * abs(alpha): alpha'   

    def cci(self):
        '''# Commodity channel index'''
        return f'alpha ={self.alpha}; TP=(high+close+low)/3; CCI= (TP-ts_mean(TP,20))/(0.015*ts_std_dev(TP,20));CCI<=100?alpha+0.1*abs(alpha):alpha'

    def mfi(self):
        '''# Money Flow Index (MFI)'''
        return f'alpha ={self.alpha}; RMF = (High + Low + Close)/3 * Volume; MFR = ts_sum(ts_delta(close,1) > 0 ? RMF: 0, 14)/ts_sum(ts_delta(close,1) < 0 ? RMF: 0, 14); MFI = 100 - 100/(1 + MFR); MFI < 30 ? alpha + 0.1 * abs(alpha): alpha'
    
    def ppo(self):
        '''# Percentage Price Oscillator (PPO)'''
        return f'alpha={self.alpha};PPO = (ts_decay_exp(close, 0.1538, 12)/ts_decay_exp(close, 0.074, 26) - 1) * 100;SL = ts_decay_exp(PPO , 0.1, 9); PPO < SL ? alpha + 0.1 * abs(alpha): alpha'

    def stochastic_oscillator(self):
        '''# Stochastic Oscillator'''
        return f'alpha={self.alpha};pK = (close-ts_min(low,14))/(ts_max(high,14)-ts_min(low,14))*100;pD = ts_sum(pK,3)/3;pK<20?alpha + 0.1*abs(alpha):alpha'

    def stochastic_oscillator_2(self):
        '''# Stochastic Oscillator 2'''
        return f'alpha={self.alpha};pK = (close-ts_min(low,14))/(ts_max(high,14)-ts_min(low,14))*100;pD = ts_mean(pK,3); pK > 80? alpha - 0.1*abs(alpha): pK<20?alpha + 0.1*abs(alpha):alpha'

    def ultimate_oscillator(self):
        '''# Ultimate Oscillator'''
        return f'alpha={self.alpha};BP = close - min(low,ts_delay(close,1));TR = max(high,ts_delay(close,1))-min(low,ts_delay(close,1));AVG7 = ts_sum(BP,7)/ts_sum(TR,14);AVG14 = ts_sum(BP,14)/ts_sum(TR,14);AVG28 = ts_sum(BP,28)/ts_sum(TR,28);UO = 100*(4*AVG7+2*AVG14+AVG28)/7; UO <30 ? alpha + 0.1*abs(alpha):alpha'

    def vortex_indicator(self):
        '''# Vortex Indicator'''
        return f'alpha={self.alpha};VM1=ts_sum(abs(high -ts_delay(low,1)),14);VM2=ts_sum(abs(low-ts_delay(high,1)),14);TR = ts_sum(max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1))),14);VI1=VM1/TR;VI2=VM2/TR; abs(VI1-VI2)<0.1 ? alpha +0.1*abs(alpha):alpha'

    def tenkan(self):
        '''# Tenkan'''
        return f'alpha={self.alpha};Tenkan_Sen=(ts_max(high,9) + ts_min(low,9))/2; Kijun_Sen=(ts_max(high,26)+ts_min(low,26))/2; Senkou_Span_A=(Tenkan_Sen+Kijun_Sen)/2;Senkou_Span_B=(ts_max(high,52)+ts_min(low,52))/2;Kumo_peak=max(Senkou_Span_A,Senkou_Span_B); close<Kumo_peak?alpha+0.1*abs(alpha):alpha'

class My_strategy():
    def __init__(self):
        pass

    def Strategy_1(self,alpha):
        return f"{alpha}+rank(-ts_delta(close,3))"   
    
    def Strategy_2(self,alpha):
        return f"{alpha}+rank(-ts_delta(close,2))"    
    
    def Strategy_3(self, alpha, x="close", day=3):
        return f"{alpha}+exp(rank(-ts_delta(close,3)))"    
    
    def Strategy_4(self,alpha):
        return f"{alpha}-exp(rank(volume/adv20))"    
    
    def Strategy_5(self,alpha):
        return f"{alpha}+rank(-ts_delta(ts_mean(close,7),2))"  
    
    def Strategy_6(self,alpha):
        return f"{alpha}+rank(ts_delay(close, 2) - ts_regression(close, vwap, 60, lag=0, rettype=3))" 
    
    def Strategy_7(self,alpha):
        return f"{alpha}+(ts_sum(sign(ts_delta(close, 1)), 4) == -4 ? 0 : rank(-ts_delta(close, 2)))"    
    
    def Strategy_8(self,alpha):
        return f"{alpha}+(volume > adv20 ? 2 * rank(-ts_delta(close, 2)) : rank(-ts_delta(close, 2)))"    
    
    def Strategy_9(self,alpha):
        return f"{alpha}+(close>ts_sum(close, 20) / 20 ? 1.5 * rank(-ts_delta(close, 2)) : rank(-ts_delta(close, 2)))" 
    
    def Strategy_10(self,alpha):
        return f"{alpha}+rank(sales / assets)" 
    
    def Strategy_11(self,alpha):
        return f"{alpha}+rank(trade_when(volume > adv20, -returns, -1))"    
    
    def Strategy_12(self,alpha):
        return f"{alpha}-ts_regression(returns, ts_delay(returns, 1), 120)"    
        
    def Strategy_13(self,alpha):
        return f"{alpha}-rank(ts_delta(close,2)) * rank(volume / ts_sum(volume, 30) / 30)"    
        
    def Strategy_14(self,alpha):
        return f"a = ts_sum(open > close, 20) / ts_sum(open < close, 20); b = ts_sum(open > close, 250) / ts_sum(open < close, 250); {alpha}+rank(a / b)"    
        
    def Strategy_15(self,alpha):
        return f"bar = (open - close) / (high - low); a = ts_sum((open > close) * bar, 20) / ts_sum((open < close) * (-bar), 20); b = ts_sum((open > close) * bar, 250) / ts_sum((open < close) * (-bar), 250);{alpha}+rank(a / b)"    
        
    def Strategy_16(self,alpha):
        return f"{alpha}+ts_product(close, 5) ^ 0.2 - close"    
        
    def Strategy_17(self,alpha):
        return f"{alpha}+group_rank(eps / close, subindustry)"    
        
    def Strategy_18(self,alpha):
        return f"{alpha}+rank(trade_when(volume > adv20, -returns, -1))"    
       
class Merge():
    def __init__(self,good,bad) -> None:
        self.good = good
        self.bad = bad
        self.len_good = len(self.good)
        self.len_bad = len(self.bad)
    
    def bad1(self):
        alpha = []
        for j in self.bad:
            alpha.append(f"-({j})")
        return alpha
    
    def good1__bad1(self):
        alpha = []
        for i in self.good:
            for j in self.bad:
                alpha.append(f"{i}-({j})")
        return alpha
    
    def good2(self):
        alpha = []
        for i in range(self.len_bad-1):
            for j in range(i+1,self.len_bad):
                alpha.append(f"{i}+({j})")
        return alpha
    
    def bad2(self):
        alpha = []
        for i in range(self.len_bad-1):
            for j in range(i+1,self.len_bad):
                alpha.append(f"-({i})-({j})")
        return alpha
    
    def good1__bad2(self):
        alpha = []
        for i in range(self.len_good):
            for j in range(self.len_bad-1):
                for z in range(j+1,self.len_bad):
                    alpha.append(f"{i}-({j})-({z})")
        return alpha

class Sub_universe():
    def __init__(self) -> None:
        pass

    # Allocate more weight for stock having higher dollar volume
    def Strategy1(self,alpha):
        return f"{alpha} * rank(adv20*close)"
    
    def Strategy2(self,alpha):
        return f"{alpha} * power(rank(adv20*close),2.0)"   

    # Allocate more weight for stock having higher volatility 
    def Strategy3(self,alpha):
        return f"{alpha} * rank(ts_std_dev(close, 20)"
    
    def Strategy4(self,alpha):
        return f"{alpha} * power(rank(ts_std_dev(close,20),2.0)"       
    
    #  Apply decay ở alpha expression
    def Strategy5(self,alpha):
        return f"rank(adv20*close) > 0.66 ? ts_decay_linear(-ts_returns({alpha},5),5): ts_decay_linear(-ts_returns({alpha},5),15)"
    
    def Strategy6(self,alpha):
        return f"scale ({alpha}) + scale(rank(adv20*close) > 0.66 ? {alpha}: nan)"    