import sqlite3
import pandas as pd

# Class for easy and fast database interpreting without need of getting out from programming enviroment

class DataBase_Reader():
    def __init__(self, *path):
        try:
            db = sqlite3.connect(path)
        except:
            db = sqlite3.connect("./databases/sqlite3/message_data.db")
        
        self.df = pd.read_sql('select *  from conversation_data', db)
        
    
    def __str__(self):
        return str(self.df)

if __name__ == '__main__':
    db_reader = DataBase_Reader()
    print(db_reader)