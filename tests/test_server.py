from time import sleep
from assertpy import assert_that


class TestServer:
    def test_servers_are_idle_without_scheduling(self, test_queue, create_tasks, create_servers):
        sleep(1)

        # Verify NO tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(9)

    def test_servers_are_activated_with_scheduling(self, test_queue, create_tasks, create_servers):
        # Attempt to consume all tasks by same server
        for _ in range(9):
            test_queue.set_next_worker(0)
            test_queue.get_task_for_sid(0)

        # Verify tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(0)
