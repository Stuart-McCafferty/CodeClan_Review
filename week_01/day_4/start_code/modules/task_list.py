# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    return get_tasks_by_status(list, False)

## Get a list of completed tasks
def get_completed_tasks(list):
    return get_tasks_by_status(list, False)


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    result_tasks = []
    for item in list:
        if item["time_taken"] >= time:
            result_tasks.append(item)
    return result_tasks

## Find a task with a given description
def get_task_with_description(list, description):
    for item in list:
        if item["description"] == description:
            return item


# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    status_list = []
    for item in list:
        if item["completed"] == status:
            status_list.append(item)
    return status_list

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

