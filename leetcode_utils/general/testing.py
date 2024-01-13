import glob
import importlib
import inspect
import itertools
import os.path as osp


def get_test_suite(test_data):
    test_file_path = inspect.currentframe().f_back.f_globals["__file__"]
    solution_paths = glob.glob(osp.abspath(f"{test_file_path}/../solution*.py"))
    solution_names = [osp.basename(path[:-3]) for path in solution_paths]
    solutions = [importlib.import_module(name) for name in solution_names]

    return [
        (solution.Solution(), *data)
        for solution, data in itertools.product(solutions, test_data)
    ]
