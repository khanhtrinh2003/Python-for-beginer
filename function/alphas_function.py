import sys
sys.path.append("../")

from function.login import *
# Basic modules
import requests
import time
import os
import json
import pandas as pd
import numpy as np
import re
import random
from datetime import datetime,timedelta


class Infor():
    def __init__(self):
        self.headers = headers

    def get_api_data(self, url, ):
        response = requests.get(url, headers=self.headers)              
        a = response.json()
        return a 

    def get_alpha(self, alpha_id):
        url = f"https://api.worldquantbrain.com/alphas/{alpha_id}"
        a = self.get_api_data(url)
        return a

    def check_alpha(self, alpha_id):
        url = f"https://api.worldquantbrain.com/alphas/{alpha_id}/check"
        a = self.get_api_data(url)
        return a

    def get_pnl(self,alpha_id):
        url = f"https://api.worldquantbrain.com/alphas/{alpha_id}/recordsets/pnl"
        payload = json.dumps({
            "hidden": True
            })
        
        response = requests.request("PATCH", url, headers=headers, data=payload)

    def get_yearly_stats(self, alpha_id):        
        url = f"https://api.worldquantbrain.com/alphas/{alpha_id}"
        a = self.get_api_data(url)
        return a
    
    def hidden_alpha(self, alpha_id):        
        url = f"https://api.worldquantbrain.com/alphas/{alpha_id}/recordsets/yearly-stats"
        a = self.get_api_data(url)
        return a

    def before_after(self,alpha_id):
        url = f"https://api.worldquantbrain.com/competitions/MAPC2023/alphas/{alpha_id}/before-and-after-performance"
        a = self.get_api_data(url)
        return a["score"]
         
    def get_prod_corr(self, alpha_id, save = False):
        done = False
        payload={}
        while not done:
            try:
                url = f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod"
                # prod_corr = self.session.get(query_prod_corr.format(alpha_id = alpha_id)).json()
                prod_corr = requests.request("GET", url, headers=self.headers, data=payload).json()

                if "Incorrect authentication credentials" in str(prod_corr):
                    if save:
                        return False
                    else:
                        print("Incorrect authentication credentials")
                        sys.exit("Bye")
                elif 'records' in str(prod_corr):
                    try:
                        for i in range(len(prod_corr['records'])):
                            j = 19 - i
                            if prod_corr['records'][j][2] !=0:
                                break
                        prod_corr = prod_corr['records'][j][1]
                    except Exception as e:
                        prod_corr = 0.99
                        print('prod_corr', e)
                    done = True
                elif 'THROTTLED' in str(prod_corr):
                    time.sleep(5)
                else:
                    print('prod_corr', prod_corr)
            except Exception:
                time.sleep(5)
                pass
        return prod_corr

    def get_self_corr(self, alpha_id, save = False):
        done = False
        # return 0
        payload={}
        while not done:
            try:
                url = f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/self"
                # self_corr = self.session.get(query_self_corr.format(alpha_id = alpha_id)).json()
                self_corr = requests.request("GET", url, headers=self.headers, data=payload).json()

                if "Incorrect authentication credentials" in str(self_corr):
                    if save:
                        return False
                    else:
                        print("Incorrect authentication credentials")
                        sys.exit("Bye")
                elif 'records' in str(self_corr):
                    try:
                        self_corr = self_corr['records'][0][5]
                    except Exception as e:
                        print('self_corr', e)
                        self_corr = 0
                    done = True
                elif 'THROTTLED' in str(self_corr):
                    time.sleep(5)
                else:
                    print('self corr', self_corr)
            except Exception as e:
                time.sleep(5)
                pass
        return self_corr

    def get_data_is(self, prefix = '', offset = '0', universe = 'TOP150', date_start = '2019-06-20', sharpe = '0.7', fitness = '0.7'):
        if prefix == '-':
            url = f"https://api.worldquantbrain.com/users/self/alphas?limit=10&offset={offset}&settings.universe={universe}&dateCreated%3E{date_start}T00:00:00.000Z&dateCreated%3C2119-05-11T04:00:00.000Z&stage=IS&is.sharpe%3C=-{sharpe}&is.fitness%3C=-{fitness}&order=dateCreated&hidden=false&type=REGULAR"
        else:
            url = f"https://api.worldquantbrain.com/users/self/alphas?limit=10&offset={offset}&settings.universe={universe}&dateCreated%3E{date_start}T00:00:00.000Z&dateCreated%3C2119-05-11T04:00:00.000Z&stage=IS&is.sharpe%3E={sharpe}&is.fitness%3E={fitness}&order=dateCreated&hidden=false&type=REGULAR"        
        payload = {}
        done_p = False
        while not done_p:
            try:
                # Get PURPLE
                # data = self.session.get(query_format).json()
                data = requests.request("GET", url, headers=self.headers, data={}).json()
                if "Incorrect authentication credentials" in str(data):
                    print('Incorrect authen')                
                elif data['count'] == 0:
                    print("Don't have data")
                    # sys.exit("Don't have data")
                else:
                    print('Count Api: ', data['count'])
                    # print(data)
                    done_p = True
            except Exception as e:
                print(e)
                print('Wait')
                time.sleep(10)
                # sys.exit('Done')
                pass
        return data
    
    def get_data_os(self, offset = '0', region = 'USA', sharpe = '1.58', fitness = '1'):
        payload = {}
        url = f"https://api.worldquantbrain.com/users/self/alphas?limit=10&offset={offset}&stage=OS%1fPROD&order=-dateCreated&type=REGULAR&settings.region={region}&is.turnover%3C0.3&settings.universe=TOP3000"
        data = requests.request("GET", url, headers=self.headers, data=payload).json()

        if "Incorrect authentication credentials" in str(data):
            print('Incorrect authen')
        # print(data)
        # data = self.session.get(query_format).json()

        return data

    def get_perfect_alpha(self, df, path):
        file_names = ["perfect.csv", "only1.csv", "oeoe.csv"]
        
        df["pass"] = df.apply(count_pass,axis=1)
        df["code"] = df.apply(get_code,axis=1)
        df["fitness"] = df.apply(get_fitness,axis=1)
        df["sharpe"] = df.apply(get_sharpe,axis=1)
        df["turnover"] = df.apply(get_turnover,axis=1)        

        df1 = df[["pass","id","fitness","sharpe","turnover","code"]].sort_values(by="fitness",ascending=False)

        header1 = not os.path.exists(f"{path}/{file_names[0]}")
        df1[df1["pass"]>=6].to_csv(f"{path}/{file_names[0]}", mode="a", header=header1, index=False)

        header2 = not os.path.exists(f"{path}/{file_names[1]}")
        df1[(df1["pass"]==5) & (df1["pass"]>=5)].to_csv(f"{path}/{file_names[1]}", mode="a", header=header2, index=False)   

        header3 = not os.path.exists(f"{path}/{file_names[1]}")
        df1[(df1["pass"]<5)].to_csv(f"{path}/{file_names[2]}", mode="a", header=header3, index=False)            

    def get_base_payment(self):
        url = "https://api.worldquantbrain.com/users/self/activities/base-payment"
        payload={}
        # headers = {
        #     'accept': 'application/json;version=3.0',
        # }

        data = self.get_api_data(url)
        # print(data)
        try:
            print('yesterday: ', data['yesterday'])
            print('current: ', data['current'])
            print('previous: ', data['previous'])
        except Exception:
            print(data)

    def get_other_payment(self):
        url = "https://api.worldquantbrain.com/users/self/activities/other-payment"
        payload={}

        data = self.get_api_data(url)
        # print(data)
        try:
            # print(data)
            print('total: ', data['total']['value'])
            print('records: ', data['records']["records"])
            # print('previous: ', data['previous'])
        except Exception:
            print(data) 

    def get_noti(self, type_noti = 'ANNOUNCEMENT'):
        payload = {}
        url_query = f"https://api.worldquantbrain.com/users/self/messages?type={type_noti}&order=-dateCreated&limit=3&offset=0"
        url = url_query.format(type_noti = type_noti)
        data = self.get_api_data(url)
        try:
            print(json.loads(data))
        except Exception:
            print(data)

    def get_check_ladder(self, alpha_id, save = False):
        done_get = False
        while not done_get:
            result_get = requests.request("GET", f'https://api.worldquantbrain.com/alphas/{alpha_id}/check', headers=self.headers).text
            if result_get == "b''" or result_get == "":
                time.sleep(1)
            elif "Incorrect authentication credentials" in result_get:
                print("Incorrect authentication credentials")
                time_pause = 90
                print(time_pause)
                time.sleep(time_pause*60)
                return False, False
            elif ('Not Found' in result_get) or ('THROTTLED' in result_get):
                return False, False
            elif ('400 Bad Request' in result_get):
                print('check', result_get)
                return False, False
            elif 'IS_LADDER_SHARPE' in result_get:
                IS_LADDER_SHARPE = "PASS"
                LOW_SUB_UNIVERSE_SHARPE = "FAIL"
                if 'name":"IS_LADDER_SHARPE","result":"FAIL' in result_get:
                    IS_LADDER_SHARPE = "FAIL"
                elif 'name":"IS_LADDER_SHARPE","result":"PENDING':
                    IS_LADDER_SHARPE = "PENDING"
                if 'LOW_SUB_UNIVERSE_SHARPE","result":"PASS' in result_get:
                    LOW_SUB_UNIVERSE_SHARPE = "PASS"
                elif 'LOW_SUB_UNIVERSE_SHARPE","result":"PENDING' in result_get:
                    LOW_SUB_UNIVERSE_SHARPE = "PENDING"
                return LOW_SUB_UNIVERSE_SHARPE, IS_LADDER_SHARPE
            else:
                print('check?', result_get)
                done_get = True
        time.sleep(1)
        return True    
    
    def get_number_submit(self, dateSubmitted = '2022-12-22'):
        url = f"https://api.worldquantbrain.com/users/self/alphas?limit=10&offset=0&stage=OS&dateSubmitted%3E{dateSubmitted}T00:00:00-04:00&order=-dateCreated&type=REGULAR"
        payload = {}
        data = requests.request("GET", url, headers=self.headers, data=payload).json()
        results = data['results']
        for item in results:
            print(item['id'], "=====",item['regular']['code'], "===", item['regular']['operatorCount'], "===",  item['dateSubmitted'], "===",  item['dateCreated'])
            print('========')
        return int(data['count'])

    def save_name(self, alpha_id):
        reset_y = {
            "color": None,
            "name": alpha_id,
            "tags": [],
            "category": None,
            "regular": {
                "description": None
            },
        }
        # print(reset_y)
        requests.request("PATCH", f'https://api.worldquantbrain.com/alphas/{alpha_id}', headers=self.headers, data=json.dumps(reset_y))

    def reset_name(self, alpha_id):
        reset_y = {
            "color": None,
            "name": None,
            "tags": [],
            "category": None,
            "regular": {
                "description": None
            },
            'favorite':False,
            'hidden':False,
        }
        # print(reset_y)
        requests.request("PATCH", f'https://api.worldquantbrain.com/alphas/{alpha_id}', headers=self.headers, data=json.dumps(reset_y))

    def submit(self, alpha_id, k, favorite = False):
        done_post = False
        while not done_post:
            # result_post = str(self.session.post('https://api.worldquantbrain.com/alphas/'+ alpha_id +'/submit').content)
            result_post = requests.request("POST", 'https://api.worldquantbrain.com/alphas/' + alpha_id +'/submit', headers=self.headers, data={}).text
            if result_post == "b''" or result_post == "":
                # print('Success')
                time.sleep(5)
            elif '"FAIL"' in result_post:
                if '{"name":"REGULAR_SUBMISSION","result":"FAIL","limit":4,"value":4}' in result_post:
                    print(result_post)
                    sys.exit("Done 4")
                elif 'ALREADY_SUBMITTED' in result_post:
                    print('ALREADY_SUBMITTED ', alpha_id)
                    done_post = True
                else:
                    self.save(alpha_id, 'hide', favorite)
                    print('Hide FAIL POST', alpha_id)
                    print(result_post)
                    done_post = True
                    return -1
            elif "Incorrect authentication credentials" in result_post:
                    print("Incorrect authentication credentials")
                    time_pause = 90
                    print(time_pause)
                    time.sleep(time_pause*60)
                    done_post = True
            elif ('Not Found' in result_post) or ('PASS' in result_post) or ('THROTTLED' in result_post):                            
                # check done or not
                done_get = False
                while not done_get:
                    result_get = requests.request("GET", 'https://api.worldquantbrain.com/alphas/' + alpha_id, headers=self.headers, data={}).text
                    if result_get == "b''":
                        result_post = requests.request("POST", 'https://api.worldquantbrain.com/alphas/' + alpha_id +'/submit', headers=self.headers, data={}).text
                        print('post2?', result_post)
                        # print('Success')
                        if ('THROTTLED' in result_post):
                            time.sleep(20)
                        else:
                            time.sleep(10)
                    elif '"name":"REGULAR_SUBMISSION","result":"PENDING"' in result_get:
                        print("PENDING ", alpha_id)
                        result_post = requests.request("POST", 'https://api.worldquantbrain.com/alphas/' + alpha_id +'/submit', headers=self.headers, data={}).text
                        print('post2?', result_post)
                        return -1
                        # done_get = True
                    elif "Incorrect authentication credentials" in result_get:
                        print("Incorrect authentication credentials")
                        time_pause = 90
                        print(time_pause)
                        time.sleep(time_pause*60)
                        done_get = True
                    elif '"FAIL"' in result_get:
                        if '{"name":"REGULAR_SUBMISSION","result":"FAIL","limit":4,"value":4}' in result_get:
                            print(result_get)
                            sys.exit("Done 4")
                        else:    
                            self.save(alpha_id, 'hide', favorite)
                            print('Hide FAIL GET', alpha_id)
                            print(result_get)
                            done_get = True
                    elif '504 Gateway Time-out' in result_get:
                        done_get = True
                        print('Time-out')
                    elif 'PASS' in result_get: 
                        # k += 1
                        # print(k)
                        print(result_get, '??get')
                        print('Success')
                        # self.reset(alpha_id)
                        done_get = True
                    else:
                        print('get?', result_get)
                        done_get = True
                done_post = True
            elif ('400 Bad Request' in result_post):
                print('Resub', result_post)
                time.sleep(30)
                # done_post = True
            else:
                print('post?', result_post)
                done_post = True
        time.sleep(5)
        now = datetime.utcnow()-timedelta(hours=5)
        k = self.get_number_submit(now.strftime("%Y-%m-%d"))
        print('Number submit', k)
        return int(k)

    def submit_super(self, alpha_id, k, favorite = False, combo_des = "", selection_des = ""):
        body = {
            "color": None,
            "name": None,
            "tags": [],
            "category": None,
            "regular": {
                "description": None
            },
            "combo": {
                "description": combo_des
            },
            "selection": {
                "description": selection_des
            }
        }
        
        result = requests.request("PATCH", 'https://api.worldquantbrain.com/alphas/' + alpha_id, headers=self.headers, data=json.dumps(body)).text

        print(result)
        print('Next')
        done_post = False
        while not done_post:
            # result_post = str(self.session.post('https://api.worldquantbrain.com/alphas/'+ alpha_id +'/submit').content)

            result_post = requests.request("POST", 'https://api.worldquantbrain.com/alphas/' + alpha_id +'/submit', headers=self.headers, data={}).text
            if result_post == "b''" or result_post == "":
                # print('Success')
                time.sleep(10)
            elif '"FAIL"' in result_post:
                if '{"name":"SUPER_SUBMISSION","result":"FAIL"' in result_post:
                    print(result_post)
                    sys.exit("Done")
                else:
                    self.save(alpha_id, 'hide', favorite)
                    print('Hide FAIL POST', alpha_id)
                    print(result_post)
                    done_post = True
            elif "Incorrect authentication credentials" in result_post:
                print("Incorrect authentication credentials")
                sys.exit("Bye")
            elif ('Not Found' in result_post) or ('PASS' in result_post) or ('THROTTLED' in result_post):                            
                # check done or not
                done_get = False
                while not done_get:
                    result_get = requests.request("GET", 'https://api.worldquantbrain.com/alphas/' + alpha_id, headers=self.headers, data={}).text
                    
                    if result_get == "b''" or result_get == "":
                        result_post = requests.request("POST", 'https://api.worldquantbrain.com/alphas/' + alpha_id, headers=self.headers, data={}).text
                        print('post2?', result_post)
                        # print('Success')
                        if ('THROTTLED' in result_post):
                            time.sleep(20)
                        else:
                            time.sleep(10)
                    elif "Incorrect authentication credentials" in result_get:
                        print("Incorrect authentication credentials")
                        sys.exit("Bye")
                    elif '"FAIL"' in result_get:
                        if '{"name":"SUPER_SUBMISSION","result"' in result_get:
                            print(result_get)
                            sys.exit("Done")
                        else:    
                            self.save(alpha_id, 'hide', favorite)
                            print('Hide FAIL GET', alpha_id)
                            print(result_get)
                            done_get = True
                    elif '504 Gateway Time-out' in result_get:
                        done_get = True
                        print('Time-out')
                    elif 'PASS' in result_get: 
                        # k += 1
                        # print(k)
                        print('Success')
                        # self.reset(alpha_id)
                        done_get = True                                   
                    else:
                        print('get?', result_get)
                        done_get = True
                done_post = True
            elif ('400 Bad Request' in result_post):
                print('Resub', result_post)
                # time.sleep(10)
                done_post = True
            else:
                print('post?', result_post)
                done_post = True
        time.sleep(10)
        return 1
