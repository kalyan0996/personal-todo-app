# Personal To-Do List Application

## Overview
A Personal To-Do List Application with both CLI and Web interfaces. Originally developed as part of a VaultofCodes internship project.

## Features
- Add tasks with title, description, and category
- View all tasks with their status
- Mark tasks as completed or toggle back to pending
- Delete tasks
- Data persists automatically to JSON file

## How to Run

### Web Application (Recommended)
1. Install dependencies: `pip install flask`
2. Run: `python app.py`
3. Open browser at `http://localhost:5000`

### CLI Application
1. Run: `python todo.py`
2. Follow the on-screen menu

## Project Structure
- `app.py` - Flask web application
- `todo.py` - Original CLI application
- `tasks.json` - Task data storage
- `templates/` - HTML templates
- `static/` - CSS styles

## Categories
- Work, Personal, Urgent, Other
