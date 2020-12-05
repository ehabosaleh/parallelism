import numpy as np
from mpi4py import MPI
import scipy.stats as ss
import matplotlib.pyplot as plt
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
#generate normal distributions numbers
n=1000

if rank==0:
     sendbuf_0 = np.random.normal(0,1, n)
     comm.Bcast(sendbuf_0, root =0)
elif rank==1:
     sendbuf_0 = np.empty(n)
     comm.Bcast(sendbuf_0, root =0)

     cs=['b*','r^']    
     rv_0=ss.norm.pdf(sendbuf_0)
     plt.plot(sendbuf_0,rv_0,cs[0])
     
     m=np.mean(sendbuf_0)
     s=np.std(sendbuf_0)
     
     
     sendbuf_1 = np.random.normal(m,s,n)
     
     rv_1=ss.norm.pdf(sendbuf_1)
     plt.plot(sendbuf_1,rv_1,cs[1])
     plt.legend
     plt.show()   
     
     
     

     
