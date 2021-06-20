import time
import pandas as pd
from datetime import datetime,timedelta
from github import Github
import matplotlib.pyplot as plt
class sumit_repl:
    def __init__(self):
        self.__token=None
        self.__dataset={}
        self.__repo_list=None
        self.__g=None
        self.__df=None
        self.__date=None
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
    def set_date(self,days):
        self.__days=days
        
    def activity_count(self):
        start_date = (datetime.today()-timedelta(days=self.__days))
        end_date = datetime.today()
        t1=time.time()
        self.__dataset={}
        for r in self.__repo_list:
            repo = self.__g.get_user().get_repo(r)
            cnt=0
#             print(repo.name)
            for i in repo.get_commits(since=start_date,until=end_date):
                if i.author.login == self.__g.get_user().login:
                    datetimeobj=datetime.strptime(i.last_modified[5:16],"%d %b %Y")
                    date=datetimeobj.strftime("%Y%m%d")
                    if date in self.__dataset:
                        self.__dataset[date] += 1
                    else:
                        self.__dataset[date]=1
        data_df = {'date':list(self.__dataset.keys()),'commits':list(self.__dataset.values())}
        df = pd.DataFrame(data_df,columns=['date','commits'])
        df['date']=pd.to_datetime(df['date'])
        df = df.sort_values(by="date")
        convert_dict = {'date': str}
        filtered_dates = df.astype(convert_dict)
        self.__df = filtered_dates.to_numpy().tolist()
        t2=time.time()
        print(t2-t1)
        
    def get_dataset(self):
        return self.__dataset
    def get_data(self):
        return self.__df

        
        
    
        
        
    
# obj = sumit_repl()
# obj.set_token("")
# obj.initiate()
# obj.repo_list()
# obj.set_date(60)
# obj.activity_count()
# obj.get_data()
        
        
    
        
        
    