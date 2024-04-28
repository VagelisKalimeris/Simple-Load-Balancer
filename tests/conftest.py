from threading import Event
import pytest
from src.server import Server
from src.work_queue import WorkQueue


@pytest.fixture(scope='function')
def test_queue() -> WorkQueue:
    # Create test queue
    test_queue = WorkQueue(Event())

    yield test_queue

    # Stop execution of all threads working on current queue
    test_queue.stop_threads()


@pytest.fixture(scope='function')
def create_tasks(test_queue: WorkQueue) -> None:
    # Add tasks to queue
    for _ in range(9):
        test_queue.add_task('test_task')


@pytest.fixture(scope='function')
def create_servers(test_queue: WorkQueue) -> None:
    # Create server threads
    for s in range(3):
        Server(s, test_queue).start()
