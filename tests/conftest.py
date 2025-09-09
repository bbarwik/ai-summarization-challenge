"""Common test fixtures for pipeline projects."""

import asyncio

import pytest
from ai_pipeline_core import disable_run_logger, prefect_test_harness


@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    """
    Session-scoped fixture that runs all tests against a temporary Prefect database.
    This isolates tests and prevents them from affecting the main Prefect database.
    """
    with prefect_test_harness():
        yield


@pytest.fixture(autouse=True, scope="session")
def disable_prefect_logging():
    """
    Function-scoped fixture that disables Prefect run logger for each test.
    This prevents RuntimeError from missing flow context when testing tasks/flows directly.
    """
    with disable_run_logger():
        yield


@pytest.fixture(autouse=True, scope="session")
def event_loop():
    """
    Create an event loop with proper cleanup handling.
    This overrides pytest-asyncio's default event loop fixture to handle cleanup better.
    """
    loop = asyncio.new_event_loop()
    yield loop

    # Give pending tasks time to complete before closing the loop
    try:
        pending = asyncio.all_tasks(loop)
        if pending:
            # Allow a small delay for httpx and other async cleanup
            loop.run_until_complete(asyncio.sleep(0.2))

            # Cancel remaining tasks
            for task in asyncio.all_tasks(loop):
                task.cancel()

            # Wait for cancellation to complete
            loop.run_until_complete(
                asyncio.gather(*asyncio.all_tasks(loop), return_exceptions=True)
            )
    finally:
        loop.close()
