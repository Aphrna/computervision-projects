import cv2
from deepface import DeepFace
import pyttsx3
import threading

# Start webcam
cap = cv2.VideoCapture(0)

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Optional: adjust speech speed

last_emotion = None  # To track changes in emotion

# Function to speak emotion
def speak_emotion(emotion):
    try:
        engine.say(f"You look {emotion}")
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze emotion using DeepFace
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = results[0]['dominant_emotion']
        print("Detected Emotion:", emotion)  # Debug

        # Display emotion on the frame
        cv2.putText(frame, f'Emotion: {emotion}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Speak the emotion if it's different from the last one
        if emotion != last_emotion:
            last_emotion = emotion
            threading.Thread(target=speak_emotion, args=(emotion,), daemon=True).start()

    except Exception as e:
        print("Error detecting emotion:", e)

    cv2.imshow("Emotion Recognition with Voice", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()