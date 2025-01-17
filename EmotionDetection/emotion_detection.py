"""
emotion_detection.py

This module provides functions for performing emotion_detection.py on text data.
It includes the main function `emotion_detection.py` which analyzes the emotion
of a given text and returns a a dictionary of emotions scores, including the 
dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """Analyze the emotion of the given text.

    This function takes a string input, `text_to_analyse`, and performs
    emotion detection using a pre-defined model or service. It returns
    a dictionary of emotions scores, including the dominant emotion.

    Parameters:
    text_to_analyse (str): The text to be analyzed for emotion.

    Returns:
    A dictionary of emotions scores, including the dominant emotion, e.g.,
        '{
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': '<name of the dominant emotion>'
        }'
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

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # If the response status code is 400, set all dictionary keys to None
    if response.status_code == 400:
        return { 
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    # Extract a dictionary of emotions scores, including anger, disgust, fear, joy and sadness
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Add the dominant emotion to the dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion

    # Returning a dictionary of emotions scores, including the dominant emotion
    return emotion_scores
