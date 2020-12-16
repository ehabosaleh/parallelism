from  multiprocessing import Process, Lock, Value
import time
def add_a(total,n):
   for i in range(n):
       time.sleep(0.001)
       total+=1
   return total 
def sub_a(total,n):
   for i in range(n):
       time.sleep(0.001)
       total-=1
   return total 

if __name__=='__main__':
   total =500
   n=500
   print(total)
   total=add_a(total,n)
   print(total)
   total=sub_a(total,n)
   print(total)
