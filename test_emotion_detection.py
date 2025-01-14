from EmotionDetection.emotion_detection import emotion_detector
import json

test_list = [('I am glad this happened','joy'),
            ('I am really mad about this','anger'),
            ('I feel disgusted just hearing about this','disgust'),
            ('I am so sad about this','sadness'),
            ('I am really afraid that this will happen','fear')]

for element in test_list:
    text_to_analyse = element[0]
    emotion = element[1]
    resoult = emotion_detector(text_to_analyse=text_to_analyse)
    print(resoult)
    dominant_emotion = resoult['dominant_emotion']
    if dominant_emotion == emotion:
        print("[+] pass!")
    else:
        print(f"[-] error: emotion should be {emotion} but instead got {dominant_emotion}")