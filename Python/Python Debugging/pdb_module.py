# with using pdb
import pdb

def my_function(a,b):
    pdb.set_trace()
    result = a/b
    return result

my_function(10,0)