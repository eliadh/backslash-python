import pytest
import slash
import munch

from backslash.contrib.utils import distill_slash_traceback

def test_importing_slash_plugin():
    from backslash.contrib import slash_plugin

def test_exception_distilling(traceback):
    assert isinstance(traceback, list)
    assert traceback
    for f in traceback:
        assert f['code_line']

@pytest.fixture
def traceback(error_result):
    [e] = error_result.get_errors()
    return distill_slash_traceback(e)

@pytest.fixture
def error_result():

    def test_failing():
        1/0

    with slash.Session() as s:
        with s.get_started_context():
            slash.runner.run_tests(slash.loader.Loader().get_runnables([test_failing]))
            [res] = s.results.iter_test_results()
    return res
