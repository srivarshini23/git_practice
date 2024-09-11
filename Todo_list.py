print("Your To-Do List")
New_list = []

while True:
    task = input("Enter the Task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    New_list.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(New_list, start=1):
    print(f"{i}. {task}")
