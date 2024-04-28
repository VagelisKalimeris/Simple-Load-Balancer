from time import sleep
from assertpy import assert_that
from src.work_queue import WorkQueue


class TestServer:
    def test_servers_are_idle_without_scheduling(self, test_queue: WorkQueue, create_tasks: None,
                                                 create_servers: None) -> None:
        sleep(1)

        # Verify NO tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(9)

    def test_servers_are_activated_with_scheduling(self, test_queue: WorkQueue, create_tasks: None,
                                                   create_servers: None) -> None:
        # Attempt to consume all tasks by same server
        for _ in range(9):
            test_queue.set_next_worker(0)
            test_queue.get_task_for_sid(0)

        # Verify tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(0)
