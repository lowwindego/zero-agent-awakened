
from flask import Flask, request, jsonify, render_template
import os
from agent import Agent, AgentConfig

app = Flask(__name__, static_folder="static", template_folder="templates")

# Initialize agent with native execution (no Docker)
config = AgentConfig(
    code_exec_docker_enabled=False,
    api_keys={
        "openai": os.environ.get("OPENAI_API_KEY", "")
    }
)
agent = Agent(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/run_task', methods=['POST'])
def run_task():
    data = request.json
    task = data.get('task', '')
    
    if not task:
        return jsonify({"error": "No task provided"}), 400
    
    try:
        result = agent.run_task(task)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/list_tools', methods=['GET'])
def list_tools():
    tools = agent.list_available_tools()
    return jsonify({"tools": tools})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50001, debug=True)
