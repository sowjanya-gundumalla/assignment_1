# assignment_1

## 🎯 Project Overview  
This repository contains “First Python Assignment” — a set of Python utilities and scripts for tasks such as configuration management, password-strength checking, CPU usage monitoring, backups, etc. It serves as a learning / utility project to practise Python scripting and basic system-automation tasks.

## 📁 Contents  
| File / Module | Description |
|---------------|-------------|
| `config_management.py` | Script to manage configuration (read/write) from `config.ini`. |  
| `check_password_strength.py` | Script to validate and check strength of passwords. |  
| `cpu_usage_monitor.py` | Script to monitor CPU usage (for system monitoring). |  
| `backup.py`, `backup2.py` | Backup utilities / example scripts. |  
| `config.ini` | Configuration file (used by config-management script). |  
| `requirements.txt` | List of external dependencies / Python packages required. |  

## 🚀 Getting Started  

### Prerequisites  
- Python (version 3.x) installed on your system.  
- (Optional) A virtual environment tool like `venv` or `virtualenv` is recommended.  

### Installation & Setup  
```bash  
# Clone the repository  
git clone https://github.com/sowjanya-gundumalla/assignment_1.git  
cd assignment_1  

# (Optional but recommended) create virtual environment  
python3 -m venv venv  
source venv/bin/activate      # on Linux / macOS  
venv\Scripts\activate         # on Windows  

# Install dependencies  
pip install -r requirements.txt  
