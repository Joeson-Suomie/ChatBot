# Django Chatbot with NLP

This project is a simple Django-based chatbot that utilizes natural language processing (NLP) through the spaCy library to understand and respond to user queries. It features keyword-matching logic to provide relevant answers, handles multiple questions on a single line, and can return consistent responses for variations of the same question. Additionally, the chatbot includes a user-friendly interface with a "Delete" button to clear the chat history.

## Features

- **NLP with spaCy**: Uses spaCy for processing and understanding natural language inputs.
- **Multiple Question Handling**: Can process multiple questions on a single line and provide appropriate responses.
- **Consistent Responses**: Returns the same response for different variations of the same question (e.g., "hi", "hello", "hey").
- **Chat History Management**: Allows users to clear chat history with a "Delete" button.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Joeson-Suomie/django-chatbot.git
    cd django-chatbot
    ```


2. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    

3. Install the spaCy language model:

    ```bash
    python -m spacy download en_core_web_sm
    ```
    

4. Apply migrations and start the Django server:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
    

5. Access the chatbot in your browser at `http://127.0.0.1:8000/chat/`.

## Usage

- Type a question into the chat input field and press "Send" to receive a response.
- Multiple questions can be asked in a single input, separated by periods, question marks, or exclamation marks.
- Click the "Delete" button to clear the chat history.

## Example Queries

- "Hi" or "Hello" or "Hey" will return: `Hello! How can I help you today?`
- "What is Python?" will return: `Python is a versatile programming language popular for web development, data analysis, and more.`
- "Tell me about Django and spaCy" will return: `Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. spaCy is an NLP library in Python that provides tools for processing and analyzing text.`


## Dependencies

- Django
- spaCy
- en_core_web_sm (spaCy language model)

  
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to suggest improvements or report bugs.
