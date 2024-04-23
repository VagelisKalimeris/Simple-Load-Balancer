from assertpy import assert_that


class TestWorkQueue:
    def test_task_queue_is_empty(self, test_queue):
        # Verify task queue is empty by default
        assert_that(test_queue.get_tasks_num()).is_equal_to(0)

    def test_add_task(self, test_queue):
        # Add a task to queue
        test_queue.add_task('test_task')

        # Verify task queue is NOT empty
        assert_that(test_queue.get_tasks_num()).is_equal_to(1)

    def test_get_task_for_enabled_sid(self, test_queue):
        # Add a task to queue
        test_queue.add_task('test_task')

        # Choose server 0 as next
        test_queue.next_sid = 0

        # Verify chosen server is enabled to consume task
        assert_that(test_queue.get_task_for_sid(0)).is_equal_to('test_task')

        # Verify NO task is left to consume
        assert_that(test_queue.get_task_for_sid(0)).is_equal_to(None)

    def test_get_task_for_not_enabled_sid(self, test_queue):
        # Add a task to queue
        test_queue.add_task('test_task')

        # Verify server 0 cannot receive task before being enabled
        assert_that(test_queue.get_task_for_sid(0)).is_equal_to(None)

    def test_default_next_sid(self, test_queue):
        # Verify next sid is None by default
        assert_that(test_queue.next_sid).is_equal_to(None)

    def test_set_next_worker(self, test_queue):
        # Set next worker
        test_queue.set_next_worker(5)

        # Verify operation succeeded
        assert_that(test_queue.next_sid).is_equal_to(5)

    def test_illegal_set_next_worker(self, test_queue):
        # Set next worker
        test_queue.set_next_worker(5)

        # Attempt to re-set next worker while next worker is NOT None and verify operation failed
        test_queue.set_next_worker(10)
        assert_that(test_queue.next_sid).is_equal_to(5)

    def test_get_tasks_num(self, test_queue, create_tasks):
        # Verify task count is correct
        assert_that(test_queue.get_tasks_num()).is_equal_to(9)

    def test_default_check_end(self, test_queue):
        # Verify un-stopped state
        assert_that(test_queue.check_end()).is_equal_to(False)

    def test_stop_threads_check_end(self, test_queue):
        # Stop execution
        test_queue.stop_threads()

        # Verify stopped state
        assert_that(test_queue.check_end()).is_equal_to(True)

    def test_re_enable(self, test_queue):
        # Stop execution
        test_queue.stop_threads()

        # Re-enable execution
        test_queue.re_enable()

        # Verify un-stopped state
        assert_that(test_queue.check_end()).is_equal_to(False)
