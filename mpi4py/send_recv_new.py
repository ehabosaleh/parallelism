from mpi4py import MPI
import numpy as np
import random as ra
import datetime
import time

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
s=MPI.Status()
any_dest=ra.randint(1,size-1)
#any_dest=3

def do_something_else(data,d,rank):
  if(rank==0):
    print("Core {} sent message to Core {} at time:{}".format(rank,d,data.time()))
  else:
    print("Core {} recieved message from Core {} at time: {}".format(rank,d,data.time())) 
   
if rank == 0:
    print(any_dest)
    any_tag=ra.randint(0,10)
    data_1=datetime.datetime.now()
    req_1=comm.send(data_1,dest=any_dest, tag=any_tag)
    do_something_else(data_1,any_dest,rank)
   
   
    
else:
    req_2=comm.irecv(source=MPI.ANY_SOURCE,tag=MPI.ANY_TAG)
    req_2.wait()
    data_2=datetime.datetime.now()               
    do_something_else(data_2,0,rank)
    time.sleep(10)
    comm.Abort(1)
    


