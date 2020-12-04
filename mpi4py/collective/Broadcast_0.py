import numpy as np
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
n=10
if rank==0:
     A1 = np.arange (n,  dtype=np.float64)
     comm.Bcast( [A1, MPI.DOUBLE] , root =0)
else:
     A2 = np.empty (n,  dtype=np.float64)
     comm.Bcast( [A2, MPI.DOUBLE] , root =0)
     if rank==1:
	       print("the mean value is :{}".format(np.mean(A2)))
     if rank==2:
	       print("The standard deviation value is :{}".format(np.std(A2)))
     if rank==3:
	       print("The variance value is :{}".format(np.var(A2)))

     
        
