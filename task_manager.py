"""
Notes: 
    1. Use the following username and password to access the admin rights:
            username: admin
            password: password
    2. Needs tasks.txt and user.txt in the same folder.
"""

import os
from datetime import datetime


def print_line(character, length):
    """
    The function 'print_line' takes a character and a length as input and prints a line made up of that
    character repeated for the specified length.
    
    :param character: The 'character' parameter is the symbol or character that will be used to create
    the line when the 'print_line' function is called
    :param length: The 'length' parameter represents the number of times the 'character' will be
    repeated to create the line that will be printed
    """
    line = character * length
    character = "-"
    length = 80
    print(line)


def reg_user(username_password):
    """
    The 'reg_user' function allows a user to register a new username and password, and stores the
    information in a dictionary and a text file.
    
    :param username_password: The 'username_password' parameter is a dictionary that stores the
    usernames as keys and their corresponding passwords as values
    """
    while True:
        new_username = input("New Username: ")
        if new_username in username_password.keys():
            print("Username already exists. Please try a different username.")
        else:
            new_password = input("New Password: ")
            confirm_password = input("Confirm Password: ")
    
            if new_password == confirm_password:
                print("New user added")
                username_password[new_username] = new_password
        
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
                    break
            else:
                print("Passwords do not match")


def add_task(username_password, task_list):
    """
    The 'add_task' function allows a user to add a new task to a task list, including the username of
    the person assigned to the task, the title and description of the task, the due date, and the
    assigned date.
    
    :param username_password: The 'username_password' parameter is a dictionary that stores the
    usernames and passwords of users. The keys of the dictionary are the usernames, and the values are
    the corresponding passwords
    :param task_list: The 'task_list' parameter is a list that contains dictionaries representing tasks.
    Each dictionary represents a task and contains the following keys: 'username', 'title',
    'description', 'due_date', 'assigned_date', and 'completed'
    :return: The function does not explicitly return anything.
    """
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    
    curr_date = datetime.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all(task_list):
    """
    The function 'view_all' takes a list of tasks and displays information about each task in a
    formatted way.
    
    :param task_list: The 'task_list' parameter is a list of dictionaries, where each dictionary
    represents a task. Each task dictionary should have the following keys: 'title', 'username',
    'assigned_date', 'due_date', and 'description'
    """
    for t in task_list:
        disp_str = f"Task: \t\t\t {t['title']}\n"
        disp_str += f"Assigned to: \t\t {t['username']}\n"
        disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"\nTask Description: \t {t['description']}\n"
        print_line()
        print(disp_str)


