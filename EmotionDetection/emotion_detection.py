import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url,json=input_json, headers=headers)

    data = json.loads(response.text)

    status_code = response.status_code

    if status_code != 400:
        emotion_scores = data['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    else:
        emotion_scores = data['emotionPredictions'][0]['emotion']
        for emotion in emotion_scores:
            emotion_scores[emotion] = None
        dominant_emotion = None

    output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
        }
    
    return output