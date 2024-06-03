import yaml
import os
#print(os.getcwd())

with open(r'Project/Medplans_Srujan/test_schema.yaml', 'r') as f:
    schema = yaml.safe_load(f)


ddl_statement = f"CREATE TABLE {table_name} {column_name} {datatype} {contraints}"


