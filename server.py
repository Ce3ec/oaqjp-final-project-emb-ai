'''
This module manages the emotion analysis server.
It uses Watson service to predict emotions based on text.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetectionApp")

@app.route("/emotionDetector")
def emotion_function():
    '''
    It requests the data from the html page 
    and then returns the emotions through the Watson Ai 
    process and finally formats everything
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response =  emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        response = "Invalid text! Please try again."
    else:
        response = f"For the given statement, the system response is {response}."

    return response

@app.route("/")
def app_rendering():
    '''
    Render the index.html
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = 'localhost', port=5001, debug=True)
