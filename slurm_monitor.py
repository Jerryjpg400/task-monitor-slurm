import subprocess
import time
import asyncio
import sys
from .telegram_notify import send_telegram_message


async def monitor_slurm_job(task_name: str, script: str) -> None:
    """
    Submits an SLURM job using sbatch and monitors its execution.

    Args:
        task_name (str): Descriptive name for the task.
        script (str): The SLURM job script to submit.
    """
    try:
        # Submit the SLURM job
        sbatch_output = subprocess.check_output(["sbatch", script], text=True)
        job_id = sbatch_output.strip().split()[-1]  # Extract job ID
        await send_telegram_message(f"🚀 *Started {task_name}* (SLURM Job `{job_id}`)")

        # Monitor job status
        while True:
            time.sleep(10)  # Check every 10 seconds
            status = subprocess.getoutput(f"squeue --job {job_id}")

            if job_id not in status:
                break  # Job is no longer running

        # Fetch final job status
        final_status = subprocess.getoutput(f"sacct -j {job_id} --format=JobID,State")

        if "COMPLETED" in final_status:
            await send_telegram_message(f"✅ *{task_name}* (SLURM Job `{job_id}`) completed successfully.")
        else:
            await send_telegram_message(f"⚠️ *{task_name}* (SLURM Job `{job_id}`) failed.\nStatus: {final_status}")

    except Exception as e:
        await send_telegram_message(f"❌ *{task_name}* failed to submit.\nError: {e}")
        sys.exit(1)

