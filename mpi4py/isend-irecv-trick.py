from mpi4py import MPI
import numpy as np
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
class tic_toc:
    data=[]
    def __init__(self,num):
       for i in range(num):
         if rank == 0:
         
              self.data.append(rank)
              req_1=comm.isend(self.data,dest=1,tag=0)
              print("Processor: {} sent: {}".format(rank,self.data))
              req_1.wait() # no need
              req_2=comm.irecv(source=1,tag=1)
              self.data=req_2.wait()
              print("Processor: {} recieved: {}".format(rank,self.data))


         elif rank == 1:
              req_3=comm.irecv(source=0,tag=0)
              self.data=req_3.wait() 
              print("Processor: {} recieved: {}".format(rank,self.data))
              self.data.append(rank) 
              req_4=comm.isend(self.data,dest=0,tag=1)
              print("Processor: {} sent: {}".format(rank,self.data))
              req_4.wait() # no need
              

sr=tic_toc(2)

