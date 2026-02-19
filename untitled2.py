from modules.task_manager import *

tasks = {
    "task 1" : "low",
    "task 2" : "medium",
    "task 3" : "high",
    "task 4" : "medium",
    "task 5" : "low",
    "task 6" : "high"
}

print(add_task(tasks, "task 7", "low"))
print(add_task(tasks, "task 8", "medium"))
print(add_task(tasks, "task 9", "high"))
print(remove_task(tasks, "task 243"))
print(get_tasks_by_priority(tasks, "high"))
print(count_tasks(tasks))