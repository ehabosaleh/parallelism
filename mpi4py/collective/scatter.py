
from mpi4py import MPI

import numpy as np
comm = MPI.COMM_WORLD
s = comm.Get_size()
rank = comm.Get_rank()
n=5
if rank == 0:
   data = np.random.randint(n**n,size=(s,n**2))
   print ('We will be scattering:{}'.format(data))
   data = comm.scatter(data, root=0)
   print ('rank {} has data: {}\n'.format(rank,data))
else:
   data = None
   data = comm.scatter(data, root=0)
   print ('rank {} has data: {}\n'.format(rank,data))



