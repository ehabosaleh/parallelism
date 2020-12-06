from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
n=5
if rank == 0:
    sendbuf = np.array(np.random.randint(n**2,size=(n,n)),dtype=np.float64)
  
    print(sendbuf)

    # count: the size of each sub-task
 
    ave, res = divmod(sendbuf.size, nprocs)
    count = [ave + 1 if p < res else ave for p in range(nprocs)]
    count = np.array(count)
    print(count)
    
    # displacement: the starting index of each sub-task
    displ = [sum(count[:p]) for p in range(nprocs)]
    displ = np.array(displ)
    
    
else:
    sendbuf = None

    count = np.zeros(nprocs, dtype=np.int)
    displ = None
    
comm.Bcast(count, root=0)
    
    

recvbuf = np.zeros(count[rank])

comm.Scatterv([sendbuf, count, displ,  MPI.DOUBLE], recvbuf, root=0)

print('After Scatterv, process {} has data:'.format(rank), recvbuf)

"""The root processor just scatter the vector specified in the instructionand uses the count and displ to help the root processor identify the number and the indexes if data to be sent. but the othrer processor need to know the size of scattered data so we the root processor needs also to broascast the amount count"""