# Stimulation
import requests
from typing import Dict, Any

class Simulate:
    def __init__(self, universe = 'TOP3000', region= 'USA',  neutralization="MARKET",decay=0,delay=1):
        self.headers = headers
        self.universe = universe
        self.region = region
        self.neutralization = neutralization
        self.delay =delay
        self.decay =decay
        self.url = "https://api.worldquantbrain.com/simulations"


    def _get_regular_code(self, code):
        alpha = {
                    "type": "REGULAR",
                    "settings": {
                        "nanHandling": "OFF",
                        "instrumentType": "EQUITY",
                        "delay": self.delay,
                        "universe": self.universe,
                        "truncation": 0.08,
                        "unitHandling": "VERIFY",
                        "pasteurization": "ON",
                        "region": self.region,
                        "language": "FASTEXPR",
                        "decay": self.decay,
                        "neutralization": self.neutralization,
                        "visualization": False
                        },
                    "regular": code
                }
        return alpha     

    def _get_super_code(self, combo, selection, selectionLimit = 10):
        # selectionLimit = random.randint(15,20)
        alpha = {
                    "type":"SUPER",
                    "settings":{
                        "nanHandling":"OFF",
                        "instrumentType":"EQUITY",
                        "delay":1,
                        "universe": self.universe,
                        "truncation":0.08,
                        "unitHandling":"VERIFY",
                        "selectionLimit":selectionLimit,
                        "selectionHandling":"NON_ZERO",
                        "pasteurization":"ON",
                        "region": self.region,
                        "language":"FASTEXPR",
                        "decay": self.decay,
                        "neutralization": self.neutralization,
                        "visualization": False
                    },
                    "combo": combo,
                    "selection": selection
                }
        return alpha
    
    def _check_simulation_progress(self, simulation_progress_url):
        while True:
            simulation_progress = requests.get(simulation_progress_url, headers=self.headers)
            if simulation_progress.headers.get("Retry-After", 0) == 0:
                break
            time.sleep(float(simulation_progress.headers["Retry-After"]))
        return simulation_progress.json()
    
    def _simulate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(self.url, headers=self.headers, json=payload)
        result = response.text
        print(result)
        if "SIMULATION_LIMIT_EXCEEDED" in result:
            print("Wait")
            time.sleep(10)
        elif "Incorrect authentication credentials" in result:
            print("Incorrect authentication credentials")
            time_pause = random.randint(45, 75)
            print(time_pause)
            time.sleep(time_pause*60)
            return False
        else:
            print('Run')
        simulation_progress_url = response.headers['Location']
        simulation_progress = self._check_simulation_progress(simulation_progress_url)
        
        alpha = simulation_progress["alpha"]
        response = requests.get(f"https://api.worldquantbrain.com/alphas/{alpha}", headers=self.headers)
        result = response.text
        print(result)
        
        return response.json() 


    def regular(self, alpha: str,time_sleep=10) :
        alpha_code = self._get_regular_code(code=alpha)
        return self._simulate(payload=alpha_code)

    def super(self, combo, selection, selectionLimit = 10):
        alpha_code = self._get_super_code(combo, selection, selectionLimit)
        return self._simulate(payload=alpha_code)


