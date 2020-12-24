import threading
import concurrent.futures
import time


def do_something(seconds):
	print(f'Sleeping for {seconds} seconds(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'

start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
	results=[executor.submit(do_something,1) for _ in range(10)]
	for f in concurrent.futures.as_completed(results):
		print(f.result())

end=time.perf_counter()
print(f'Finished in {end-start} sec')
