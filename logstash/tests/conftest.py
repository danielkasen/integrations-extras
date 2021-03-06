import os

import pytest

from datadog_checks.dev import docker_run
from datadog_checks.dev.conditions import CheckEndpoints

from .common import HERE, URL


@pytest.fixture(scope='session')
def dd_environment():
    with docker_run(
        compose_file=os.path.join(HERE, "docker", "docker-compose.yml"), conditions=[CheckEndpoints(URL, wait=2)]
    ):
        yield
