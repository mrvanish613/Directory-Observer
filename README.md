---

# File System Watcher Script

## Description
This Python script monitors specified directories for file system events such as file creation and modification. It uses the `watchdog` library to keep track of filesystem changes. When a file is created or modified, the script logs these events.

## Requirements
- Python 3.x
- `watchdog` library

To install `watchdog`, run:
```bash
pip install watchdog
```

## Usage
To use the script, run it with Python 3. It will require administrator privileges to function correctly. Upon execution, it will ask for the directory path that you want to monitor.

## Features
- Monitor specified directories for file changes.
- Log file creation and modification events.
- Requires administrator privileges to access some system directories.

---
