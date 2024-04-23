## Task Queue
- Maintains tasks awaiting to be consumed by associated server threads.
- Facilitates run, synchronization & shutdown of associated server threads and scheduler thread.


## Servers
- Consume tasks whenever their server id has been selected by associated scheduler.
- Run endlessly until task queue notifies for shutdown.


## Load Balancer
- Creates a scheduler thread that selects next server to consume task according to selected policy.
- Runs endlessly until task queue notifies for shutdown.


## Example
Running [main.py](src%2Fmain.py) gives us a demo round of execution for each scheduling type:

    Round-robin execution:
        Server: 0, served: Task_rr_0.
        Server: 1, served: Task_rr_1.
        Server: 2, served: Task_rr_2.
        Server: 0, served: Task_rr_3.
        Server: 1, served: Task_rr_4.
        Server: 2, served: Task_rr_5.
        Server: 0, served: Task_rr_6.
        Server: 1, served: Task_rr_7.
        Server: 2, served: Task_rr_8.
    Random choice execution:
        Server: 0, served: Task_rc_0.
        Server: 2, served: Task_rc_1.
        Server: 1, served: Task_rc_2.
        Server: 2, served: Task_rc_3.
        Server: 1, served: Task_rc_4.
        Server: 0, served: Task_rc_5.
        Server: 1, served: Task_rc_6.
        Server: 2, served: Task_rc_7.
        Server: 0, served: Task_rc_8.
