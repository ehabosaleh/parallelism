import os
from multiprocessing import Process, current_process
def square(number):
    result=number**2
    process_id=os.getpid()
    print("process ID  is {}".format(process_id))
    print("process name is {}".format(current_process().name))
    print("the number {} squares to {}".format(number,result))

if __name__=='__main__':
    numbers=[1,2,3,4]
    processes=[]
   
    for num in numbers:
        process=Process(target=square,args=(num,))
        processes.append(process)
        process.start()


