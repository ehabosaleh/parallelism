from mpi4py import MPI
comm = MPI.COMM_WORLD
print('The number of cores are :{}\n'.format(comm.Get_size()))
R=comm.Get_rank()
if R==0:
   print("Hi, this is core {} sending first message!".format(R))
   comm.send('Ehab Saleh',dest=1)
elif R==1:
   print("Hi, this is core {} reciveing first message!".format(R))
   message=comm.recv()
   print("This message: {} , from processor {}".format(message,R))
   


