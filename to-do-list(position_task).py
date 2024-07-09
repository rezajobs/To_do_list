# Input tasks from the user
task_list = input('Add all the tasks for today, separated by a dash (-): ').split('-')

# Input the task to find its position
position_task = input('Which task do you want to find the position of? ')

# Find the position of the task
if position_task in task_list:
    task_position = task_list.index(position_task)+1
    print(f"The position of '{position_task}' in the list is: {task_position}")
else:
    print(f"The task '{position_task}' is not in the list.")
