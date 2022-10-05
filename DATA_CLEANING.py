import csv
import pandas as pd
import json


df = pd.read_csv('./Small_talk_Intent.csv')
df = pd.DataFrame(df)



#that function saves files to dictionary, than saves it to intents, and lastly it saves it to json
def save_to_json(tags, patterns):

    intents = []
    for i_tag in range(len(tags)):
        dictionary = {
            "tag": tags[i_tag],
            "patterns":[i for i in patterns[i_tag]],
            "responses":[]
        }
        intents.append(dictionary)
    
    # Serializing json
    final_data = {
        "intents": intents
    }
    json_object = json.dumps(final_data, indent=4)
    with open("chatbot_data.json", "w") as outfile:
        outfile.write(json_object)


#data.itertuples()[1] = utters
#data.itertuples()[2] = intent
#module of converting data to chatbot 

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
    tags, patterns = find_every_pattern(df)
    save_to_json(tags, patterns)

