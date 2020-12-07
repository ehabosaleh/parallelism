from mpi4py import MPI
import time
import math



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

# number of integration steps
nsteps = 10000000
# step size
dx = 1.0 / nsteps

if rank == 0:
    # determine the size of each sub-task
    ave, res = divmod(nsteps, nprocs)
    counts = [ave + 1 if p < res else ave for p in range(nprocs)]

    # determine the starting and ending indices of each sub-task
    starts = [sum(counts[:p]) for p in range(nprocs)]
    ends = [sum(counts[:p+1]) for p in range(nprocs)]
   
    # save the starting and ending indices in data  
    data = [(starts[p], ends[p]) for p in range(nprocs)]
else:
    data = None

data = comm.scatter(data, root=0)
partial_pi = 0.0
t0 = time.process_time()
for i in range(data[0], data[1]):
    x = (i + 0.5) * dx
    partial_pi += 4.0 / (1.0 + x * x)
partial_pi *= dx
partial_pi = comm.gather(partial_pi, root=0)
t1 = time.process_time()
if rank == 0:
    print("Computed pi value is: {}".format(sum(partial_pi)))
    print('*'*50)
    print('pi computed in {:.3f} sec'.format(t1 - t0))
    
    print('*'*50)
    print('error is {}'.format(abs(sum(partial_pi)- math.pi)))

