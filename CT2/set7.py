from threading import Thread, Semaphore
from time import sleep
import random
import sqlite3

# create or connect to a db
conn1 = sqlite3.connect('./Database/database1.db')
conn2 = sqlite3.connect('./Database/database2.db')
conn3 = sqlite3.connect('./Database/database3.db')



def runDB(self, conn, i):
    print('Thread number: ', i)
    c = conn.cursor()
    # create a table
    c.execute("""CREATE TABLE details (
        fname text,
        lname text,
        id integer
    )""")
    c.execute("INSERT INTO details VALUES (:fname, :lname, :id)", {
        'fname': 'Tanisha',
        'lname': 'Bisht',
        'id': 2409
    })
    c.execute("SELECT * FROM details")
    print('The values stored in the database are: ')
    print(c.fetchall())
    conn.commit()
    conn.close()


t1 = Thread(target=runDB,args=[conn1, 1],daemon=True)
t2 = Thread(target=runDB,args=[conn2, 2],daemon=True)
t3 = Thread(target=runDB,args=[conn3, 3],daemon=True)
# t1 = RunDB(conn1, 1)
# t2 = RunDB(conn2, 2)
# t3 = RunDB(conn3, 3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print('MAIN THREAD BYE!')






# Simple PRODUCER CONSUMER: Demonstrates queue and event with locks

# Imports
# import random
# import threading
# import multiprocessing
# import logging
# from threading import Thread
# from queue import Queue
# import time
# logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)



# # Functions
# def display(msg):
#     threadname = threading.current_thread().name
#     processname = multiprocessing.current_process().name
#     logging.info(f'{processname}\\{threadname}: {msg}')



# # Producer
# def create_work(work,finished,max):
#     finished.put(False)
#     for x in range(max):
#         v = random.randint(1,100)
#         work.put(v)
#         display(f'Producing {x}:{v}')
#     finished.put(True)
#     display('finished')



# # Consumer 
# def perform_work(work,finished):
#     counter = 0
#     while True:
#         if not work.empty():
#             v = work.get()
#             display(f'Consuming {counter}: {v}')
#             counter += 1
#         else:
#             q = finished.get()
#             if q == True:
#                 break
#         display('finished')



# #Main function
# def main():
#     max = 50
#     work = Queue()
#     finished = Queue()

#     producer = Thread(target=create_work,args=[work,finished,max],daemon=True)
#     consumer = Thread(target=perform_work,args=[work,finished],daemon=True)

#     producer.start()
#     consumer.start()

#     producer.join()
#     display('PRODUCER HAS FINISHED')
#     consumer.join()
#     display('CONSUMER HAS FINISHED')

#     display('FINISHED')



# if __name__ == "__main__":
#     main()