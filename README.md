# Django Phonebook Application

A simple Phonebook application built using Django.

## Features

- Add, edit, and delete contacts
- List all contacts
- Search for contacts by name

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-phonebook.git
    cd django-phonebook
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Visit `http://127.0.0.1:8000/phonebook/contacts/` in your browser.

## Usage

- Access the contact list at `/phonebook/contacts/`
- Add a new contact at `/phonebook/add/`
- Edit a contact at `/phonebook/edit/<contact_id>/`
- Delete a contact at `/phonebook/delete/<contact_id>/`
- Search for contacts at `/phonebook/search/`
