"""
Freestyle - Helper Functions
Nicholas Johnston
December 23, 2020
"""
import json


def FREESTYLE_PROMPTS_PATH():
    """Path for prompts.json"""
    return "prompts.json"


def open_prompts() -> dict:
    """
    Open json file

    :postcondition: dictionary containing freestyle prompts
    :return: dict
    """
    with open(FREESTYLE_PROMPTS_PATH()) as json_object:
        return json.load(json_object)
