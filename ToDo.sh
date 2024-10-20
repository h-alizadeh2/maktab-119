#!/bin/bash

TODO_FILE="todo_list.txt"

function show_menu() {
    echo "========================"
    echo "      ToDo List        "
    echo "========================"
    echo "1. Add a task"
    echo "2. View tasks"
    echo "3. Delete a task"
    echo "4. Exit"
    echo "========================"
}

function add_task() {
    read -p "Enter the task: " task
    echo "$task" >> "$TODO_FILE"
    echo "Task added."
}

function view_tasks() {
    if [ ! -f "$TODO_FILE" ]; then
        echo "No tasks found."
        return
    fi

    echo "Your tasks:"
    nl "$TODO_FILE"
}

function delete_task() {
    view_tasks
    if [ ! -f "$TODO_FILE" ]; then
        return
    fi

    read -p "Enter the task number to delete: " task_num
    sed -i "${task_num}d" "$TODO_FILE"
    echo "Task deleted."
}

while true; do
    show_menu
    read -p "Choose an option: " option

    case $option in
        1) add_task ;;
        2) view_tasks ;;
        3) delete_task ;;
        4) echo "Goodbye!"; exit ;;
        *) echo "Invalid option! Please try again." ;;
    esac
done

