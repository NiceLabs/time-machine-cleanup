#!/usr/bin/env python3
import os
import sys
from argparse import ArgumentParser
from datetime import datetime, timedelta
from subprocess import check_output, run
from typing import List, Tuple


def get_backup_time(backup_path: str) -> datetime:
    return datetime.strptime(os.path.basename(backup_path), "%Y-%m-%d-%H%M%S")


def delete_backup(backup_path: str):
    start_time = datetime.now()
    run(["tmutil", "delete", backup_path])
    end_time = datetime.now()
    print("Elapsed time:", end_time - start_time)


def list_backups() -> List[Tuple[timedelta, str]]:
    now = datetime.now()
    latest_path = check_output(["tmutil", "latestbackup"]).decode()
    machine_path = check_output(["tmutil", "machinedirectory"]).decode()
    return [
        (now - get_backup_time(backup_path), backup_path)
        for backup_path
        in check_output(["tmutil", "listbackups"]).decode().splitlines()
        if backup_path.startswith(machine_path) and backup_path != latest_path
    ]


def cleanup(base_delta: timedelta):
    print("Removing old Time Machine Backups for older than", base_delta.days, "days.")
    backups = list_backups()
    if not backups:
        print("Did not find any Time Machine Backups older than", base_delta.days, "days old.")
        sys.exit(2)
    for delta, backup_path in backups:
        if delta > base_delta:
            delete_backup(backup_path)


def main():
    if os.geteuid() != 0:
        print("This script must be run as root!")
        sys.exit(1)

    parser = ArgumentParser()
    parser.add_argument("--day-ago", type=int, default=30)
    args = parser.parse_args()
    cleanup(timedelta(days=args.day_ago))


if __name__ == "__main__":
    main()
