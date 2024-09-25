 # working with json as a string 
import json
# import ujson
cust: str = '''
{
"customers":[
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
                }
            ]
}
'''
customers : dict = json.loads(cust) # json string value is converted to dictionary
# print(customers)
# print(type(customers))
# print(customers['customer'])

for customer in customers['customers']:
    print(f"{customer['Name']} - {customer['Occupation']}")

temp_cust: dict = {
    "id" : 3,
    'Name' : 'Zippy',
    'City' : None,
    'Country' : None,
    'Occupation' : 'Puppet'
}

# append a dictionary
customers['customers'].append(temp_cust)
print(customers)
print("-----"*30)

# to convert dictionary to string
# notice all single quotes converted to double quotes and none to null value
json_payload = json.dumps(customers, indent= 2)
print(json_payload)
print(type(json_payload))