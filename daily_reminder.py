# Prompt user for task description, priority, and time sensitivity
task = input("Enter the task description: ")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        priority_message = "This is a high-priority task."
    case "medium":
        priority_message = "This task is of medium priority."
    case "low":
        priority_message = "This is a low-priority task."
    case _:
        priority_message = "Unknown priority."

# Check if the task is time-bound and update reminder accordingly
if time_bound == "yes":
    time_bound_message = "This task requires immediate attention today!"
else:
    time_bound_message = "No immediate action required."

# Print a customized reminder message
print(f"Task: {task}\nPriority: {priority_message}\n{time_bound_message}")

