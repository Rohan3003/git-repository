# JSON WORKING WITH FILES
# using context manager to create a json file
import json
customers : str = '''
{"customers":[
                {
                    "id" : 1,
                    "Name": "Mary Poppins",
                    "City": "London",
                    "Country": "UK",
                    "Occupation":"Nanny"
                },
                {
                    "id" : 2,
                    "Name": "Bruce Banner",
                    "City": null,
                    "Country": null,
                    "Occupation":"Scientist"
                },
                {
                    "id" : 3,
                    "Name" : "Zippy",
                    "City" : null,
                    "Country" : null,
                    "Occupation" : "Puppet"
                }
            ]
}
'''
json_dict : dict = json.loads(customers)
# print(json_dict)
# print("-----"*30)

json_path = 'D:/Work/Codes/git repository/Data Enginerering/working with json/sample_json.json'

# write json_dictionary to files using context manager
with open(json_path, mode='w') as json_file:
    json.dump(json_dict, json_file, indent=4)


# to laod json_file data to console
with open(json_path, mode='r') as json_file:
    data = json.load(json_file)
    json_data = json.dumps(data)

print(json_data)