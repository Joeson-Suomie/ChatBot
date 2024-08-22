import re
import spacy
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatLog

# Load the spaCy language model
spacy.load('en_core_web_sm')
nlp = spacy.load("en_core_web_sm")
# Create your views here.
 
def chatbot_response(query):
    doc = nlp(query.lower())

    questions = re.split(r'[.?!]\s*', query.lower())
    responses = []

    for question in questions:
        if question.strip():  # Ignore empty strings
            doc = nlp(question.strip())
    
    # Simple intent recognition based on keywords
    if any(token.lemma_ in ["hi", "hello", "hey", "wassup"] for token in doc):
                responses.append("Hello! How can I help you today?")
    elif any(token.lemma_ in ["good day!","bye"] for token in doc):
                responses.append("Goodbye! Have a great day!")
    elif any(token.lemma_ == "thank You" for token in doc):
                responses.append("You are welcome there!")
    elif "your name" in question or "who are you" in question:
                responses.append("I'm a chatbot created by my master Joeson Z. Suomie to assist you!")
    elif "how are you" in question or "how do you do" in question:
                responses.append("I'm just a bot, but I'm here to help you!")
    elif "weather" in question or "forecast" in question:
                responses.append("I'm sorry, I can't provide weather updates yet.")
    elif "time" in question:
                responses.append("I'm unable to tell time, but your device should have the correct time.")
    elif "date" in question:
         responses.append("I'm unable to tell the date, but your device should display it.")
    elif "your creator" in question or "who made you" in question:
                responses.append("I was created by a developer called Joeson Z Suomie to assist with common queries.")
    elif "openai" in question or "gpt" in question:
                responses.append("OpenAI is a research organization that developed the GPT models.")
    elif "python" in question:
                responses.append("Python is a versatile programming language popular for web development, data analysis, and more.")
    elif "django" in question:
                responses.append("Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.")
    elif "spaCy" in question:
                responses.append("spaCy is an NLP library in Python that provides tools for processing and analyzing text.")
    elif "nltk" in question:
                responses.append("NLTK is a suite of libraries and programs for symbolic and statistical natural language processing.")
    elif "machine learning" in question:
                responses.append("Machine learning is a field of AI that allows computers to learn from data and make decisions.")
    elif "deep learning" in question:
                responses.append("Deep learning is a subset of machine learning focused on neural networks with many layers.")
    elif "ai" in question:
                responses.append("AI stands for Artificial Intelligence, the simulation of human intelligence by machines.")
    elif "natural language processing" in question:
                responses.append("Natural Language Processing (NLP) is a field of AI focused on the interaction between computers and humans through language.")
    elif "database" in question:
                responses.append("A database is an organized collection of data, generally stored and accessed electronically.")
    elif "sql" in question:
                responses.append("SQL stands for Structured Query Language, used for managing and querying relational databases.")
    elif "json" in question:
                responses.append("JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write.")
    else:
                responses.append("I'm sorry, I didn't understand that. Could you please ask something else?")

     # Combine all the responses into one
    return " ".join(responses)
    

def chat_view(request):
    if request.method == "POST":
        user_query = request.POST.get('query')
        response = chatbot_response(user_query)
        
        # Save to database (optional)
        ChatLog.objects.create(user_query=user_query, bot_response=response)
        
        return JsonResponse({'response': response})

    return render(request, 'chatbot/chat.html')