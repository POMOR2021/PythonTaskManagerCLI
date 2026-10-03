import sys
import os
import json


def add_task(task: dict):
    filename = "task_list.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r", encoding="utf-8", errors="replace") as file:
            try:
                tasks = json.load(file)
                if not isinstance(tasks, list):
                    tasks = []
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

    tasks.append(task)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def del_task(index: int):
    filename = "task_list.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, "r", encoding = "utf-8", errors = "replace") as file:
                data = json.load(file)
            data.pop(index - 1)
            with open(filename, "w", encoding="utf-8", errors="replace") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("Заипиь удалена")
        except json.JSONDecodeError:
            print("Sorry, error")
    else:
        print("Sorry, list is empty")


def print_tasks():
    filename = "task_list.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, "r", encoding="utf-8", errors="replace") as file:
                tasks = json.load(file)
            for task in tasks:
                status = "In progress" if task['status'] == 1 else "Done"
                print(f"ID: {task['index']} - {task['text']}\nStatus: {status}")
                print("-" * 20)
        except json.JSONDecodeError:
            print("Sorry, error")
    else:
        print("Sorry, list is empty")

def update_task(index: int):
    filename = "task_list.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, "r", encoding="utf-8", errors="replace") as file:
                data = json.load(file)
            for task in data:
                if task['index'] == index:
                    print("Введите новый текст")
                    text = input()
                    print("Введите новый статус")
                    status = int(input())
                    task['text'] = text
                    task['status'] = status
            with open(filename, "w", encoding="utf-8", errors="replace") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("Update task successfully")
        except json.JSONDecodeError:
            print("Sorry, error")
    else:
        print("Sorry, list is empty")


if len(sys.argv) < 2:
    print("Please enter a command. If you need see command list enter \"--help\"")
else:
    print("Welcome in Task Manager.\n-------------------------\nBeautiful life for our world")
    match sys.argv[1]:
        case "--help":
            print("All commands list:\n1.add - Add task in your task list\n2.list - See your task list\n3.del - Delete task in task list\n4.upd - Update your task")
        case "add":
            print("Please input index for your task")
            index = int(input())
            print("Please input text for your task")
            text = input()
            print("Please input status for your task(in number).\n1. In progress\n2. Done")
            status = int(input())
            add_task({"index": index, "text": text, "status": status})
        case "list":
            print_tasks()
        case "del":
            print("Please input index for your task")
            index = int(input())
            del_task(index)
        case "upd":
            print("Please input index for your task")
            index = int(input())
            update_task(index)
        case _:
            print("Input incorrect command")