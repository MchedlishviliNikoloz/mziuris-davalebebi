def add_task(tasks: dict, title: str, priority: str) -> dict:
    li = ["low", "medium", "high"]
    if priority.lower() not in li:
        while priority.lower() not in li:
            priority = input("შემოიყვანეთ სწორი ფორმით დავალების პრიორიტეტობა (low, medium, high): ")
    tasks[title] = priority.lower()
    return tasks

def remove_task(tasks: dict, title: str) -> dict | None :
    try:
        del tasks[title]
        return tasks
    except KeyError:
        print(f"დავალება '{title}' არ არის სიაში.")
        return None

def get_tasks_by_priority(tasks: dict, priority: str) -> list[str]:
    li = ["low", "medium", "high"]
    if priority.lower() not in li:
        while priority.lower() not in li:
            priority = input("შემოიყვანეთ სწორი ფორმით დავალების პრიორიტეტობა (low, medium, high): ")
    filtered_tasks = [key for key, value in tasks.items() if value == priority.lower()]
    return filtered_tasks

def count_tasks(tasks: dict) -> int:
    return len(tasks)

if __name__ == "__main__":
    d = {"task" : "low"}
    print(count_tasks(d))