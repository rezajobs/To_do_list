# Get the number of tasks to be done
To_do_list_number = int(input('How many tasks should you do today? : '))

# Initialize an empty list to store the tasks
task_list = []

# Collect each task
for i in range(To_do_list_number):
    task_step = input('Task ' + str(i+1) + ': ')
    task_list.append(task_step)

# Print the list of tasks
print('your task for today is :',task_list)

print([task_list])

#Ask if each task is completed
for i,task in enumerate(task_list):
    completed = input(f"Have you completed the task '{task}'? (yes/no): ")
    if completed.lower()== 'yes':
        print(f"good job for completing task {i+1}:'{task}'!")
    else:
        print(f"Task {i+1} ('{task}') is still pending. Keep going!")

print("Task check complete. Good luck with the rest of your tasks!")
