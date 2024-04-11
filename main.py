from threading import Event
from time import sleep

from src.load_balancer import LoadBalancer
from src.server import Server
from src.work_queue import WorkQueue


# Create a queue
queue = WorkQueue(Event())

# Add some tasks to queue
for i in range(9):
    queue.add_task(f'Task_rr_{i}')

# Create some server threads
for s in range(3):
    Server(s, queue).start()

print('Round-robin execution:')
# Start a round-robin load balancer
LoadBalancer(queue, 3, LoadBalancer.Policy.round_robin).start()

# Wait for tasks to finish
sleep(1)

# Stop all threads execution
queue.stop_threads()

# Add new tasks to queue
for i in range(9):
    queue.add_task(f'Task_rc_{i}')

# Re-enable queue
queue.re_enable()

print('Random choice execution:')
# Start a random choice load balancer
LoadBalancer(queue, 3, LoadBalancer.Policy.random_choice).start()

# Wait for tasks to finish
sleep(1)

# Stop all threads execution
queue.stop_threads()
