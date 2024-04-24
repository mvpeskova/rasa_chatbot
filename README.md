"Study & Work Abroad" Rasa Chatbot

# Project Description

This project is a chatbot designed to assist students at DIT (or prospective DIT students) in learning information about study and work opportunities abroad. The bot is capable of providing details on seven specific topics related to this area: listing partner universities, providing information on events, offering a list of available scholarships, explaining credit transfer processes, listing the documents needed for a semester abroad, informing about summer school opportunities, and helping with the documents necessary for an internship abroad.

# Prerequisites
- Python 3.8.10
- Rasa 3.6.15
- Flask 2.2.5

# Installation 
### Clone the Repository
`git clone "https://github.com/mvpeskova/rasa_chatbot"`
### Create a Virtual Environment
`python -m venv venv`
### Activate the Virtual Environment
`.\venv\Scripts\activate.bat`
### Install Rasa
`pip install rasa==3.6.15`
### Install Flask
`pip install flask==2.2.5`
### Initialize the Rasa Project
`rasa init`

# Basic Usage
### Run the Rasa Action Server
In Terminal 1:

`rasa run actions`
### Set Flask Environment Variables
In Terminal 2:

`set FLASK_APP=app.py`

`set FLASK_ENV=development`

`flask run`
### Train the Rasa Model
In Terminal 3:

`rasa train`
### Use the Chatbot
`rasa shell`

# Implementation of the Requests

1. "Inquire about events"
- intents: request_event, input_language
- actions: action_get_event, utter_events

2. "Ask for the list of scholarships"
- intents: scholarships_general, input_scholarship
- actions: action_inquire_scholarship, utter_scholarship

3. "Ask about documents required for an internship abroad"
- intents: internship_general_questions, specify_document
- actions: action_inquire_document, utter_internship

4. "Learn about credit transfer"
- intents: transfer_credits_questions, input_transfer_credits_option
- actions: action_transfer_credits, utter_transfer_credits

5. "Ask about summer schools options"
- intents: summer_school_questions, input_summer_school
- actions: action_summer_schools, action_summer_school_info

6. "Ask about documents required for a semester abroad"
- intents: exchange_semester_question, input_semester
- actions: action_semester_abroad, utter_exchange_semester

7. "Get the list of partner universities"
- intents: partner_universities, input_country
- actions: action_inquire_universities, utter_ask_country