def view_mine(task_list, curr_user):
    """
    The 'view_mine' function displays tasks assigned to the current user, allows selection of a task for
    editing or marking as complete, and provides options to edit the task's details.
    
    :param task_list: The 'task_list' parameter is a list of dictionaries
    where each dictionary represents a task. Each task dictionary contains the following keys:
    :param curr_user: The 'curr_user' parameter represents the current user who is viewing their
    assigned tasks. This parameter is used to filter and display only the tasks
    that are assigned to the current user in the task list.
    :return: The 'view_mine' function does not explicitly return any value. It contains a return
    statement with no value specified, which means it will exit the function without returning anything
    when the user inputs "-1" to return to the main menu.
    """
    task_index = 1
    task_indices = {}

    print("\nTasks assigned to you:\n")
    print_line("-", 80)
    for i, t in enumerate(task_list):
        if t['username'] == curr_user:
            task_indices[task_index] = i
            print(f"{task_index}. Task: \t\t{t['title']}")
            print(f"   Assigned to: \t{t['username']}")
            print(f"   Date Assigned: \t{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"   Due Date: \t\t{t['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"   Task Description: \t{t['description']}")
            print(f"   Completed: \t\t{'Yes' if t['completed'] else 'No'}")
            task_index += 1
            print_line("-", 80)


    while True:
        choice = input("\nEnter the number of the task you want to select, or -1 to return to the main menu: ")

        if choice == "-1":
            return
        elif choice.isdigit():
            choice = int(choice)
            if choice in task_indices:
                selected_task_index = task_indices[choice]
                selected_task = task_list[selected_task_index]

                if selected_task['completed']:
                    print("\nThis task has already been completed and cannot be edited.")
                else:
                    edit_choice = input("\nEnter 'c' to mark the task as complete, 'e' to edit the task, or 'b' to go back: ").lower()
                    if edit_choice == 'c':
                        selected_task['completed'] = True
                        update_tasks_file(task_list) # Updates 'tasks' file
                        print("\nTask marked as complete!")
                    elif edit_choice == 'e':
                        edit_field = input("\nEnter 'username' to edit the username, 'due date' to edit the due date, or 'b' to go back: ").lower()
                        if edit_field == 'username':
                            new_username = input("\nEnter the new username: ")
                            selected_task['username'] = new_username
                            update_tasks_file(task_list) # Updates 'tasks' file
                            print("\nUsername updated!")
                        elif edit_field.lower() == 'due date':
                            while True:
                                try:
                                    new_due_date = input("\nEnter the new due date (YYYY-MM-DD): ")
                                    selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                    update_tasks_file(task_list) # Updates 'tasks' file
                                    print("\nDue date updated!")
                                    break
                                except ValueError:
                                    print("\nInvalid datetime format! Please use the format specified.")
                        elif edit_field == 'b':
                            continue
                        else:
                            print("\nInvalid choice. Please try again.")
                    elif edit_choice == 'b':
                        continue
                    else:
                        print("\nInvalid choice. Please try again.")
            else:
                print("\nInvalid task number. Please try again.")
        else:
            print("\nInvalid input. Please enter a number or -1 to return to the main menu.")


def update_tasks_file(task_list):
    """
    The function 'update_tasks_file' writes task details from a list to a file in a specific format.
    
    :param task_list: the 'update_tasks_file' function is designed to update a file named
    'tasks.txt' with the contents of the 'task_list'. The function iterates over each task in the
    'task_list' and writes the task details in a specific format to the file
    """
    with open('tasks.txt', 'w') as task_file:
        for task in task_list:
            task_file.write(f"{task['username']};{task['title']};{task['description']};{task['due_date'].strftime(DATETIME_STRING_FORMAT)};{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if task['completed'] else 'No'}\n")


def generate_reports(task_list, username_password):
    """
    The function 'generate_reports' creates task and user overview reports based on task list and
    username-password dictionary input.
    
    :param task_list: The 'task_list' parameter is a list of dictionaries where each dictionary
    represents a task. Each task dictionary contains information such as the task's title, description,
    due date, completion status, and the username of the user to whom the task is assigned
    :param username_password: The 'username_password' parameter is a dictionary that contains usernames
    as keys and corresponding passwords as values. This dictionary is used to generate a report on the
    tasks assigned to each user, along with their completion status and other relevant statistics
    """
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    uncompleted_tasks = total_tasks - completed_tasks
    today = datetime.today()
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'] < today)
    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100 if total_tasks != 0 else 0
    percentage_overdue = (overdue_tasks / total_tasks) * 100 if total_tasks != 0 else 0

    total_users = len(username_password)

    
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("Tasks Overview:\n\n")
        task_overview_file.write("-"*80)
        task_overview_file.write("\n\n")
        task_overview_file.write(f"Total number of tasks: {total_tasks}\n")
        task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
        task_overview_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        task_overview_file.write(f"Total number of overdue incompleted tasks: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of incomplete tasks: {percentage_incomplete:.2f}%\n")
        task_overview_file.write(f"Percentage of overdue tasks: {percentage_overdue:.2f}%\n")
        
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write("Users Overview:\n\n")
        user_overview_file.write(f"Total number of users: {total_users}\n")
        user_overview_file.write(f"Total number of tasks: {total_tasks}\n\n")
        user_overview_file.write("-"*80)
        user_overview_file.write("\n\n")



        for username, password in username_password.items():
            user_tasks = sum(1 for task in task_list if task['username'] == username)
            user_completed_tasks = sum(1 for task in task_list if task['username'] == username and task['completed'])
            user_percentage_tasks = (user_tasks / total_tasks) * 100 if total_tasks != 0 else 0
            user_percentage_completed = (user_completed_tasks / user_tasks) * 100 if user_tasks != 0 else 0
            user_percentage_remaining = 100 - user_percentage_completed
            user_overdue_tasks = sum(1 for task in task_list if task['username'] == username and not task['completed'] and task['due_date'] < today)
            user_percentage_overdue = (user_overdue_tasks / user_tasks) * 100 if user_tasks != 0 else 0


            user_overview_file.write(f"Username: {username}\n")
            user_overview_file.write(f"Password: {password}\n\n")
            user_overview_file.write(f"Total number of tasks assigned: {user_tasks}\n")
            user_overview_file.write(f"Percentage of total tasks assigned: {user_percentage_tasks:.2f}%\n")
            user_overview_file.write(f"Percentage of completed tasks: {user_percentage_completed:.2f}%\n")
            user_overview_file.write(f"Percentage of tasks remaining: {user_percentage_remaining:.2f}%\n")
            user_overview_file.write(f"Percentage of overdue tasks: {user_percentage_overdue:.2f}%\n")
            user_overview_file.write("-"*80)
            user_overview_file.write("\n\n")


def display_statistics():
    """
    The 'display_statistics' function reads and displays task and user overview reports from files,
    generating them if they don't exist.
    """
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports(task_list, username_password)

    with open("task_overview.txt", "r") as task_overview_file:
        task_overview = task_overview_file.read()
        print(f"\n{task_overview}")

    print_line("-", 80)

    with open("user_overview.txt", "r") as user_overview_file:
        user_overview = user_overview_file.read()
        print(f"\n{user_overview}")


def print_menu():
    """
    The 'print_menu' function displays a menu with options for registering users, adding tasks, viewing
    tasks, generating reports, displaying statistics, and exiting the program based on user input.
    """
    while True:
        print()
        print(" "*(30-(len(title)//2)), title)
        print_line("-", 64)
        menu = input('''
    \tR   -  Register user
    \tA   -  Add task
    \tVA  -  View all tasks
    \tVM  -  View my tasks
    \tGR  -  Generate reports
    \tDS  -  Display statistics
    \tE   -  Exit

    \tEnter choice: ''').lower()
        
        if menu == 'r':
            reg_user(username_password)
        elif menu == 'a':
            add_task(username_password, task_list)
        elif menu == 'va':
            view_all(task_list)
        elif menu == 'vm':
            view_mine(task_list, curr_user)
        elif menu == 'gr' and curr_user == 'admin': # onlly available to admin
            generate_reports(task_list, username_password)
        elif menu == 'ds' and curr_user == 'admin': # onlly available to admin
            display_statistics()  
        elif menu == 'e':
            print('\n\tGoodbye!!!')
            exit()
        else:
            print("\n\tYou have made a wrong choice. Please try again!")


DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


# --- Login Section ---

#This code reads usernames and password from the user.txt file to allow a user to login.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True



title = "Please select one of the following options:"





print_menu()
