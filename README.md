
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
- "list processes"
- "list files"

## Using with Pinokio

This project includes a `pinokio.json` configuration file that makes it easy to run in Pinokio:

1. Open Pinokio
2. Add this repository
3. Click "Install" and then "Run"

## Adding New Tools

To add new tools, create Python scripts in the `src/tools/` directory.
