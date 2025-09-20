task = input("What task do you want to be reminded of? ")
priority = input("Is it high, medium, or low priority? ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()
match priority:
    case ("high"):
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task}  is a low priority task. Consider completing it when you have free time..")
    case ("medium"):
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task. Try to complete it within the next few days.")
        else:
            print(f"Reminder: {task} is a medium priority task. You can schedule it for later this week.")
    case ("low"):
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task. You can complete it at your convenience.")
        else:
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please choose high, medium, or low.")
# This program sets a daily reminder based on task priority and time sensitivity.