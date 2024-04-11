import pytest
from time import sleep
from assertpy import assert_that
from src.load_balancer import LoadBalancer


class TestLoadBalancer:
    @pytest.mark.parametrize('policy', [LoadBalancer.Policy.round_robin, LoadBalancer.Policy.random_choice])
    def test_load_balancer_policies(self, test_queue, create_tasks, create_servers, policy):
        # Start load balancer
        LoadBalancer(test_queue, 3, policy).start()

        sleep(1)

        # Verify all tasks are consumed
        assert_that(test_queue.get_tasks_num()).is_equal_to(0)
