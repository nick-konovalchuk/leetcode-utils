import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("path", help="name or path for a new problem directory")
    args = parser.parse_args()

    if args.command == "init":
        os.makedirs(args.path)
        with open(f"{args.path}/solution1.py", "w") as f:
            pass

        with open(f"{args.path}/test_all.py", "w") as f:
            pass
    else:
        print("Unknown command")
