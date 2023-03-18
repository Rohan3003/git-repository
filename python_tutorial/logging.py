import logging
logging.basicConfig(filename='demo.log',level=logging.DEBUG)
#logging.disable()


def nameCheck(name):
    if len(name) <= 2:
        logging.debug.debug(" Checking the name length....")
        return 'Invalid Name!'
    elif name.isspace():
        logging.debug.debug(" Checking if name is a space...")
        return 'Invalid Name!'
    elif name.isalpha():
        logging.debug(" Checking if name is alphabet")
        return 'Name is valid!'
    elif name.replace(' ', '').isalpha():
        logging.debug(" Checking for Full name with whitespaces")
        return 'Name is valid'
    else:
        logging.debug(" Failed all check")
        return 'Invalid name!'
    
print(nameCheck('Rohan'))