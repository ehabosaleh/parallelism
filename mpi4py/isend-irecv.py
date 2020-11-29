from mpi4py import MPI
import numpy as np
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
def do_something_else(data,rank):
  if(rank==0):
    print("Data base :{} been sent from core: {} 😋️ ".format(data.keys(),rank))
  elif(rank==1):
    print("Data base :{} been recieved in core: {} 🤪️ ".format(data.keys(),rank))

if rank == 0:

    data = {'Digits': 3.141592653589793,'Lists':[1,3,4,5,'A','B','6'],'Arrays':np.array([[12,12,34],[1,2,4]])}
   
    req_1=comm.isend(data, dest=1, tag=0)# req is mpi4py.MPI.Request object
    req_1.wait()
    do_something_else(data,rank)
    
elif rank == 1:
    req_2 = comm.irecv(source=0, tag=0) # req is mpi4py.MPI.Request object
    data_recieved=req_2.wait()
    do_something_else(data_recieved,rank)
   
