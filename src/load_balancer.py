from enum import Enum, auto
from random import choice
from threading import Thread

from .work_queue import WorkQueue


class LoadBalancer(Thread):
    """
    Instance schedules given queue's server threads according to selected policy.
    """
    class Policy(Enum):
        round_robin = auto()
        random_choice = auto()

    def __init__(self, wq: WorkQueue, server_count: int, policy: Policy):
        self.serve = 0
        self.server_num = server_count
        self.wq = wq
        self.stop = False
        self.policy = policy
        self.schedulers = [self.round_robin, self.random_choice]

        Thread.__init__(self)

    def run(self):
        while True:
            if self.wq.check_end():
                break

            self.schedulers[self.policy.value - 1]()

    def round_robin(self):
        """Round-robin policy, schedules next server in a clockwise manner."""
        if self.wq.set_next_worker(self.serve):
            # Cycle through server ids
            self.serve += 1
            if self.serve == self.server_num:
                self.serve = 0

    def random_choice(self):
        """Random choice policy, schedules next server randomly."""
        if self.wq.set_next_worker(self.serve):
            self.serve = choice([x for x in range(0, self.server_num) if x != self.serve])
