from T1_Sensor import *
from T2_BC import *


thread1 = SensorThread("0", "Thread-1")
thread2 = BC_Thread("1", "Thread-2")
	
try:
	thread1.start()
	thread2.start()
except:
	print("Can not start thread")

thread1.join()
thread2.join()

print(thread1.name + " Exited Successfully")
print(thread2.name + " Exited Successfully")
print("Exiting Main Thread")