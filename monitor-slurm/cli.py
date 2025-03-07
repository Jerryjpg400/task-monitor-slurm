import argparse
import asyncio
from .slurm_monitor import monitor_slurm_job


def parse_args() -> argparse.Namespace:
    """
    Parses command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Submit SLURM jobs and monitor execution with Telegram notifications.")
    parser.add_argument("task_name", type=str, help="Descriptive name of the task.")
    parser.add_argument("job_script", type=str, help="Path to the SLURM job script.")

    return parser.parse_args()


def main() -> None:
    """
    Main function to parse arguments and execute SLURM job monitoring.
    """
    args = parse_args()
    asyncio.run(monitor_slurm_job(args.task_name, args.job_script))


if __name__ == "__main__":
    main()

