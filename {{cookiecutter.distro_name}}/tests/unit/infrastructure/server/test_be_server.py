from http import HTTPStatus
from unittest import TestCase

from fastapi import FastAPI
from starlette.testclient import TestClient

from {{cookiecutter.package_name}}.infrastructure.adapters.factory import FactoryType
from {{cookiecutter.package_name}}.infrastructure.server.be_server import API_PREFIX, create_app


class TestBeServer(TestCase):
    """A test case for BE Server end points."""

    app: FastAPI
    client: TestClient

    @classmethod
    def setUpClass(cls) -> None:
        """Preparation steps that are executed once for the entire test case."""
        cls.app = create_app(FactoryType.LOCAL_TEST)
        cls.client = TestClient(cls.app)

    def test_has_healthy_check_endpoints(self):
        """be_server should have end-points to check for health status (liveness and readiness).

        Given an instance of BE server
        When its health check end-points are called
        Then a successful HTTP response is returned.
        """
        end_point_info = [
            # (test name, url path)
            ("liveness", f"{API_PREFIX}/health/live"),
            ("readiness", f"{API_PREFIX}/health/ready"),
        ]
        for test_name, url_path in end_point_info:
            with self.subTest(test_name):
                response = self.client.get(url_path)
                self.assertEqual(response.status_code, HTTPStatus.OK)
