from time import sleep
from assertpy import assert_that


class TestServer:
    def test_servers_are_idle_without_scheduling(self, test_queue, create_tasks, create_servers):
        sleep(1)

        # Verify NO tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(9)

    def test_servers_are_activated_with_scheduling(self, test_queue):
        # todo: Implement this
        pass