# Pnl calculation
class Pnl():
    def __init__(self, pnl):
        self.pnl = pnl

        max_pnl = 100000000
        num_ser = len(pnl)
        step = max_pnl/num_ser
        self.pnl_stand =np.arange(0,max_pnl,step)        

    def get_corr(self):
        cor_res = self.pnl.corrwith(pd.DataFrame(self.pnl_stand)[0])
        return cor_res
    
    def get_r_abs(self):
        r_abs_res = abs((self.pnl).sum()/(self.pnl_stand).sum())
        return r_abs_res
    
    def summary(self):
        res = pd.concat([pd.DataFrame(self.get_corr(),columns=["correlation"]).T,pd.DataFrame(self.get_r_abs(),columns=["r_abs"]).T])
        return res.T
    
# regular
def get_code(x):
    code = x["regular"]["code"]
    return code

def get_raw(x):
    text = x['code']
    # Kiểm tra xem có merge alpha không 
    count_negative_raw_alpha = text.count('-')
    count_positive_raw_alpha = text.count('+')
    if text[0] == '-':
        count_raw_alpha = count_positive_raw_alpha + count_negative_raw_alpha
    else:
        count_raw_alpha = count_positive_raw_alpha + count_negative_raw_alpha + 1    
    return count_raw_alpha
