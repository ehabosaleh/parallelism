import os
import time
from multiprocessing import Process, current_process
def square(numbers):
    for number in numbers:
       time.sleep(0.5)
       result=number**2
       process_id=os.getpid()
       print("process ID  is {}".format(process_id)) 
       print("the number {} squares to {}".format(number,result))

if __name__=='__main__':
    numbers= range(100)
    processes=[]
   
    for num in range(50):
        process=Process(target=square,args=(numbers,))
        processes.append(process)
        process.start()
        process.join()

print("Multiprocesing complete")

