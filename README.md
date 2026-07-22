[![Test Multiple Python Versions](https://github.com/Nesmakamalsh/Python_for_Devops/actions/workflows/main.yml/badge.svg)](https://github.com/Nesmakamalsh/Python_for_Devops/actions/workflows/main.yml)
# Python_for_Devops
## Create a project scaffold

* Create development environment that is cloud-based:
### [Colab notebook] (https://github.com/Nesmakamalsh/Python_for_Devops/blob/main/Python_for_Devops.ipynb)
### Github code spaces

Build out python project scaffold:

#### [Makefile]: (https://github.com/Nesmakamalsh/Python_for_Devops/blob/main/Makefile)
  * It automates build steps (like compiling and linking code) by listing targets (what to build), prerequisites (what’s needed), and recipes (commands to run)
  * It tracks dependencies so make only recompiles files that have changed, saving time and avoiding unnecessary work
  * It can also run other tasks (e.g., cleaning up files, generating data) when requested
#### [requirements.txt] (https://github.com/Nesmakamalsh/Python_for_Devops/blob/main/requirements.txt)
#### [test_library.py] (https://github.com/Nesmakamalsh/Python_for_Devops/blob/main/test_devopslib.py)
#### [python_library] (https://github.com/Nesmakamalsh/Python_for_Devops/tree/main/devopslib)
**Python Libraries**
1. `pylint` — Code Quality Checker (Linter)
pylint analyzes your Python code and looks for:
>Syntax errors  
>Bugs and bad practices    
>Style violations  
>Unused variables/imports  
>Missing documentation  

2. `pytest` — Testing Framework
pytest is used to write and run tests.
>Ex: 
def add(a, b):  
    return a + b  

>Test file:  
def test_add():  
    assert add(2, 3) == 5  

pytest runs the test, and output is: ``passed``

3. ``black`` — Code Formatter
black automatically reformats Python code into a consistent style.

4. ``fire`` Python Fire is a simple way to create a CLI in Python. Fire is a helpful tool for developing and debugging Python code. it helps with exploring existing code or turning other people's code into a CLI, and it makes transitioning between Bash and Python easier.

>if __name__ == '__main__':  
    fire.Fire(hello)  

Python sets a special variable called  `__name__` .

If you run the file directly:  
`python app.py`  
then:
__name__ == "__main__"  
If you import the file from another script:
`import app`  
then:
__name__ == "app"

So it means only execute the code below if this file is being run directly.
Fire automatically converts Python functions into command-line interfaces (CLI).
Then you can run:  
`python app.py John`  
and get:  
`Hello John`  
Fire automatically: reads command-line arguments,
Calls hello() func,
Passes arguments to the function,
Prints the result.
#### Dockerfile
#### command_line_tool
#### Microservice

1. Create a virtualenv `virtualenv ~/.venv`

* `virtualenv` Command: virtualenv is a Python tool that creates an isolated Python environment.
This environment has its own Python interpreter, pip, and site-packages directory.
It prevents conflicts between different projects’ dependencies.
* `~/.venv` Path:
`~` means your home directory (e.g., /home/username on Linux/Mac).
`.venv` is a hidden folder (dot prefix makes it hidden in ls unless you use ls -a).
So `~/.venv` is a hidden virtual environment stored in your home directory.
* What It Actually Does
Creates a directory structure like:

>~/.venv/  
>├── bin/        # executables (python, pip, activate scripts)  
>├── lib/        # installed Python packages  
>└── pyvenv.cfg  # environment configuration  
>Installs a fresh copy of Python and pip inside it.  

2. edit my ~/.bashrc  `vim ~/.bashrc`
* `vim` is a text editor in the terminal. It opens files for editing directly in the shell.
* `~/.bashrc` `~` : your home directory (e.g., /home/username on Linux/Mac).  
* `.bashrc` is a hidden configuration file for the Bash shell.  
It runs every time you start a new interactive shell session (like opening a new terminal tab or SSH session).  
It’s used to set:  
>Environment variables (PATH, EDITOR, etc.)  
>Aliases (alias ll='ls -la')  
>Shell options  
>Functions  
>Prompt customization  
* The Command Opens the `.bashrc` file in Vim so you can view or edit it.
>In Vim  
:w → Write (save) the file.  
:q → Quit Vim.  
:wq → Save and quit in one step.  
:q! → Quit without saving changes.  

> 1. Open the File
`vim ~/.bashrc`
> 2. Enter Insert Mode  
Vim starts in Normal mode (where keys are commands, not text).
To start typing, press one of these keys:  

>i	Insert before the cursor (most common)  
I	 Insert at the start of the current line  
a	 Append after the cursor  
A	 Append at the end of the current line  
o	 Open a new line below and start typing  
O	 Open a new line above and start typing  

Example:
>If you want to add something at the bottom of the file:  
Press G (go to end of file).  
Press o (new line below).  
Start typing.  
![ex in terminal](image-3.png)  
Type Your Text. Once in Insert mode, you can type normally.

>3. Exit Insert Mode  
Press Esc to go back to Normal mode.
>4. Save and Quit `:wq`
and press Enter.

3. `make all`

### AWS cloudShell
### AWS cloud9

## Command-Line Tools
* `AWS Lambda` is a serverless compute service that allows you to run code without provisioning or managing servers. AWS automatically handles infrastructure management, scaling (Automatic Scaling: 1 user invokes the function → 1 executionor 10,000 users invoke the function → AWS automatically scales), availability, and execution environments, allowing developers to focus only on writing business logic.
Lambda functions are commonly used to: Process files and events, Run automation tasks, Execute backend APIs, Integrate cloud services, Perform infrastructure operations, Trigger CI/CD workflows  
What is AWS Lambda? AWS Lambda executes code in response to events.
> Instead of:  
Creating a server  
Installing an operating system  
Managing patches  
Configuring scaling   

>You simply:  
Write code  
Upload it to AWS Lambda  
Configure a trigger  

>Lambda can be triggered by:   
S3 uploads  
API Gateway requests  
CloudWatch events  
DynamoDB streams  
SQS messages  
SNS notifications  
Step Functions

* `AWS Step Functions` is a workflow orchestration service. It helps connect multiple AWS services into a coordinated workflow. Instead of writing complex orchestration code, Step Functions visually define:
>What task runs first  
What runs next  
Error handling  
Retries  
Parallel execution  
Conditional logic

[workflow code ex] (https://github.com/Nesmakamalsh/Python_for_Devops/blob/main/state-machine.json)
<img width="2514" height="1166" alt="image" src="https://github.com/user-attachments/assets/4f74058d-f402-4c87-8328-b16b06e2a8f4" />


## Microservices

## Containerized Continous Delivery


# Bash shell
Bash is a shell scripting language , a command‑line interface interpreter that runs commands and can execute scripts.

* touch: touch command is a Linux/Unix shell utility used to create new empty files or update the access and modification timestamps of existing files --> ex in terminal: touch Makefile
* rm: deletes a file --> ex in terminal: rm devopslib__init__.py
* clear: Removes all visible text from the terminal Ctrl + L (works in most shells, same as clear).

![Excuted steps](image-1.png)
* `git add` Stages changes (new files, modifications, deletions) so they are ready to be committed. `git add *` * is not a Git feature — it’s a shell glob (wildcard) that matches all files and directories in the current directory (but not hidden files starting with .).
The shell expands * before Git sees it.
* `git commit -m ""` -m means a commit message  
![ex in terminal](image-4.png)
* `pip freeze | wc -l` pip is Python's package manager. It is the command-line tool used to: Install packages, Upgrade packages, Remove packages, List installed packages. `freeze` is a subcommand of pip, it prints all installed packages and their exact versions in a format suitable for a requirements file.
`pip freeze` Lists all installed Python packages in the current environment, typically in the format:
>umpy==2.0.1  
>pandas==2.2.2  
>requests==2.32.3  

`|` (pipe) Sends the output of the command on the left as input to the command on the right.
`wc -l` wc means word count. The -l option counts lines.  
So the command counts how many package entries are returned by pip freeze.
* `git mv` is the Git command used to move or rename a file (or directory) while telling Git about the change.
>git mv <old_name> <new_name>
