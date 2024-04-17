# Django Todo App

## Introduction

A simple Django app to create and manage a personal todo list.

## Features

With this Todo App, users can:

- **View** a list of todo tasks
- **Add** new tasks
- **Mark** tasks as completed
- **Edit** existing tasks
- **Delete** tasks
- **Clear** all completed tasks

Data persistence is achieved through Django models, which store task information in a SQLite database.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

2. **Install dependencies:**

3. **Run migrations to set up the database:**

4. **Create an admin user:**

5. **Run the development server:**

## Code Structure

### Models

- `Tasks`: Stores task name and completion status.
- `CompletedTask`: Archive of completed tasks.

### Views

- `views.py`: Contains the logic to display, add, edit, complete, and delete tasks.

### Templates

- `todo.html`: The main template to render the todo list.

### Forms

- `forms.py`: Defines forms for adding and editing tasks.

### Tests

- `tests.py`: Includes basic tests for the model functionality.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to improve the functionality or documentation of this project.
