from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    """Display all tasks."""
    tasks = load_tasks()
    categories = ['Work', 'Personal', 'Urgent', 'Other']
    return render_template('index.html', tasks=tasks, categories=categories)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task."""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    category = request.form.get('category', 'Other')
    
    if not title:
        flash('Task title is required!', 'error')
        return redirect(url_for('index'))
    
    tasks = load_tasks()
    new_task = {
        'title': title,
        'description': description,
        'category': category,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    flash(f'Task "{title}" added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        flash('Task marked as completed!', 'success')
    else:
        flash('Task not found!', 'error')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        removed = tasks.pop(task_id)
        save_tasks(tasks)
        flash(f'Task "{removed["title"]}" deleted!', 'success')
    else:
        flash('Task not found!', 'error')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
        save_tasks(tasks)
        status = 'completed' if tasks[task_id]['completed'] else 'pending'
        flash(f'Task marked as {status}!', 'success')
    else:
        flash('Task not found!', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
