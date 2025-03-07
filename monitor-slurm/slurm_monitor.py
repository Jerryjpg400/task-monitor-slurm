import subprocess
import time
import asyncio
import sys
from .telegram_notify import send_telegram_message


async def monitor_slurm_job(task_name: str, script: str) -> None:
    """
    Submits an SLURM job using sbatch and tracks its status through PENDING, RUNNING, and COMPLETED/FAILED states.

    Args:
        task_name (str): Descriptive name for the task.
        script (str): The SLURM job script to submit.
    """
    try:
        # Submit the SLURM job
        sbatch_output = subprocess.check_output(["sbatch", script], text=True)
        job_id = sbatch_output.strip().split()[-1]  # Extract job ID

        await send_telegram_message(f"🚀 *Submitted {task_name}* (SLURM Job `{job_id}`), waiting to start...")

        # Monitor job status
        job_started = False

        while True:
            time.sleep(10)  # Check every 10 seconds
            status = subprocess.getoutput(f"squeue --job {job_id} --format=%T | tail -n 1").strip()

            if status == "RUNNING" and not job_started:
                await send_telegram_message(f"⚡ *{task_name}* (SLURM Job `{job_id}`) is now running!")
                job_started = True

            if status not in ["PENDING", "RUNNING"]:
                break  # Job is no longer running or pending

        # Fetch final job status
        final_status = subprocess.getoutput(f"sacct -j {job_id} --format=JobID,State | tail -n 1").strip()

        if "COMPLETED" in final_status:
            await send_telegram_message(f"✅ *{task_name}* (SLURM Job `{job_id}`) completed successfully.")
        else:
            await send_telegram_message(f"⚠️ *{task_name}* (SLURM Job `{job_id}`) failed.\nStatus: {final_status}")

    except Exception as e:
        await send_telegram_message(f"❌ *{task_name}* submission failed.\nError: {e}")
        sys.exit(1)

