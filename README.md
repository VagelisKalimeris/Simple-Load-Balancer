## Task Queue
Task queue serves 2 purposes:
- Maintains tasks awaiting to be consumed by servers.
- Facilitates safe server threads and scheduler thread, run, synchronization, shutdown.


## Server
Servers are simple threads that consume tasks whenever their server id has been selected by scheduler.
Run endlessly until task queue notifies for shutdown.


## Load Balancer
Creates a scheduler thread that selects next server to consume task according to selected policy.
Runs endlessly until task queue notifies for shutdown.
