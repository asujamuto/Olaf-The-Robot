from models import Conversation

# Class for easy and fast database interpreting without need of getting out from programming enviroment
"""
class DataBase_Reader():
    def __init__(self):
        db = Conversation()
        self.db = db

    def __str__(self):
        return [i for i in self.db]

if __name__ == '__main__':
    db_reader = DataBase_Reader()
"""
db = Conversation()
print(db)