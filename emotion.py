import cv2
from deepface import DeepFace
from collections import Counter
import os

emoji_paths = {
    "happy": "emojis/happy1.png",
    "sad": "emojis/sad.png",
    "angry": "emojis/angry1.png",
    "surprise": "emojis/surprise.png",
    "neutral": "emojis/neutral.png",
    "fear": "emojis/fear.png",
    "disgust": "emojis/disgust.png",
}

emojis = {}
for emotion, path in emoji_paths.items():
    emoji = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if emoji is None:
        raise Exception(f"Erro ao carregar emoji: {path}")
    emojis[emotion] = emoji


def overlay_emoji(frame, emoji, x, y, w, h):
    scale_factor = 3
    new_w = int(w * scale_factor)
    new_h = int(h * scale_factor)
    new_x = x - (new_w - w) // 2
    new_y = y - (new_h - h) // 2

    new_x = max(new_x, 0)
    new_y = max(new_y, 0)
    new_w = min(new_w, frame.shape[1] - new_x)
    new_h = min(new_h, frame.shape[0] - new_y)

    emoji = cv2.resize(emoji, (new_w, new_h))
    for c in range(3):
        frame[new_y : new_y + new_h, new_x : new_x + new_w, c] = emoji[:, :, c] * (
            emoji[:, :, 3] / 255.0
        ) + frame[new_y : new_y + new_h, new_x : new_x + new_w, c] * (
            1 - emoji[:, :, 3] / 255.0
        )

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("Erro ao abrir a câmera.")

emotion_history = []
history_length = 5

if os.name == 'posix':
    cv2.namedWindow("Detecção de Emoções em Tempo Real", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotions = DeepFace.analyze(
        frame,
        actions=["emotion"],
        enforce_detection=False,
        detector_backend="yolov8",
    )

    for face in emotions:
        x, y, w, h = (
            face["region"]["x"],
            face["region"]["y"],
            face["region"]["w"],
            face["region"]["h"],
        )
        x, y = max(x, 0), max(y, 0)

        emotion = face["dominant_emotion"]

        emotion_history.append(emotion)
        if len(emotion_history) > history_length:
            emotion_history.pop(0)

        smoothed_emotion = Counter(emotion_history).most_common(1)[0][0]

        emoji = emojis.get(smoothed_emotion, emojis["neutral"])

        overlay_emoji(frame, emoji, x, y, w, h)

    cv2.imshow("Detecção de Emoções em Tempo Real", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
