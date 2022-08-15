import json

list_cenz = []

#, encoding='utf-8'
with open('cenz_dict.txt') as str_cenz_file:
    for i in str_cenz_file:
        #print (i.split('\n')[0])
        #print (i.lower())
        if i !='':
            list_cenz.append(i.lower().split('\n')[0])

with open ('cenz_dict.json', 'w', encoding='utf-8') as json_items:
    json.dump(list_cenz, json_items)

