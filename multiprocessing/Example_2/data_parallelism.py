import time
from multiprocessing import Pool
import numpy as np
def square(x):
   return x**2
if __name__=='__main__':
   numbers =np.linspace(1,10000000)
   p=Pool(4) 
   t1=time.process_time()  
   print(p.map(square,numbers))
   t2=time.process_time()
   p.close()
   p.join() 

   print("executing time when using pool is: {}".format(t2-t1))
   t1=time.process_time()
   for number in numbers:
       print(square(number))
   t2=time.process_time()
   print("executing time without Pool (serial execution) is: {}".format(t2-t1))
