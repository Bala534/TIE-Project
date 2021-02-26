# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.types import DomainDict
import random
import requests
#

url = "https://53be12badfe4.ngrok.io/"

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



class ButtonsFactory:

    @classmethod
    def createButtons(cls, list_of_possibles: list, intent: str, slot_name: str):
        lst = []
        for i in list_of_possibles:
            d = {}
            d['title'] = i
            d['payload'] = "/" + intent + "{\"" + slot_name + "\":\" "+i+" \"}"
            lst.append(d)
        return lst
 
##########################################################################################

class ActionLeaveBalance(Action):

    def name(self) -> Text:
        return "action_leave_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        authenticate = tracker.get_slot("authenticate")
        if authenticate is None:
            dispatcher.utter_message(text = f"you have not logged in. Please login and try again", buttons = ButtonsFactory.createButtons(list_of_possibles = ['Login'], intent = "greet", slot_name = "dummy"))
        else:
            id = tracker.get_slot("id")
            data = {"id": int(id)}
            with open("data.json", "w") as f:
                json.dump(data, f)
            response = requests.post(url = url+"leavebalance", params = data)
            dispatcher.utter_message(text=f"Your remaining leaves {response.text}")


#################################################################################################


class ActionLogin(FormValidationAction):

    def name(self) -> Text:
        return "validate_greet"
    
    def validate_password(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        id = tracker.get_slot("id")
        password = tracker.get_slot("password")
        data = {
            "id" : int(id),
            "signuppswd" : password
        }
        with open("data.json", "w") as f:
            json.dump(data, f)
        print(data)
        response = requests.post(url = url, params = data)
        print(response.text)
        dispatcher.utter_message(text="YOU HAVE LOGGED IN SUCCESSFULLY")
        if response.text == "OK":
            d = {}
            d['id'] = id
            d['password'] = password
            d['authenticate']=1
            return d
        else:
            d = {}
            d['id'] = None
            d['password'] = None
        return d


##########################################################################################################

class ActionSalaryIssue(FormValidationAction):

    def name(self) -> Text:
        return "validate_salary_issue"

    def validate_SALARY_ISSUE(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,) -> Dict[Text, Any]:
        print(1)
        authenticate = tracker.get_slot("authenticate")
        if authenticate is None:
            print("sending to authenticate")
            dispatcher.utter_message(text = f"you have not logged in. Please login and try again")
            return [FollowupAction("greet")]
        else:
            id = tracker.get_slot("id")
            issue = tracker.get_slot("SALARY_ISSUE")
            data = {"id": int(id),
                    "salaryissue": str(issue) }
            with open("data.json", "w") as f:
                json.dump(data, f)
            response = requests.post(url = url+"salaryissue", params = data)
            
            dispatcher.utter_message(text=f"{response.text}")
            print(issue)
        return []


##############################################################################################################################

class ActionHarrasment(FormValidationAction):

    def name(self) -> Text:
        return "validate_harrasment"
    
    def validate_NAME_ACCUSED(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,) -> Dict[Text, Any]:

        authenticate = tracker.get_slot("authenticate")
        if authenticate is None:
            dispatcher.utter_message(text = f"you have not logged in. Please login and try again")
            return [FollowupAction("greet")]
        else:
            d = {"NAME_ACCUSED": slot_value}
            return d

    def validate_ISSUE_DISCRIPTION(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,) -> Dict[Text, Any]:
        id = tracker.get_slot("id")
        issue = tracker.get_slot("ISSUE_DISCRIPTION")
        accused = tracker.get_slot("NAME_ACCUSED")

        data = {
            "id1" : int(id),
            "case" : issue,
            "id2" : accused
        }
        with open("data.json", "w") as f:
                json.dump(data, f)
        response = requests.post(url = url+"harassment", params = data)
            
        dispatcher.utter_message(text=f"{response.text}")



#############################################################################################################

class ActionResignation(FormValidationAction):

    def name(self) -> Text:
        return "validate_resign"


    def validate_WHY_DO_YOU_WANT_TO_LEAVE(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,) -> Dict[Text, Any]:

        authenticate = tracker.get_slot("authenticate")
        if authenticate is None:
            dispatcher.utter_message(text = f"you have not logged in. Please login and try again")
            return [FollowupAction("greet")]
        else:
            d = {"NAME_ACCUSED": slot_value}
            return d
    
    def validate_IS_THERE_ANYTHING_WE_CAN_SO_THAT_YOU_STAY(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,) -> Dict[Text, Any]:
        id = tracker.get_slot("id")
        issue = tracker.get_slot("WHY_DO_YOU_WANT_TO_LEAVE")
        korika = tracker.get_slot("IS_THERE_ANYTHING_WE_CAN_SO_THAT_YOU_STAY")

        data = {
            "id1" : int(id),
            "resignissue" : issue,
            "block" : korika
        }
        with open("data.json", "w") as f:
                json.dump(data, f)
        response = requests.post(url = url+"resignation", params = data)
            
        dispatcher.utter_message(text=f"{response.text}")



