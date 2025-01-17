"""
emotion_detection.py

This module provides functions for performing emotion_detection.py on text data.
It includes the main function `emotion_detection.py` which analyzes the emotion
of a given text and returns a text attribute of the response object.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """Analyze the emotion of the given text.

    This function takes a string input, `text_to_analyse`, and performs
    emotion detection using a pre-defined model or service. It returns
    a text attribute of the response object.

    Parameters:
    text_to_analyse (str): The text to be analyzed for emotion.

    Returns:
    A text attribute of the response object, e.g.,
        '{"emotionPredictions":[{"emotion":{"anger":0.01364663, [SNIP]'
    """

    # URL of the emotion detection service
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers=header, timeout=10)

    # Returning a text attribute of the response object.
    return response.text