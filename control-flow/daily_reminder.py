# Prompt the user for task details
task = input("Enter the task description: ").strip()
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Generate a customized reminder
match priority:
    case "high":
        reminder = f"The task '{task}' is a high-priority task."
    case "medium":
        reminder = f"The task '{task}' is a medium-priority task."
    case "low":
        reminder = f"The task '{task}' is a low-priority task."
    case _:
        reminder = f"The task '{task}' has an unknown priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the reminder
print(reminder)
