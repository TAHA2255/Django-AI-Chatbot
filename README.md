# Django AI Chatbot with DeepInfra Integration

This project is a  web-based chatbot built using the Django framework and integrated with the DeepInfra API for generating conversational responses. It provides a simple and interactive chat interface in your browser.

## Features

* Basic chat interface with user and bot message display.
* Integration with the DeepInfra API for intelligent responses.
* Uses the Mistralai/Mixtral-8x7B-Instruct-v0.1 model (configurable).
* Clean and responsive design.
![image](https://github.com/user-attachments/assets/f6c94147-6f5d-4bf1-83aa-37df86af8c08)

  

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python:** (version 3.7 or higher recommended) - [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip:** Python package installer (usually included with Python).
* **Django:** (latest stable version recommended) - Install using `pip install Django`
* **DeepInfra API Key:** You will need to sign up for a DeepInfra account and obtain your API key from their dashboard: [https://deepinfra.com/](https://deepinfra.com/)

## Setup and Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/TAHA2255/Django-AI-Chatbot
    cd chatbot
    ```

2.  **Set up environment variables:**
    * Create a `.env` file in the root of your project (next to `manage.py`).
    * Add your DeepInfra API key to this file:
        ```
        DEEPINFRA_API_KEY=YOUR_ACTUAL_DEEPINFRA_API_KEY
        ```
    * Install the `python-dotenv` package if you haven't already:
        ```bash
        pip install python-dotenv
        ```
    * Modify your `chatbot/settings.py` to load environment variables:
        ```python
        import os
        from dotenv import load_dotenv

        load_dotenv()

        # ... your other settings ...

        DEEPINFRA_API_KEY = os.getenv('DEEPINFRA_API_KEY')
        ```
        *(Then, in your `main/views.py`, you can directly access it using `settings.DEEPINFRA_API_KEY`)*

3.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a superuser (optional, for Django admin):**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
