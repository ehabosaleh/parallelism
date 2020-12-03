from mpi4py import  MPI
import numpy as np
import random as rn

comm=MPI.COMM_WORLD
size = comm.Get_size()
rank=comm.Get_rank()
n=200
if rank==0:
     data_buffer=[0,0,0]
     array=np.random.randint(10000,size=(n,n))
     for i in range(1,4):
         comm.Send(array,dest=i,tag=i)
     for j in range(1,4):
         data_buffer[j-1]=comm.recv(source=j,tag=j)
     print("Matrix summstion is: {}".format(data_buffer[0]))
     print("Maximum value is :  {}".format(data_buffer[1]))
     print("Minimum value is :  {}".format(data_buffer[2]))
  

if rank==1:
    data_1=np.empty([n,n])
    comm.Recv(data_1,source=0,tag=rank)
    s=np.sum(data_1)
    comm.send(s,dest=0,tag=rank)

if rank==2:
    data_2=np.empty([n,n])
    comm.Recv(data_2,source=0,tag=rank)
    Max=np.amax(np.amax(data_2))
    comm.send(Max,dest=0,tag=rank)

if rank==3:
    data_3=np.empty([n,n])
    comm.Recv(data_3,source=0,tag=rank)
    Min=np.amin(np.amin(data_3))
    comm.send(Min,dest=0,tag=rank)
