"""
Freestyle - Helper Functions
Nicholas Johnston
December 23, 2020
"""
import json


def FREESTYLE_PROMPTS_PATH():
    """Path for prompts.json"""
    return "prompts.json"


def open_prompts():
    """
    Open json file
    :return:
    """
    with open(FREESTYLE_PROMPTS_PATH()) as json_object:
        return json.load(json_object)
