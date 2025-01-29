import tkinter as tk
from tkinter import messagebox
import json

# Path to the tasks file
TASKS_FILE = 'tasks.json'

# Function to load tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Function to display tasks in the listbox
def display_tasks():
    tasks = load_tasks()
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔ Done" if task['completed'] else "✘ Not Done"
        listbox.insert(tk.END, f"{task['title']} - {status}")

# Function to add a new task
def add_task():
    title = task_entry.get()
    if title:
        tasks = load_tasks()
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        display_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task title.")

# Function to mark a task as completed
def mark_task_as_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks = load_tasks()
        task = tasks[task_index]
        task['completed'] = True
        save_tasks(tasks)
        display_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Set up the main window
window = tk.Tk()
window.title("To-Do List Application")
window.geometry("600x400")  # Adjust window size
window.configure(bg="#f0f0f0")  # Background color

# Add a header label
header_label = tk.Label(window, text="To-Do List", font=("Helvetica", 24, "bold"), bg="#4CAF50", fg="white")
header_label.pack(fill=tk.X, pady=20)

# Set up the task entry widget
task_entry_label = tk.Label(window, text="Enter Task Title:", font=("Helvetica", 12), bg="#f0f0f0")
task_entry_label.pack(pady=5)

task_entry = tk.Entry(window, width=40, font=("Helvetica", 12))
task_entry.pack(pady=10)

# Set up the buttons with custom colors
add_task_button = tk.Button(window, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat", width=20)
add_task_button.pack(pady=5)

mark_done_button = tk.Button(window, text="Mark Task as Completed", command=mark_task_as_completed, bg="#2196F3", fg="white", font=("Helvetica", 12), relief="flat", width=20)
mark_done_button.pack(pady=5)

# Set up the listbox to display tasks
listbox_label = tk.Label(window, text="Your Tasks:", font=("Helvetica", 12), bg="#f0f0f0")
listbox_label.pack(pady=5)

listbox = tk.Listbox(window, width=50, height=10, font=("Helvetica", 12), selectmode=tk.SINGLE, bd=2, relief="sunken", bg="#ffffff", fg="#333333", highlightbackground="#4CAF50")
listbox.pack(pady=10)

# Set up the display of tasks on startup
display_tasks()

# Start the Tkinter event loop
window.mainloop()