# is
def get_fitness(x):
    fit = x["is"]["fitness"]
    return fit

def get_sharpe(x):
    sharpe = x["is"]["sharpe"]
    return sharpe

def get_turnover(x):
    turnover = x["is"]["turnover"]
    return turnover

def get_longCount(x):
    fit = x["is"]["longCount"]
    return fit

def get_shortCount(x):
    sharpe = x["is"]["shortCount"]
    return sharpe

def get_concentrated_weight(x):
    sharpe = x["is"]["checks"][4]['result']
    return sharpe

def count_pass(x):
    my_list = x["is"]["checks"]
    count = [d for d in my_list if d.get('result') == 'PASS']  # filter list with comprehension
    count = len(count)  # count the number of items in the filtered list
    return count  


def count_fail(x):
    my_list = x["is"]["checks"]
    count = [d for d in my_list if d.get('result') == 'FAIL']  # filter list with comprehension
    count = len(count)  # count the number of items in the filtered list
    return count 

def get_result_theme(df):
    for i in df['is']['checks']:
        if i['name']=='MATCHES_THEMES':
            return i['result']
# Setting
def get_neutralization(x):
    neu = x['settings']['neutralization']
    return neu

def get_region(x):
    neu = x['settings']['region']
    return neu

def get_universe(x):
    neu = x['settings']['universe']
    return neu


