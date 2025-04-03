
document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const outputArea = document.getElementById('outputArea');
    
    taskForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const task = taskInput.value.trim();
        if (!task) {
            outputArea.innerHTML = '<div class="error-message">Please enter a task</div>';
            return;
        }
        
        // Show loading indicator
        outputArea.innerHTML = '<div>Processing your task...</div>';
        
        // Send request to backend
        fetch('/api/run_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task: task })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                outputArea.innerHTML = `<div class="error-message">Error: ${data.error}</div>`;
                return;
            }
            
            let output = `<div>
                <h3>Response:</h3>
                <p>${data.result.response || 'Task completed successfully'}</p>
            </div>`;
            
            if (data.result.output) {
                output += `<div class="tool-output">
                    <h3>Output:</h3>
                    <pre>${data.result.output}</pre>
                </div>`;
            }
            
            if (data.result.tool_used) {
                output += `<div><small>Tool used: ${data.result.tool_used}</small></div>`;
            }
            
            outputArea.innerHTML = output;
        })
        .catch(error => {
            outputArea.innerHTML = `<div class="error-message">Network error: ${error.message}</div>`;
        });
    });
});
