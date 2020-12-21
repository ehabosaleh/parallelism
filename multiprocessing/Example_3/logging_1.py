from  multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger
import logging
import time
def add(total,n,lock):
   for i in range(n):
       time.sleep(0.001)
       lock.acquire()
       total.value+=1
       lock.release()

def sub(total,n,lock):
   for i in range(n):
       time.sleep(0.001)
       lock.acquire()
       total.value-=1
       lock.release()

if __name__=='__main__':

   total=Value('i',500)
   n=500
   lock1=Lock()
   logging.basicConfig(filename="log_report.log",level= logging.DEBUG,format="%(asctime)s | %(threadName)s | %(name)s | %(message)s")

   lock2=lock1
   add_process=Process(target=add,args=(total,n,lock1))
   sub_process=Process(target=sub,args=(total,n,lock2))
   add_process.start()
   sub_process.start()
   add_process.join()
   sub_process.join()
   logging.warning("total value is: {}".format(total.value))
   
