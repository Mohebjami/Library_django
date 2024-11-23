Library Management System (Python + Tkinter + SQLite)

This is a Library Management System application built using Python, Tkinter, and SQLite. It provides a graphical user interface (GUI) for managing library books. Users can perform CRUD operations (Create, Read, Update, Delete) with ease. This system uses SQLite as the database backend for storing book data.

Features

	1.	User-Friendly GUI: Designed with Tkinter for an intuitive user experience.
	2.	SQLite Integration: Persistent storage of book data.
	3.	CRUD Operations:
	•	Create: Add new books to the library.
	•	Read: View books in a dynamic table with update and delete buttons.
	•	Update: Modify details of an existing book.
	•	Delete: Remove books from the database.
	4.	Search Functionality: Search for books by title or author. A reset button clears the search and displays all books.
	5.	Dynamic Table: Displays books with scroll support and functional update/delete buttons.

Prerequisites

Ensure you have the following installed on your system:
	•	Python 3.6 or later
	•	pip (Python package manager)

Installation

Step 1: Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/your-repository/library-management-system.git
cd library-management-system

Step 2: Install Required Libraries

Install the required Python libraries using pip:

pip install tkinter

	Note: Tkinter is included in most Python installations. If it’s not available, install it using the above command.

Step 3: Run the Application

Start the application with:

python library_management.py

SQLite Setup

You don’t need to install SQLite separately as it comes pre-installed with Python. The database (library.db) is automatically created the first time you run the application.

How to Install Python

macOS

	1.	Install Python using Homebrew:

brew install python


	2.	Verify the installation:

python3 --version



Windows

	1.	Download and install Python from the official website.
	2.	During installation, check the box “Add Python to PATH”.
	3.	Verify the installation:

python --version



Linux

	1.	Install Python using your package manager:

sudo apt update
sudo apt install python3


	2.	Verify the installation:

python3 --version

How to Install Django

Although Django is not used in this project, here’s how you can install it for future reference:

Step 1: Install Django

Install Django globally using pip:

pip install django

Alternatively, install it in a virtual environment (recommended):

python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
pip install django

Step 2: Verify Installation

Ensure Django is installed:

django-admin --version

Step 3: Create a Django Project

Create a new project with:

django-admin startproject project_name

How to Run the Application

macOS/Linux

	1.	Open a terminal and navigate to the project directory:

cd library-management-system


	2.	Run the application:

python3 library_management.py



Windows

	1.	Open a command prompt and navigate to the project directory:

cd library-management-system


	2.	Run the application:

python library_management.py

Application Workflow

	1.	Launch the application.
	2.	Use the buttons to perform the following operations:
	•	Add Book: Add new books with details like title, author, and publication year.
	•	View Books: Display books in a dynamic table with update and delete buttons.
	•	Search Books: Filter books by title or author keywords.
	•	Update Book: Modify details of a selected book.
	•	Delete Book: Remove books from the library database.
	3.	Use the search bar at the top of the table to find specific books.
	4.	Use the Clear Search button to reset the search filter and display all books.
