import csv
import pandas as pd
import json


#that function saves files to dictionary, than saves it to intents, and lastly it saves it to json
def save_to_json(tags, patterns, responses, path, type_of_dict):
    
    intents = []
    for i_tag in range(len(tags)):
        dictionary = {
                "tag": tags[i_tag],
                "patterns":[i for i in patterns[i_tag]],
                "responses":[]
                }   
        
        dictionary_delete_double = {
                "tag": tags[i_tag],
                "patterns":[i for i in patterns[i_tag]],
                "responses":[j for j in responses[i_tag]]
            }
        if type_of_dict == 0:
            dictionary = dictionary 

        elif type_of_dict == 1:
            dictionary = dictionary_delete_double
        
        
        intents.append(dictionary)
        
    # Serializing json
    final_data = {
        "intents": intents
    }
    
    outfile = open(path, "w")
    json_object = json.dump(final_data, outfile, indent=4)
    
    outfile.close()

def find_every_pattern(data):
    tags = []
    patterns = []
    same_tags = []
    for i in data.itertuples():
        if i[2][10:] not in tags:
            tags.append(i[2][10:])
            group_name = i[2]
            for t in data.itertuples():
                if t[2] == group_name:
                    same_tags.append(t[1])
                else:
                    continue
            
            patterns.append(same_tags)
            same_tags = []
        
        if i[2] in tags:
            continue
        else:
            continue
    return tags, patterns


if  __name__ == "__main__":
    df = pd.read_csv('./Small_talk_Intent.csv')
    df = pd.DataFrame(df)
    path = "databases/clean.json"
    tags, patterns = find_every_pattern(df)
    save_to_json(tags, patterns, responses, path, type_of_dict)

