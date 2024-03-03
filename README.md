# Task Management System

Welcome to the Task Management System! This Python project allows users to register, add tasks, view tasks, generate reports, and display statistics. It provides an organized way to manage tasks and user information.

- [Installation](#installation)
- [Usage](#usage)
  - [User Registration](#user-registration)
  - [Adding Tasks](#adding-tasks)
  - [Viewing Tasks](#viewing-tasks)
  - [Viewing Personal Tasks](#viewing-personal-tasks)
  - [Generating Reports](#generating-reports-admin-only)
  - [Displaying Statistics](#displaying-statistics-admin-only)
  - [Exiting the Program](#exiting-the-program)
- [Notes](#notes)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-management-system.git
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `tasks.txt` and `user.txt` files are in the same folder as the Python scripts.

## Usage

### User Registration
- To register as a new user, run the script and choose option 'R'.
- Enter a unique username and password when prompted.

### Adding Tasks
- Select option 'A' to add a new task.
- Enter details such as task title, description, due date, and the person assigned to the task.
- The task will be added to the task list.

### Viewing Tasks
- Choose 'VA' to view all tasks.
- See a formatted display of all tasks including title, assigned user, due date, and description.

### Viewing Personal Tasks
- Select 'VM' to view tasks assigned to you.
- Edit tasks or mark them as complete.

### Generating Reports (Admin Only)
- Admin users (username: admin, password: password) can generate reports using 'GR'.
- Reports include task overviews and user statistics.
  
### Displaying Statistics (Admin Only)
- Admins can view task and user overview reports with option 'DS'.

### Exiting the Program
- To exit the program, choose option 'E'.

## Notes
- Admin access is granted using the following credentials:
  - Username: admin
  - Password: password

- Make sure `tasks.txt` and `user.txt` files are present in the project folder.
- Use `DATETIME_STRING_FORMAT = "%Y-%m-%d"` for date formatting.

## Examples

Here are a few examples to get you started:

### Registering a New User
```bash
$ python main.py
...
    R   -  Register user
    A   -  Add task
    ...
Enter choice: R

New Username: new_user
New Password: mypassword
Confirm Password: mypassword

New user added
```

### Adding a Task
```bash
$ python main.py
...
    R   -  Register user
    A   -  Add task
    ...
Enter choice: A

Name of person assigned to task: new_user
Title of Task: Complete Project Proposal
Description of Task: Draft a detailed project proposal document.
Due date of task (YYYY-MM-DD): 2024-04-30

Task successfully added.
```

### Viewing All Tasks
```bash
$ python main.py
...
    VA  -  View all tasks
    VM  -  View my tasks
    ...
Enter choice: VA

Task:           Complete Project Proposal
Assigned to:    new_user
Date Assigned:  2024-03-03
Due Date:       2024-04-30

Task Description:  Draft a detailed project proposal document.

-------------------------------------------------------------------------------
...
```

## Dependencies
- Python 3.x

## Contributing
Contributions are welcome! If you have any suggestions or find bugs, please open an issue or create a pull request.
