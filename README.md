
# Agent Zero (De-Dockerized)

This is a native Python version of Agent Zero, without Docker dependencies.

## Requirements

- Python 3.8+
- pip (Python package manager)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/agent-zero-native.git
   cd agent-zero-native
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/run_ui.py
   ```

4. Access the web interface at: http://localhost:50001

## Available Tasks

Try these example tasks:
- "list processes" - Shows running processes on your system
- "list files" - Displays files in the current directory
- "system info" - Provides detailed system information (CPU, memory, disk usage)

## Using with Pinokio

This project includes a `pinokio.json` configuration file that makes it easy to run in Pinokio:

1. Open Pinokio
2. Add this repository
3. Click "Install" and then "Run"
4. Access the web interface at: http://localhost:50001

## How It Works

Agent Zero is a lightweight agent that:
1. Receives tasks through a web UI
2. Processes the tasks using simple keyword matching
3. Executes appropriate tools based on the task
4. Returns the results to the web UI

## Adding New Tools

To add new tools, create Python scripts in the `src/tools/` directory.

For example, to create a new tool that checks available disk space:

```python
# src/tools/disk_space.py
import shutil

def get_disk_space():
    """Return available disk space on the system"""
    total, used, free = shutil.disk_usage("/")
    return {
        "total": total // (2**30),  # GB
        "used": used // (2**30),    # GB
        "free": free // (2**30)     # GB
    }
```

Then, add a new method to the Agent class in `agent.py` to use your tool.
