import sys
print('we are learning about command-line arguments in python')
print('sys.argv is a list which contains : ', sys.argv)
first_arg = sys.argv[0]
second_arg = sys.argv[1]
print('The first element is the name of script :', first_arg)
print('The second element is the second argument passed in command line (here 117):', second_arg)