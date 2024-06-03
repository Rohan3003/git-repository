import json

def get_json_values(path:str):
    open_file = open(path)
    json_content = json.load(open_file)
    return json_content
