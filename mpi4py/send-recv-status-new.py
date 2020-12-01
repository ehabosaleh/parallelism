from mpi4py import MPI
import numpy as np
import random as ra
import datetime
import time

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
s=MPI.Status()


def do_something_else(data,d,rank):
  if(rank==0):
    print("Core {} sent message to Core {} at time:{}".format(rank,d,data.time()))
  else:
    print("Core {} recieved message from Core {} at time:{}, with tag {}.".format(rank,d.Get_source(),data.time(),d.Get_tag()))
    
   
   
if rank == 0:
    
    any_tag=ra.randint(0,10)
    data_1=datetime.datetime.now()
    for i in range(1,size):
      comm.send(data_1, dest=i, tag=any_tag)
      do_something_else(data_1,i,rank)
else:
    
    comm.recv(source=MPI.ANY_SOURCE,tag=MPI.ANY_TAG,status=s)
    data_2=datetime.datetime.now()
    do_something_else(data_2,s,rank)
    