def extract_form(formula, columns):
    # Find all column names in the formula
    column_names = re.findall(r'\b(' + '|'.join(columns) + r')\b', formula)
    
    # Replace the column names with f1, f2, etc.
    for i, column_name in enumerate(column_names):
        formula = formula.replace(column_name, f"param{i+1}")
    
    # Return the modified formula
    return formula 

def extract_operator(s, operators_list):
    indices = []
    for keyword in s:
        indices.append(operators_list.index(keyword))
    return indices

def extract_field(s, field_list):
    indices = []
    for keyword in s:
        indices.append(field_list.index(keyword))
    return indices

def convert_div(a):
    # Define a regex pattern to match any expression of the form "func(X/Y)"
    pattern = r'(\w+)\s*\(\s*([(),/\w\s]+)\s*/\s*([(),/\w\s]+)\s*\)'

    # Use regex to replace any matches of the pattern in the input string
    a = re.sub(pattern, lambda match: f"{match.group(1)}(divide({match.group(2)},{match.group(3)}))", a)

    return a

def convert_reverse(input_str):
    return f"reverse({input_str.replace('-', '')})"

def encode_alpha(expression,l_oper,field,inner_group):
    # Define regular expressions for operators and parameters
    operator_regex = r'\b(' + '|'.join(l_oper) + r')\b'
    param_regex = r'\b(' + '|'.join(field) + r')\b'
    ingroup_regex = r'\b(' + '|'.join(inner_group) + r')\b'
    
    # Find all operator and parameter matches in the expression
    operator_matches = re.findall(operator_regex, expression)
    param_matches = re.findall(param_regex, expression)
    ingroup_matches= re.findall(ingroup_regex,expression)

    # Convert operator matches to integer indices
    operator_indices = [l_oper.index(op[0]) for op in operator_matches]
    
    # Convert parameter matches to integer indices
    param_indices = [field.index(param) for param in param_matches]
    
    ingroup_indices = [inner_group.index(ig) for ig in ingroup_matches]
    return operator_indices, param_indices, ingroup_indices
    
# delete cache
import shutil

def delete_pycache(folder):
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            if dir == '__pycache__':
                shutil.rmtree(os.path.join(root, dir))

# Save to file
def save(a, path):
    header = not os.path.exists(path)
    df = a.to_csv(path, mode="a", header=header, index=False)

