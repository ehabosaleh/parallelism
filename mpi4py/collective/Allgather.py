from mpi4py import MPI
import time
import math
import numpy as np
t0 = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
nsteps=1000000
dx = 1.0 / nsteps

if rank == 0:
    
    sendbuf = list(range(nsteps))
    ave, res = divmod(nsteps, nprocs)
    counts = np.array([ave for p in range(nprocs)])
    starts = np.array([sum(counts[:p]) for p in range(nprocs)]) 
    sendbuf=np.array( [sendbuf[starts[i]:starts[i]+counts[i]] for i in range(nprocs)],dtype="float64")
 
   
    
   
else:
    sendbuf = None
    data = None
    recvbuf=None
    counts = np.empty(nprocs, dtype=np.int)
    

comm.Bcast(counts,root=0)


recvbuf=np.zeros(counts[rank],dtype=np.float64)

comm.Scatter([sendbuf, MPI.DOUBLE], recvbuf, root=0)



partial_pi = np.zeros(nprocs)
t0 = time.process_time()
for i in  recvbuf:
    x = (i + 0.5) * dx
    partial_pi[rank] += 4.0 / (1.0 + x * x)
partial_pi[rank] *= dx
t1 = time.process_time()


counts=np.ones(nprocs)
pi_value= np.zeros(nprocs)

comm.Allgather(partial_pi[rank], [pi_value, MPI.DOUBLE])


print("Core {} computed pi value: {} in {} sec".format(rank,sum(pi_value),(t1 - t0)))
print()


