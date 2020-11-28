from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD

number_of_processors=comm.Get_size()
rank = comm.Get_rank()
if rank==0:
  result=0
  array_1=np.random.randn(1,1000000)
  comm.send(array_1,dest=1,tag=1)

  array_2=np.random.randn(1,1000000)
  comm.send(array_2,dest=2,tag=1)

  array_3=np.random.randn(1,1000000)
  comm.send(array_3,dest=3,tag=1)

  print("Data has been sent. \n")

  for i in range(1,number_of_processors):
   result+= comm.recv(source=i,tag=2)
  print("Sum of all the three arrays is:{}\n".format(result))

elif rank==1:
  data_1=comm.recv(source=0,tag=1)
  sum_1=np.sum(data_1)
  print("Sum of array_1 is :{}\n".format(sum_1))
  comm.send(sum_1,dest=0,tag=2)
  
elif rank==2:
  data_2=comm.recv(source=0,tag=1)
  sum_2=np.sum(data_2)
  print("Sum of array_2 is :{}\n".format(sum_2))
  comm.send(sum_2,dest=0,tag=2)
  
elif rank==3:
  data_3=comm.recv(source=0,tag=1)
  sum_3=np.sum(data_3)
  print("Sum of array_3 is :{}\n".format(sum_3))
  comm.send(sum_3,dest=0,tag=2)
