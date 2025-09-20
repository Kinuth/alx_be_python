task = input("What task do you want to be reminded of? ")
priority = input("Is it high, medium, or low priority? ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()
match (priority):
    case ("high"):
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task}  is a low priority task. Consider completing it when you have free time..")