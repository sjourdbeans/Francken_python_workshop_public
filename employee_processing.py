import pandas as pd
from employee import Employee

class Processing:
    def __init__(self,filename):
        self.path=f"{filename}"
        self.data=pd.read_csv(self.path)
        self.name=None
        self.birthday=None
        self.id=None
    
    def employee_list(self):
        pass

