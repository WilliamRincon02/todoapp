# TO DO APP PROJECT

## table of contents

- [Developers](#Development-team-members)
- [Instructions for running](#Instructions-for-running-a-Django-project)
- [Execution of Linters](#Execution-of-Linters)

## Development team members:
Angel Esteban Restrepo – 1151962

Bryan Alexander Niño - 1151809

William Rincón Julio – 1152053

# Instructions for running a Django project

These are the instructions for running a Django project after downloading it from GitHub, including creating a virtual environment and installing dependencies.

## 1 - Download the GitHub repository

1. Visit the repository page on GitHub and click the "Clone or download" button.
2. Select "Download ZIP" to download the project code as a ZIP file.
3. Unzip the ZIP file to the desired location on your system.

## 2 - Open a terminal or command line

Open a terminal in your operating system. On Windows, you can use the Command Prompt or PowerShell. On Linux or macOS, use the built-in terminal.

## 3 - Navigate to the project directory:

Use the "cd" (Change Directory) command to navigate to the directory where you unzipped the project. For example:

`````cd ruta/del/proyecto`````

## 4 - Create a virtual environment:

Run the following command to create a new virtual environment. This will isolate the project's dependencies from the rest of the system:
On Windows:

`````python -m venv venv`````

On Linux or macOS:

`````python3 -m venv venv`````

## 5 - Activate the virtual environment:

You must activate the virtual environment before installing dependencies or running the project. This is done with a specific command depending on your operating system:
On Windows:

`````.venv\Scripts\activate`````

On Linux or macOS:

`````source venv/bin/activate`````

## 6 - Install dependencies:

Once the virtual environment is activated, use the pip package manager to install the project dependencies. These are usually found in a requirements.txt file within the project. Run:

`````pip install -r requirements.txt`````

## 7 - Perform the migrations:

If your project uses a database, you will need to apply migrations to configure the database structure. Run:

`````python manage.py migrate`````

## 8 - Run the development server:

You are now ready to run the Django development server. Use the following command:

`````python manage.py runserver`````

## 9 -Access the project:

Open a web browser and navigate to the address provided by the Django development server (usually http://127.0.0.1:8000/).

# Execution of Linters:

To run linters and check compliance with PEP 8 conventions and code formatting using Black, simply open a terminal and navigate to the project's root directory. Then, run the following command:

`````make lint`````
