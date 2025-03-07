# **Monitor SLURM 🚀**
A CLI tool that **submits SLURM jobs and tracks their status** with real-time **Telegram notifications**. It detects job states including **submission (`PENDING`), execution (`RUNNING`), and completion (`COMPLETED` or `FAILED`)**.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## **Features**
✅ **Automated SLURM Job Monitoring**: Tracks job states (`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`).  
✅ **Real-Time Telegram Notifications**: Receive job updates directly via Telegram.  
✅ **Works with Any SLURM Job Script**: No modifications to `sbatch` required.  
✅ **Handles Failures Gracefully**: Alerts you when a job is canceled or fails.  
✅ **Simple CLI Usage**: Easy-to-use interface with minimal configuration.  

---

## **Installation**
### **1. Install via `pip`**
```bash
pip install git+https://github.com/yourusername/monitor-slurm.git
```
Or install locally:
```bash
git clone https://github.com/yourusername/monitor-slurm.git
cd monitor-slurm
pip install .
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Configure Telegram Bot**
Create a **Telegram bot** via [BotFather](https://t.me/botfather) and get:
- **`TELEGRAM_BOT_TOKEN`**
- **`TELEGRAM_CHAT_ID`**

Create a `.env` file in the project root:
```ini
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

Alternatively, set environment variables in your shell:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_CHAT_ID="your_chat_id_here"
```

---

## **Usage**
### **1. Submit & Monitor a SLURM Job**
To monitor a job:
```bash
monitor-slurm "Data Processing Task" job.sh
```

### **2. Example Telegram Notifications**
✅ **Successful Job Execution**
```
🚀 Submitted Data Processing Task (SLURM Job `123456`), waiting to start...
⚡ Data Processing Task (SLURM Job `123456`) is now running!
✅ Data Processing Task (SLURM Job `123456`) completed successfully.
```
⚠️ **Failed Job Execution**
```
🚀 Submitted Model Training (SLURM Job `987654`), waiting to start...
⚡ Model Training (SLURM Job `987654`) is now running!
⚠️ Model Training (SLURM Job `987654`) failed.
Status: FAILED
```

---

## **Project Structure**
```
monitor_slurm/
│── monitor_slurm/
│   ├── __init__.py
│   ├── config.py          # Configuration for Telegram bot
│   ├── telegram_notify.py # Handles Telegram messaging
│   ├── slurm_monitor.py   # Tracks job submission, execution, and completion
│   ├── cli.py             # CLI entry point
│── pyproject.toml
│── setup.py
│── README.md
│── .env (optional)        # Telegram credentials
```

---

## **Development & Contribution**
### **Setting Up the Development Environment**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/monitor-slurm.git
   cd monitor-slurm
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tool locally:
   ```bash
   python -m monitor_slurm.cli "Test Task" test_job.sh
   ```

### **Contributing**
We welcome contributions! 🚀  
To contribute:
- Fork the repository.
- Create a new feature branch (`feature/my-improvement`).
- Submit a **pull request** with detailed descriptions.

---

## **Troubleshooting**
❓ **Bot not sending messages?**  
✔️ Ensure your **bot has access** to the chat (`CHAT_ID` is correct).  

❓ **Job not tracking?**  
✔️ Make sure the **job script is valid and executable** (`chmod +x job.sh`).  

❓ **Exit Code 1 or 127?**  
✔️ Verify the SLURM command exists (`which sbatch`).  

---

## **License**
This project is licensed under the **MIT License**.  

📜 **Author:** [Your Name](https://github.com/yourusername)  
🔗 **GitHub Repo:** [Monitor SLURM](https://github.com/yourusername/monitor-slurm)  

🚀 **Automate SLURM job tracking effortlessly!**
