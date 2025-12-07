# Assignment 1 – Python Utility Scripts

## Overview
This repository contains a collection of Python scripts created as part of Assignment 1.  
Each script demonstrates basic system utilities such as configuration management, password-strength validation, CPU usage monitoring, and backup automation.

The project is intended for learners who want to explore Python scripting concepts and simple automation tasks.

## Repository Structure
```

assignment_1/
│
├── backup.py
├── backup2.py
├── check_password_strength.py
├── config.ini
├── config_management.py
├── cpu_usage_monitor.py
├── requirements.txt
└── README.md

````

## Features
- Read and update configuration values using `.ini` files.
- Validate password strength using defined criteria.
- Monitor CPU usage to understand basic system performance.
- Execute simple backup operations (two variations included).
- Demonstrate modular scripting practices in Python.

## Prerequisites
- Python 3.x installed on your system.
- Optional: a virtual environment tool such as `venv`.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/sowjanya-gundumalla/assignment_1.git
   cd assignment_1
````

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuration Management

Reads and updates values stored in `config.ini`.

```bash
python config_management.py
```

### Password Strength Checker

Validates user-provided passwords based on length, complexity, and character rules.

```bash
python check_password_strength.py
```

### CPU Usage Monitor

Displays basic CPU usage information.

```bash
python cpu_usage_monitor.py
```

### Backup Scripts

Creates a backup of specified files or directories.
Make sure to adjust `config.ini` to match your environment.

```bash
python backup.py
# or
python backup2.py
```

## Configuration File

`config.ini` contains values used by some scripts, such as file paths, backup locations, or monitoring limits.
Update this file before running scripts that depend on it.

## Suggested Improvements

Future enhancements could include:

* Adding unit tests for each script.
* Improving error handling and logging.
* Extending the monitoring script to include memory and disk usage.
* Creating a command-line interface to unify all utilities.
* Scheduling backups or automating them more fully.

## License

This project currently does not specify a license.
If needed, you may include MIT, Apache 2.0, or another open-source license of your choice.

## Contact

For questions or contributions, feel free to open an issue or submit a pull request on GitHub.
