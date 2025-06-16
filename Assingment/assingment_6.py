task = {}
task_id = 1

print("======Task Bar==========")
print("1. 'Add task'")
print("2. 'update task'")
print("3. 'delete task'")

task_name = input("Enteer the task name : ")
task[task_id] = task_name
print(f"Task added with id : {task_id}")
task_id+= 1
task_name = input("Enteer the task name : ")
task[task_id] = task_name
print(f"Task added with id : {task_id}")
task_id+= 1
task_name = input("Enteer the task name : ")
task[task_id] = task_name
print(f"Task added with id : {task_id}")

choice = input("Enter Your choice from (2-3): ")

if choice == "2":
    task_num = int(input("Enter the task id in number: "))
    if task_num in task:
        new_task = input("Enter the new task : ")
        task[task_num] = new_task
        print("task update successfull.")

    else:
        print("Invalid Task_id")

elif choice == "3":
    task_num = int(input("Enter the task id in number: "))
    if task_num in task:
        del task[task_num]
        print("deletion successfull.")
    else:
        print('\nTask_id is invalid')    

else:
    print("Invalid choice.")


if not task :
    print("No task available") 
else:
    print(task)       