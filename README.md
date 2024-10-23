# ToDo Application

## Overview
This ToDo application allows users to manage tasks through a simple text-based interface. Users can add, display, move, remove, and search for tasks across different lists: incomplete, completed, and deleted.

## Features
- **Add New Tasks**: Easily add tasks to the incomplete tasks list.
- **Display Incomplete Tasks**: View all tasks that are yet to be completed.
- **Move Tasks to Completed**: Transfer tasks from the incomplete list to the completed list and remove them from the former.
- **Display Completed Tasks**: View all successfully completed tasks.
- **Remove Tasks**: Delete a task and move it to the deleted tasks list.
- **Display Deleted Tasks**: View all tasks that have been deleted.
- **Search Functionality**: Search for tasks in the incomplete, completed, and deleted lists.
- **Task Priorities**: Assign priorities to tasks (1 to 3).
- **Date and Time Stamp**: Include date and time information with tasks.

## Files
The application uses three text files to store tasks:
- `incomplete_tasks.txt`
- `completed_tasks.txt`
- `deleted_tasks.txt`

If any of these files do not exist, the program will create them automatically.

## Running the Program
1. Clone this repository.
2. Navigate to the project directory.
3. Run the application using Python:
```bash
python todo.py

