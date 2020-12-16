from  multiprocessing import Process, Lock, Value
import time
def add(total,n):
   for i in range(n):
       time.sleep(0.01)
       total.value+=1
  
def sub(total,n):
   for i in range(n):
       time.sleep(0.01)
       total.value-=1
    

if __name__=='__main__':
  
   total=Value('i',500)
   n=500
   add_process=Process(target=add,args=(total,n))
   sub_process=Process(target=sub,args=(total,n))
   add_process.start()
   sub_process.start()
   add_process.join()
   sub_process.join()
   print(total.value)
