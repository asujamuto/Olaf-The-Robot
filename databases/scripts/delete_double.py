import json
from data_cleaning import save_to_json

class Data_Cleaner():
    def __init__(self, database):

        with open(database, "r") as f:
            self.data = json.load(f)

    def delete_double(self):

        cleaned_patterns = []
        responses = []
        tags = []

        #for each word in 'intents'
        for i in self.data['intents']:
     
            lower_patterns = [smaller.lower() for smaller in i['patterns']]
            
            #removing duplicated words
            res = list(set(lower_patterns))
            print(res[0])
            #appending answers and already list with removed duplicated words
            tags.append(i['tag'])
            responses.append(i['responses'])
            cleaned_patterns.append(res)

        return tags, cleaned_patterns, responses


if  __name__ == "__main__":
    data_clean = Data_Cleaner("../important-no-more/chatbot_data_pl.json")
    tags, cleaned_patterns, responses = data_clean.delete_double()

    path_for_saving_file = "/home/pete/Coding/Python/Artificial_Inteligence/chatbot/databases/cleaned_database.json"

    # givinig name of arguments to not miss any
    # type_of_dict can be 0 or 1: it depends if data are without responses or with
    # generally speaking i has used 0 because there was different data to convert
    save_to_json(tags = tags, patterns = cleaned_patterns, responses = responses, path=path_for_saving_file, type_of_dict=1)
