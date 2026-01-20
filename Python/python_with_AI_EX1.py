# Initialize lists to store tasks
daily_checklist = []
completed_tasks = []
incomplete_tasks = []

print("Welcome to your Daily Task Organizer!")
print("Please enter your tasks one by one. Type 'done' when you have finished adding all tasks.")

# Step 1: Create the daily checklist
while True:
    task = input("Enter a task: ")
    if task.lower() == 'done':
        break
    if task.strip(): # Ensure the task is not empty
        daily_checklist.append(task.strip())

if not daily_checklist:
    print("No tasks were added for today. Exiting.")
else:
    print("\n--- Your Daily Checklist ---")
    for i, task in enumerate(daily_checklist):
        print(f"{i+1}. {task}")

    print("\n--- Reviewing Tasks ---")
    print("For each task, type 'y' if it was completed, or 'n' if it was not.")

    # Step 2: Review and categorize tasks
    for task in daily_checklist:
        while True:
            response = input(f"Was '{task}' completed? (y/n): ").lower()
            if response == 'y':
                completed_tasks.append(task)
                break
            elif response == 'n':
                incomplete_tasks.append(task)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # Step 3: Display the results
    print("\n--- Daily Summary ---")

    print("\nCompleted Tasks:")
    if completed_tasks:
        for i, task in enumerate(completed_tasks):
            print(f"{i+1}. {task}")
    else:
        print("  No tasks completed today.")

    print("\nIncomplete Tasks:")
    if incomplete_tasks:
        for i, task in enumerate(incomplete_tasks):
            print(f"{i+1}. {task}")
    else:
        print("  All tasks completed today! Well done.")

"""Welcome to your Daily Task Organizer!
Please enter your tasks one by one. Type 'done' when you have finished adding all tasks.
Enter a task: enter code to Git
Enter a task: re-watch sat session
Enter a task: complete assignment
Enter a task: learn about LLM and RAG
Enter a task: Done

--- Your Daily Checklist ---
1. enter code to Git
2. re-watch sat session
3. complete assignment
4. learn about LLM and RAG

--- Reviewing Tasks ---
For each task, type 'y' if it was completed, or 'n' if it was not.
Was 'enter code to Git' completed? (y/n): n
Was 're-watch sat session' completed? (y/n): y
Was 'complete assignment' completed? (y/n): y
Was 'learn about LLM and RAG' completed? (y/n): n

--- Daily Summary ---

Completed Tasks:
1. re-watch sat session
2. complete assignment

Incomplete Tasks:
1. enter code to Git
2. learn about LLM and RAG
"""
