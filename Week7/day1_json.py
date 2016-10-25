import json

l = [None, 2, "Sam", 4]

string_list = str(l)

print(string_list)

json_list = json.dumps(l)

print(json_list)

print (json.dumps({"joel": 'codes'}))
