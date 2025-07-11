import os
import face_recognition
import asyncio
import RPi.GPIO as GPIO
import time
from telegram import Bot

# --- Configuration ---
BOT_TOKEN = "7860546334:AAH-nCaKjPkm8tU82EUGekwxEzNt680CoZs"
CHAT_ID = "1123435937"
IMAGE_PATH = "/home/shadow/Desktop/FaceRec/Face Recognition/detected.jpg"
DATASET_DIR = "/home/shadow/Desktop/FaceRec/Face Recognition/dataset"
IR_PIN = 17  # GPIO pin connected to IR sensor

# --- Setup GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

# --- Load known faces once ---
print("📚 Loading known faces...")
known_encodings = []
known_names = []

for folder in os.listdir(DATASET_DIR):
    folder_path = os.path.join(DATASET_DIR, folder)
    if not os.path.isdir(folder_path):
        continue
    for file in os.listdir(folder_path):
        img_path = os.path.join(folder_path, file)
        image = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(folder)

# --- Define process ---
async def process_and_notify():
    print("📸 Capturing image...")
    os.system(f"libcamera-still -o '{IMAGE_PATH}' --width 640 --height 480 --timeout 1000")

    unknown_image = face_recognition.load_image_file(IMAGE_PATH)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    name = "Unknown"
    if unknown_encodings:
        match = face_recognition.compare_faces(known_encodings, unknown_encodings[0])
        for i, is_match in enumerate(match):
            if is_match:
                name = known_names[i]
                break

    if name == "Unknown":
        message = "❗ Unknown person is waiting outside."
    else:
        message = f"{name} is waiting outside."

    print("📨 Sending message to Telegram...")
    bot = Bot(token=BOT_TOKEN)
    with open(IMAGE_PATH, 'rb') as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=message)
    print("✅ Message sent.")

# --- Main Loop ---
print("📡 Waiting for IR sensor trigger...")
try:
    while True:
        if GPIO.input(IR_PIN):
            print("👀 Motion detected!")
            asyncio.run(process_and_notify())
            time.sleep(5)  # Avoid rapid re-triggers
        time.sleep(0.1)
except KeyboardInterrupt:
    print("🛑 Exiting...")
finally:
    GPIO.cleanup()