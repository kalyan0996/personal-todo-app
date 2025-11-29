Personal To-Do List Application

Overview
This is a Personal To-Do List Application developed as part of the VaultofCodes internship project. It allows users to create, view, edit, and delete tasks using a simple command-line interface. All data is persisted in a local JSON file.

Features
Add Tasks: Users can add tasks with a title, description, and category.
View Tasks: Display a list of all current tasks with their status.
Categorization: Tasks can be organized by categories (e.g., Work, Personal, Urgent).
Persistence: Data is saved automatically to tasks.json so progress is never lost.
Task Management: Mark tasks as completed or delete them entirely.

Project Structure
todo.py: The main Python script containing the application logic.
tasks.json: A JSON file used to store the task data.
README.md: Project documentation.

How to Run
Ensure you have Python installed on your machine.
Download todo.py and tasks.json to the same folder.
Open a terminal or command prompt in that folder.
Run the application:
         python todo.py


Usage Guide
Launch the App: Run the script to see the main menu.
Add a Task: Select option 1 and enter the task details.
Save & Exit: Always use option 5 to exit, which ensures your changes are saved to the file.
