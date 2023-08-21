## code without threading
# import time
# from datetime import datetime
# def do_this():
#     print('Starting this')
#     time.sleep(2)
#     print('Did this!')

# def do_that():
#     print('Stating that')
#     time.sleep(3)
#     print('Did that!')

# start_time = datetime.now()
# do_this()
# do_that()
# end_time = datetime.now()
# print(f'Time taken to run the code : {end_time-start_time}')


# The same code with threading 
# need to check threading module 
import time
from datetime import datetime
from threading import Thread

def do_this():
    print('Starting this')
    time.sleep(5)
    print('Did this!')

def do_that():
    print('Stating that')
    time.sleep(8)
    print('Did that!')

start_time = datetime.now()
# do_this()
# do_that()
t1 = Thread(target = do_this())
t1.start()

t2 = Thread(target = do_that())
t2.start()

end_time = datetime.now()
print(f'Time taken to run the code : {end_time-start_time}')



