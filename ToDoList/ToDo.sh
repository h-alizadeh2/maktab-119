#!/bin/bash

# Define file locations
INCOMPLETE_FILE="incomplete_tasks.txt"  
COMPLETED_FILE="completed_tasks.txt"
DELETED_FILE="deleted_tasks.txt"

# Ensure the necessary files exist
touch "$INCOMPLETE_FILE" "$COMPLETED_FILE" "$DELETED_FILE"

# Function to display the menu
show_menu() {
    echo "Todo List Menu:"
    echo "1. Add a new task"
    echo "2. Display incomplete tasks"
    echo "3. Mark a task as completed"
    echo "4. Display completed tasks"
    echo "5. Remove a task (add to deleted tasks)"
    echo "6. Display deleted tasks"
    echo "7. Search tasks"
    echo "8. Exit"
}

# Function to add a new task
add_task() {
    read -p "Enter the task description: " description
    read -p "Enter priority (1-3): " priority
    date_time=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$date_time | Priority: $priority | $description" >> "$INCOMPLETE_FILE"
    echo "Task added."
}

# Function to display incomplete tasks
display_incomplete() {
    echo "Incomplete Tasks:"
    cat "$INCOMPLETE_FILE"
}

# Function to mark a task as completed
complete_task() {
    display_incomplete
    read -p "Enter the line number of the task to mark as completed: " line_number
    sed -n "${line_number}p" "$INCOMPLETE_FILE" > temp_task.txt
    if [ -s temp_task.txt ]; then
        echo "$(cat temp_task.txt)" >> "$COMPLETED_FILE"
        sed -i "${line_number}d" "$INCOMPLETE_FILE"
        echo "Task marked as completed."
    else
        echo "Invalid line number."
    fi
    rm temp_task.txt
}

# Function to display completed tasks
display_completed() {
    echo "Completed Tasks:"
    cat "$COMPLETED_FILE"
}

# Function to remove (delete) a task
remove_task() {
    display_incomplete
    read -p "Enter the line number of the task to delete: " line_number
    sed -n "${line_number}p" "$INCOMPLETE_FILE" > temp_task.txt
    if [ -s temp_task.txt ]; then
        echo "$(cat temp_task.txt)" >> "$DELETED_FILE"
        sed -i "${line_number}d" "$INCOMPLETE_FILE"
        echo "Task removed."
    else
        echo "Invalid line number."
    fi
    rm temp_task.txt
}

# Function to display deleted tasks
display_deleted() {
    echo "Deleted Tasks:"
    cat "$DELETED_FILE"
}

# Function to search tasks in the specified list
search_tasks() {
    read -p "Search in (incomplete/completed/deleted): " list
    read -p "Enter search term: " term
    case $list in
        incomplete)
            echo "Searching in Incomplete Tasks:"
            grep -i "$term" "$INCOMPLETE_FILE"
            ;;
        completed)
            echo "Searching in Completed Tasks:"
            grep -i "$term" "$COMPLETED_FILE"
            ;;
        deleted)
            echo "Searching in Deleted Tasks:"
            grep -i "$term" "$DELETED_FILE"
            ;;
        *)
            echo "Invalid list."
            ;;
    esac
}

# Main loop
while true; do
    show_menu
    read -p "Choose an option (1-8): " option
    case $option in
        1) add_task ;;
        2) display_incomplete ;;
        3) complete_task ;;
        4) display_completed ;;
        5) remove_task ;;
        6) display_deleted ;;
        7) search_tasks ;;
        8) exit 0 ;;
        *) echo "Invalid option. Please try again." ;;
    esac
    echo ""
done
