# -*- coding: utf-8 -*-

from collections import defaultdict


def pytest_addoption(parser):
    parser.addoption(
        "--modules-durations",
        action="store",
        type=int,
        default=None,
        metavar="N",
        help="show N slowest modules durations (N=0 for all). "
        "A module duration is the sum of the durations of all its tests, "
        "setups and teardowns.",
    )

    parser.addoption(
        "--functions-durations",
        action="store",
        type=int,
        default=None,
        metavar="N",
        help="show N slowest test functions durations (N=0 for all). "
        "This is different from the --durations argument. --durations works on "
        "a per-test basis, but a test function can produce multiple tests. "
        "This gives the sum of all the durations of the tests generated from "
        "a given test function.",
    )


def get_test_reports(terminalreporter):
    dlist = []
    for replist in terminalreporter.stats.values():
        for rep in replist:
            if hasattr(rep, "duration"):
                dlist.append(rep)
    return dlist


def report_modules_durations(terminalreporter):
    durations = terminalreporter.config.getoption("--modules-durations")
    if durations is None:
        return

    dlist = get_test_reports(terminalreporter)
    if not dlist:
        return

    # group by file
    durations_by_file = defaultdict(float)
    for test_report in dlist:
        durations_by_file[test_report.fspath] += test_report.duration

    dlist = list(durations_by_file.items())

    dlist.sort(key=lambda x: x[1])
    dlist.reverse()
    terminalreporter.write_sep("=", "slowest modules durations")
    if durations:
        dlist = dlist[:durations]

    for filename, test_time in dlist:
        terminalreporter.write_line(f"{test_time:02.2f}s {filename}")


def report_funtions_durations(terminalreporter):
    durations = terminalreporter.config.getoption("--functions-durations")
    if durations is None:
        return

    dlist = get_test_reports(terminalreporter)
    if not dlist:
        return

    # group by file
    durations_by_file = defaultdict(float)
    for test_report in dlist:
        if "[" in test_report.nodeid:
            file_and_function = test_report.nodeid[: test_report.nodeid.index("[")]
        else:
            file_and_function = test_report.nodeid
        durations_by_file[file_and_function] += test_report.duration

    dlist = list(durations_by_file.items())

    dlist.sort(key=lambda x: x[1])
    dlist.reverse()
    terminalreporter.write_sep("=", "slowest test functions durations")
    if durations:
        dlist = dlist[:durations]

    for filename, test_time in dlist:
        terminalreporter.write_line(f"{test_time:02.2f}s {filename}")


def report_sum_durations(terminalreporter):
    """Print the sum of durations of all the tests."""
    dlist = get_test_reports(terminalreporter)
    if not dlist:
        return

    terminalreporter.write_sep("=", "Sum of all tests durations")
    terminalreporter.write_line(f"{sum(x.duration for x in dlist):02.2f}s")


def pytest_terminal_summary(terminalreporter):
    report_modules_durations(terminalreporter)
    report_funtions_durations(terminalreporter)
    report_sum_durations(terminalreporter)
