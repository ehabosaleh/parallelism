from mpi4py import MPI
import numpy as np
comm=MPI.COMM_WORLD
rank=comm.Get_rank()

def do_something_else(rank):
  print("this is core: {} 😁️, at your service ☠️ ".format(rank))

if rank == 0:

    data = {'a': 7, 'b': 3.14,'c':[1,3,4,5,6],'d':np.array([[12,12,34],[1,2,4]])}
   
    comm.send(data, dest=1, tag=0)
    do_something_else(rank)
elif rank == 1:
    
    data=comm.recv(source=0, tag=0)
   # data= comm.recv(source=1, tag=0)
    do_something_else(rank)



  
