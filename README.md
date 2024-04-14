## Task Queue
- Maintains tasks awaiting to be consumed by associated server threads.
- Facilitates run, synchronization & shutdown of associated server threads and scheduler thread.


## Servers
- Consume tasks whenever their server id has been selected by associated scheduler.
- Run endlessly until task queue notifies for shutdown.


## Load Balancer
- Creates a scheduler thread that selects next server to consume task according to selected policy.
- Runs endlessly until task queue notifies for shutdown.
