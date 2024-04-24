# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import json
import requests


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionInquireUniversities(Action):

    def name(self) -> Text:
        return "action_inquire_universities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        country = next(tracker.get_latest_entity_values("country"), None)

        x = requests.get(f'http://127.0.0.1:5000/partner_universities')
        if (x.status_code != 404):
            y = x.json()
        dispatcher.utter_message(text=f"Partner univerities in {country}:\n")
        for obj in y:
            if obj["country"] == country:
                universities = "\n".join(obj["universities"])
                dispatcher.utter_message(text=universities)
        return []


class ActionInquireScholarship(Action):

    def name(self) -> Text:
        return "action_inquire_scholarship"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        scholarship = next(tracker.get_latest_entity_values("scholarship_option"), None)

        x = requests.get(f'http://127.0.0.1:5000/scholarships')
        if (x.status_code != 404):
            y = x.json()
        dispatcher.utter_message(text="Required documents:\n")
        for obj in y:
            if obj["name"] == scholarship:
                dispatcher.utter_message(text=obj['documents'])

        return []

class ActionSemesterAbroad(Action):

    def name(self) -> Text:
        return "action_semester_abroad"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        semester_abroad = next(tracker.get_latest_entity_values("apply_option"), None)

        if semester_abroad not in ["partner", "independently"]:
            dispatcher.utter_message(text="Please, choose \"partner university\" or \"apply independently\":\n")
            return []

        x = requests.get('http://127.0.0.1:5000/semester_abroad')
        if x.status_code == 200:
            y = x.json()
            dispatcher.utter_message(text="The list of documents you need for application:\n")
            for obj in y:
                if obj["name"] == semester_abroad:
                    dispatcher.utter_message(text=obj['documents'])
        else:
            dispatcher.utter_message(text="Error retrieving information. Please try again later.")

        return []


class ActionInquireDocument(Action):

    def name(self) -> Text:
        return "action_inquire_document"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        document_data = next(tracker.get_latest_entity_values("document"), None)

        if document_data is None or document_data.lower() not in ["contract", "reference", "report"]:
            dispatcher.utter_message(text=f"Sorry, I don't have information about this.")
            return []

        x = requests.get('http://127.0.0.1:5000/internship')
        if x.status_code == 200:
            y = x.json()
            dispatcher.utter_message(text=f"Here's what you need to know about {document_data}:\n")
            for obj in y:
                if obj["name"] == document_data:
                    dispatcher.utter_message(text=obj['information'])
        else:
            dispatcher.utter_message(text="Error retrieving information. Please try again later.")

        return []


class ActionTransferCredits(Action):

    def name(self) -> Text:
        return "action_transfer_credits"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        transfer_credits = next(tracker.get_latest_entity_values("transfer_credits_option"), None)

        if transfer_credits is None or transfer_credits.lower() not in ["documents", "contact"]:
            dispatcher.utter_message(text=f"Sorry, I don't have information about this.")
            return []

        x = requests.get('http://127.0.0.1:5000/transfer_credits_options')
        if x.status_code == 200:
            y = x.json()
            if transfer_credits == "documents":
                information = "Necessary forms for the transfer of credits:\n "
            elif transfer_credits == "contact":
                information = "Contact people for all courses of study:\n "

            for obj in y:
                if obj["name"] == transfer_credits:
                    information += obj["description"]

            dispatcher.utter_message(text=f"{information}\n")
        else:
            dispatcher.utter_message(text="Error retrieving information. Please try again later.")

        return []


class ActionGetEvent(Action):
    def name(self) -> Text:
        return "action_get_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_language = next(tracker.get_latest_entity_values("language"), None)

        x = requests.get(f'http://127.0.0.1:5000/events')
        if (x.status_code != 404):
            y = x.json()
        dispatcher.utter_message(text=f"Found the following events in {event_language}:\n")
        for obj in y:
            if obj["language"] == event_language:
                dispatcher.utter_message(text=f"{obj['name']}\n{obj['information']}\n")

        return []


class ActionSummerSchools(Action):

    def name(self) -> Text:
        return "action_summer_schools"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        summer_school = next(tracker.get_latest_entity_values("summer_schools"), None)

        x = requests.get('http://127.0.0.1:5000/summer_schools')
        if x.status_code == 200:
            y = x.json()
            information = ""
            for school in y:
                information += f"{school['name']}\n"

            dispatcher.utter_message(text=f"Sure! Here are the upcoming summer schools:\n\n{information}")

        else:
            dispatcher.utter_message(text="Error retrieving information. Please try again later.")

        return []


class ActionSummerSchoolInfo(Action):

    def name(self) -> Text:
        return "action_summer_school_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        summer_school = next(tracker.get_latest_entity_values("summer_school_option"), None)

        x = requests.get('http://127.0.0.1:5000/summer_schools')
        if x.status_code == 200:
            y = x.json()
            for school in y:
                if school["name"] == summer_school:
                    summer_school = f'"{summer_school}"'
                    dispatcher.utter_message(text=f"Here is the information about {summer_school}:\n\n{school['description']}")

        else:
            dispatcher.utter_message(text="Error retrieving information. Please try again later.")

        return []