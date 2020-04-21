# -*- coding: utf-8 -*-


def test_modules_durations(testdir):

    # create a temporary pytest test module
    testdir.makepyfile(
        test_foo="""
        def test_sth():
            assert 2 + 2 == 4
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest("--modules-durations=2")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["*s test_foo.py",]
    )

    assert "sum of all tests durations" in "\n".join(result.stdout.lines)

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_functions_durations(testdir):

    # create a temporary pytest test module
    testdir.makepyfile(
        test_foo="""
        import time
        import pytest
        
        @pytest.mark.parametrize("dodo", range(3))
        def test_sth(dodo):
            time.sleep(0.1)
            assert 2 + 2 == 4
        
        def test_dada():
            time.sleep(0.15)
            assert 2 + 2 == 4
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest("--functions-durations=1")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["*s test_foo.py::test_sth",]
    )

    for line in result.stdout.lines:
        assert "test_dada" not in line

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest("--help",)
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["*--functions-durations=N*",]
    )
    result.stdout.fnmatch_lines(
        ["*Shows the N slowest test functions durations*",]
    )
    result.stdout.fnmatch_lines(
        ["*--modules-durations=N*",]
    )
    result.stdout.fnmatch_lines(
        ["*Shows the N slowest modules durations*",]
    )
