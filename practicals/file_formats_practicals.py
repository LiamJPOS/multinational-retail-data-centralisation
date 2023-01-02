
import json 
'''
    Open a text editor and create a JSON file which contains
    a key called "dates_visited", which is a list of strings of dates in ISO format (look it up)
    a key called "user_id", which is a string UUID4 (again, look it up and make sure you know what it is)
    a key called "basket", which contains a list of dictionaries
        Each item in the basket should have 3 keys
            "price", which is a float
            "id", which is a UUID4 ID
            "name", which is a string
            
'''
x = {'dates_visited' : ['2022-12-28', '2023-01-02'],
     'user_id' : 'b7006899-b5b5-41df-b18f-afdcc0c6b2fe',
     'basket' : [{'price' : 38.25,
                  'id' : '9037be05-5901-4700-bd82-237b33f683bd', 
                  'name' : 'Gianni Feraud oversized checked mac coat in grey'}, 
                 {'price' : 44.00,
                  'id' : '453cb74f-cbc6-4e5f-8690-3e1bd29ab8da', 
                  'name' : 'ASOS DESIGN oversized wool mix overcoat in grey'}]}

with open('json_practical.json', mode = 'w') as f:
    json.dump(x, f)





