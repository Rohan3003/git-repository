import json
# user is dictionary
user = {"name" : "Rohan", "email" : "rohan.srivastwa00@gmail.com", "age" : 28}
serialized_user = json.dumps(user)

print(user)
print("user datatype is : ",type(user))
print(serialized_user)
print("serialized_user datatype is : ",type(serialized_user))
