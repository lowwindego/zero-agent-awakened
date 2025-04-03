
import subprocess
import os
import platform
import json
from typing import Dict, List, Optional, Any

class AgentConfig:
    def __init__(
        self,
        code_exec_docker_enabled: bool = False,
        api_keys: Optional[Dict[str, str]] = None,
    ):
        self.code_exec_docker_enabled = code_exec_docker_enabled
        self.api_keys = api_keys or {}

class Agent:
    def __init__(self, config: AgentConfig):
        self.config = config
        self.tools_dir = os.path.join(os.path.dirname(__file__), "tools")
        
    def run_task(self, task: str) -> Dict[str, Any]:
        """Process a user task and return the result"""
        print(f"Processing task: {task}")
        
        # Simple keyword-based tool selection
        if "list processes" in task.lower():
            return self._run_list_processes()
        elif "file" in task.lower() and "list" in task.lower():
            return self._run_list_files()
        else:
            # Default response for unrecognized tasks
            return {
                "response": f"I understood your task: '{task}', but I don't have a specific tool for this yet. "
                           f"You can try 'list processes' or 'list files' as example tasks."
            }
    
    def _run_list_processes(self) -> Dict[str, Any]:
        """Run system command to list processes"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(["tasklist"], capture_output=True, text=True, check=True)
            else:  # Linux/Mac
                result = subprocess.run(["ps", "aux"], capture_output=True, text=True, check=True)
                
            return {
                "response": "Here are the current processes running on your system:",
                "output": result.stdout,
                "tool_used": "system_process_lister"
            }
        except Exception as e:
            return {"error": f"Failed to list processes: {str(e)}"}
    
    def _run_list_files(self) -> Dict[str, Any]:
        """Run system command to list files in current directory"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(["dir"], shell=True, capture_output=True, text=True, check=True)
            else:  # Linux/Mac
                result = subprocess.run(["ls", "-la"], capture_output=True, text=True, check=True)
                
            return {
                "response": "Here are the files in the current directory:",
                "output": result.stdout,
                "tool_used": "file_lister"
            }
        except Exception as e:
            return {"error": f"Failed to list files: {str(e)}"}
    
    def list_available_tools(self) -> List[str]:
        """Return a list of available tools"""
        return ["system_process_lister", "file_lister"]
