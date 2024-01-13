import glob
import importlib
import inspect
import os.path as osp


def discover_solutions():
    test_file_path = inspect.currentframe().f_back.f_globals["__file__"]
    solution_paths = glob.glob(osp.abspath(f"{test_file_path}/../solution*.py"))
    solution_names = [osp.basename(path[:-3]) for path in solution_paths]

    return [importlib.import_module(name) for name in solution_names]
