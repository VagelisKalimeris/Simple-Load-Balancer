import pytest
from time import sleep
from assertpy import assert_that
from src.load_balancer import LoadBalancer
from src.work_queue import WorkQueue


class TestLoadBalancer:
    @pytest.mark.parametrize('policy', [LoadBalancer.Policy.round_robin, LoadBalancer.Policy.random_choice])
    def test_load_balancer_policies(self, test_queue: WorkQueue, create_tasks: None, create_servers: None,
                                    policy: LoadBalancer.Policy) -> None:
        # Start load balancer
        LoadBalancer(test_queue, 3, policy).start()

        sleep(1)

        # Verify all tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(0)
