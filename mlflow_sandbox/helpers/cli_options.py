import argparse
from typing import Tuple


def get_cli_options() -> Tuple[int, int, bool]:
    parser = argparse.ArgumentParser(description="Provide input for training models")
    parser.add_argument(
        "--size", "-n", type=int, default=1000, help="Provide sample size"
    )
    parser.add_argument(
        "--workers", "-w", type=int, default=2, help="Provide number of workers"
    )
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        default=False,
        help="Use RandomSearch Optimizer, else use default GridSearch Optimizer",
    )

    args = parser.parse_args()
    return args.size, args.workers, args.random
