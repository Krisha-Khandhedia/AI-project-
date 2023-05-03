# -*- coding: utf-8 -*-
"""Face Emotion Recognition from Images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/rjrahul24/ai-with-python-series/blob/main/06.%20Emotion%20Recognition%20using%20Facial%20Images/Code/Face_Emotion_Recognition_from_Images.ipynb
"""

# We install the FER() library to perform facial recognition
# This installation will also take care of any of the above dependencies if they are missing

pip install fer

# Commented out IPython magic to ensure Python compatibility.
from fer import FER
import matplotlib.pyplot as plt 
# %matplotlib inline

test_image_one = plt.imread("/content/K1.jpg")
emo_detector = FER(mtcnn=True)
# Capture all the emotions on the image
captured_emotions = emo_detector.detect_emotions(test_image_one)
# Print all captured emotions with the image
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
print(dominant_emotion, emotion_score)
plt.imshow(test_image_one)

# We repeat the same steps for a few other images to confirm the performance of FER()
test_image_two = plt.imread("/content/K2.jpg")
captured_emotions_two = emo_detector.detect_emotions(test_image_two)
# print(captured_emotions_two)
plt.imshow(test_image_two)
dominant_emotion_two, emotion_score_two = emo_detector.top_emotion(test_image_two)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_two)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_three = plt.imread("/content/D1.jpg")
captured_emotions_three = emo_detector.detect_emotions(test_image_three)
# print(captured_emotions_three)
plt.imshow(test_image_three)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_three)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_four = plt.imread("/content/S1.jpg")
captured_emotions_four = emo_detector.detect_emotions(test_image_four)
# print(captured_emotions_four)
plt.imshow(test_image_four)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_four)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_five = plt.imread("/content/M1.jpg")
captured_emotions_five = emo_detector.detect_emotions(test_image_five)
# print(captured_emotions_four)
plt.imshow(test_image_five)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_five)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_six = plt.imread("/content/R1.jpg")
captured_emotions_six = emo_detector.detect_emotions(test_image_six)
# print(captured_emotions_four)
plt.imshow(test_image_six)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_six)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_seven = plt.imread("/content/B1.jpg")
captured_emotions_seven = emo_detector.detect_emotions(test_image_seven)
# print(captured_emotions_four)
plt.imshow(test_image_seven)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_seven)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_eight = plt.imread("/content/H1.jpg")
captured_emotions_eight = emo_detector.detect_emotions(test_image_eight)
# print(captured_emotions_four)
plt.imshow(test_image_eight)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_eight)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_nine = plt.imread("/content/H2.jpg")
captured_emotions_nine = emo_detector.detect_emotions(test_image_nine)
# print(captured_emotions_four)
plt.imshow(test_image_nine)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_nine)
print(dominant_emotion, emotion_score)

# Testing on another image
test_image_ten = plt.imread("/content/K3.jpg")
captured_emotions_ten = emo_detector.detect_emotions(test_image_ten)
# print(captured_emotions_four)
plt.imshow(test_image_ten)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_ten)
print(dominant_emotion, emotion_score)

