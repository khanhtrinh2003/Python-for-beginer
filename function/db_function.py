
import pandas as pd
import sqlite3

class My_db():
    def __init__(self,path) -> None:
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()
        
    def get_database_table(self):
        # Execute the query to get the table names
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") # replace with appropriate query for your database

        # Fetch all the table names
        tables = self.cursor.fetchall()

        # Print the table names
        for table in tables:
            print(table[0])

        # Commit the changes
        self.db.commit()

    def delete_database_table(self,name):
        # Execute the query to delete the table
        self.cursor.execute(f"DROP TABLE IF EXISTS {name};") # replace "table_name" with the name of the table you want to delete

        # Commit the changes
        self.db.commit()

    def get_shape_database(self):
        # Get the table names
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()

        # Iterate through the tables and get their shape
        for table in tables:
            table_name = table[0]
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            num_rows = self.cursor.fetchone()[0]
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            num_cols = len(self.cursor.fetchall())
            print(f"{table_name}: {num_rows} rows, {num_cols} columns")

        
    def read_database_tabe(self,table):
        return pd.read_sql(f"SELECT * FROM {table}",self.db)

    def save_database_tabe(self,df,table,mode="append"):
        df.to_sql(f"{table}",con=self.db,if_exists=mode,index=False)    
    
    def get_data_US(self,theme,coverage=50):
        df = self.read_database_tabe('datasets')
        operators = ['vec_avg(param)', 'vec_choose(param,nth=0)', 'vec_ir(param)', 'vec_kurtosis(param)', 'vec_max(param)', 'vec_min(param)', 'vec_norm(param)', 'vec_percentage(param,percentage=0.5)', 'vec_powersum(param,constant=2)', 'vec_range(param)', 'vec_skewness(param)', 'vec_stddev(param)', 'vec_sum(param)']
        df1=df[(df['dataset'].isin(theme)) & (df['coverage_USA']>=coverage) & (df['delay']==1)]
        vec= df1[df1['type']=='matrix']['field'].to_list()
        matri = df1[df1['type']!='matrix']['field'].to_list()
        # result=[]
        # result.extend(matri)
        # for fi in vec:
        #     for op in operators:
        #         result.append(op.replace('param',fi))
        return df1['field'].to_list()
    
    def get_data_CHN(self,theme,coverage=50):
        df = self.read_database_tabe('datasets')
        operators = ['vec_avg(param)', 'vec_choose(param,nth=0)', 'vec_ir(param)', 'vec_kurtosis(param)', 'vec_max(param)', 'vec_min(param)', 'vec_norm(param)', 'vec_percentage(param,percentage=0.5)', 'vec_powersum(param,constant=2)', 'vec_range(param)', 'vec_skewness(param)', 'vec_stddev(param)', 'vec_sum(param)']
        df1=df[(df['dataset'].isin(theme)) & (df['coverage_CHN']>=coverage) & (df['delay']==1)]
        vec= df1[df1['type']=='matrix']['field'].to_list()
        matri = df1[df1['type']!='matrix']['field'].to_list()
        # result=[]
        # result.extend(matri)
        # for fi in vec:
        #     for op in operators:
        #         result.append(op.replace('param',fi))
        return df1['field'].to_list()