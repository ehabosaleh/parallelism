from mpi4py import MPI
import time
import math
import numpy as np
t0 = time.time()
from sympy import *
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
nsteps=10000000

x=symbols('x')

if rank == 0:
    
    sendbuf = np.arange(1,nsteps,dtype=np.float64)

    ave, res = divmod(nsteps, nprocs)
    counts = np.array([ave + 1 if p < res else ave for p in range(nprocs)])
    starts = np.array([sum(counts[:p]) for p in range(nprocs)])
   
else:
    sendbuf = None
    data = None
    counts = np.empty(nprocs, dtype=np.int)
    starts=np.empty(nprocs, dtype=np.int)


comm.Bcast(counts,root=0)
comm.Bcast(starts,root=0)

recvbuf = np.zeros(counts[rank])

partial_pi = np.zeros(nprocs)

t0 = time.process_time()
partial_pi[rank]= 4* integrate(1/(1+(x)**2),(x,starts[rank]/nsteps,(starts[rank]+counts[rank])/nsteps))
t1 = time.process_time()
print(partial_pi[rank])

counts=np.ones(nprocs)
pi_value= np.zeros(nprocs)
starts=np.array(list(range(nprocs)))

comm.Gatherv(partial_pi[rank], [pi_value, counts, starts, MPI.DOUBLE], root=0)
if rank == 0:
    print("Computed pi value is: {}".format(sum(pi_value)))
    print('*'*50)
    print('pi computed in {:.3f} sec'.format(t1 - t0))
    
    print('*'*50)
    print('error is {}'.format(abs(sum(pi_value)- math.pi)))

