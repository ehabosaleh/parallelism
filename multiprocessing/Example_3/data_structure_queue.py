from multiprocessing import Process, Queue, Lock

def square(numbers,queue,lock):
    for i in numbers:
       lock.acquire()
       queue.put(i**2)
       lock.release()

def cube(numbers,queue,lock):
    for i in numbers:
       lock.acquire()
       queue.put(i**3)
       lock.release()
if __name__=='__main__':
    numbers=[1,2,3,4,5,6]
    queue=Queue()
    lock=Lock()
    square_p=Process(target=square,args=(numbers,queue,lock))
    cube_p=Process(target=cube,args=(numbers,queue,lock))
    square_p.start()
    cube_p.start()
    square_p.join()
    cube_p.join()
    while not queue.empty():
          print(queue.get())
