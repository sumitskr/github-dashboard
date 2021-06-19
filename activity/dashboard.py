import time
import pandas as pd
from datetime import datetime,timedelta
import collections
from github import Github
import matplotlib.pyplot as plt
class sumit_repl:
    def __init__(self):
        self.__token=None
        self.__dataset={}
        self.__repo_list=None
        self.__g=None
        self.__df=None
        self.__filtered_data=None
    def set_token(self,token):
        self.__token=token
    def get_token(self):
        return self.__token
    def repo_list(self):
        l=[]
        for i in self.__g.get_user().get_repos():
            l.append(i.name)
        self.__repo_list=l
#         print(self.__repo_list)
    def initiate(self):
        self.__g = Github(self.__token)
        
    def activity_count(self):
        t1=time.time()
        for r in self.__repo_list:
            repo = self.__g.get_user().get_repo(r)
            cnt=0
            for i in repo.get_events():
                if i.actor.login == self.__g.get_user().login:
                    date = i.created_at.strftime("%Y%m%d")
                    if date in self.__dataset:
                        self.__dataset[date] += 1
                    else:
                        self.__dataset[date]=1
        t2=time.time()
        data = self.__dataset
        data_df = {'date':list(data.keys()),'commits':list(data.values())}
        df = pd.DataFrame(data_df,columns=['date','commits'])
        df['date']=pd.to_datetime(df['date'])
        df = df.sort_values(by="date")
        self.__df = df
        print(t2-t1)
    def get_dataset(self):
        return self.__dataset
    def get_data(self):
        return self.__df
    def filtered_data(self):
        start_date = (datetime.today()-timedelta(days=30)).strftime("%Y-%m-%d")
        end_date = datetime.today().strftime("%Y-%m-%d")

        after_start_date = self.__df["date"] >= start_date
        before_end_date = self.__df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        filtered_dates = self.__df.loc[between_two_dates]
        convert_dict = {'date': str}
        filtered_dates = filtered_dates.astype(convert_dict)
        self.__filtered_data = filtered_dates.to_numpy().tolist()
    def get_filtered_data(self):
        return self.__filtered_data
        
        

# obj = sumit_repl()
# obj.set_token("ds")
# obj.initiate()
# obj.repo_list()
# obj.activity_count()
# obj.filtered_data()
# print(obj.get_filtered_data())

        
        
    
