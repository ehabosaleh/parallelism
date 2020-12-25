import threading
import concurrent.futures
import time
def do_something(seconds):
	print(f"Sleeping for {seconds} second(s)...")
	time.sleep(seconds)
	return f'Done sleeping for {seconds} second(s)...'

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs=[5,4,3,2,1]
	results=executor.map(do_something,secs)
	for result in results:
		print(result)

