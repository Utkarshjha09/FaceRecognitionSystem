
# 🔍 FaceRecognitionSystem

A complete Raspberry Pi–based smart facial recognition system featuring:
- Live face detection using `face_recognition`
- IR sensor trigger + buzzer + GPIO output
- Real-time photo alerts via **Telegram bot**
- Custom dataset creation and model training

---

## 📚 Table of Contents
- [Features](#-features)
- [Hardware Requirements](#-hardware-requirements)
- [Raspberry Pi Setup](#-raspberry-pi-setup)
- [Project Structure](#-project-structure)
- [Installation](#️-installation)
- [Step 1: Create Dataset](#-step-1-create-dataset)
- [Step 2: Train the Model](#-step-2-train-the-model)
- [Step 3: Run Recognition](#-step-3-run-recognition)
- [Telegram Bot Setup](#-telegram-bot-setup)
- [GPIO Pin Mapping](#-gpio-pin-mapping)
- [Applications](#-applications)
- [To Do](#-to-do)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

- 🔍 Real-time face recognition
- 🧠 Custom model training
- 🧾 Dataset creation with image capture
- 🔔 Buzzer alert for unrecognized faces
- ✅ GPIO-based output (e.g. unlocking door)
- 📨 Sends image & name to Telegram bot

---

## 🛠 Hardware Requirements

- Raspberry Pi 4 (with Pi OS installed)
- Camera Module (Picamera2 compatible)
- IR Sensor (GPIO 17)
- Buzzer (GPIO 24)
- Relay or lock (optional, GPIO 14)
- MicroSD Card (16 GB+)
- Internet connection (Wi-Fi or Ethernet)

---

## ⚙️ Raspberry Pi Setup

1. **Flash Raspberry Pi OS**
   - Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   - Choose **Raspberry Pi OS (32-bit)**
   - Flash it to your SD card (16 GB or more)

2. **Enable SSH & Camera**
   - Insert SD card, boot Pi
   - Open terminal:
     ```bash
     sudo raspi-config
     ```
   - Enable:
     - Camera
     - SSH (optional for remote access)
     - I2C (if needed)

3. **Update Pi**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip libatlas-base-dev libopenjp2-7 libtiff5
   ```

4. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📁 Project Structure

```
FaceRecognitionSystem/
├── facial_recognition.py
├── facial_recognition_hardware.py
├── image_capture.py
├── model_training.py
├── dataset/
├── encodings.pickle
├── requirements.txt
└── README.md
```

---

## 🧾 Installation

1. Clone the repo:
```bash
git clone https://github.com/Utkarshjha09/FaceRecognitionSystem.git
cd FaceRecognitionSystem
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📸 Step 1: Create Dataset

Edit `PERSON_NAME` in `image_capture.py`:

```python
PERSON_NAME = "john"
```

Then run:
```bash
python image_capture.py
```

- Press **Space** to capture image
- Press **q** to quit
- Images saved in `dataset/john/`

---

## 🧠 Step 2: Train the Model

Once you’ve captured images for all users:

```bash
python model_training.py
```

➡️ This creates `encodings.pickle` for recognition.

---

## 🔍 Step 3: Run Recognition

For camera-only recognition:
```bash
python facial_recognition.py
```

For full system (IR, buzzer, Telegram, GPIO):
```bash
python facial_recognition_hardware.py
```

---

## 🤖 Telegram Bot Setup

1. Open Telegram and message [@BotFather](https://t.me/BotFather)

2. Send:
   ```
   /start
   /newbot
   ```

3. Give your bot a name and username  
   (e.g. `SmartDoorBot` → `smart_door_bot`)

4. Copy the **Bot Token** shown to you  
   Example:
   ```
   1234567890:ABCdefGhIjkLmNOpQRstUVwxyZ
   ```

5. Get your **chat ID**:
   - Start your bot by searching for it in Telegram and clicking “Start”
   - Visit this link in browser:  
     ```
     https://api.telegram.org/bot<YourToken>/getUpdates
     ```

   - Find `"chat":{"id":YOUR_CHAT_ID,...}` in the JSON

6. Paste both in `facial_recognition_hardware.py`:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## 🧬 GPIO Pin Mapping

| Component      | GPIO Pin |
|----------------|----------|
| IR Sensor      | GPIO 17  |
| Door Unlock    | GPIO 14  |
| Buzzer         | GPIO 24  |

---

## 💡 Applications

This system can be used in:

- 🏠 **Smart Door Lock** – Unlock when known face is detected
- 🏢 **Office Attendance** – Log and notify entry of employees
- 🚪 **Visitor Alert System** – Notify unknown visitors with images
- 🎓 **Smart Classroom** – Automate attendance for students
- 🏭 **Restricted Access Areas** – Only allow authorized personnel

---

## ✅ To Do

- [ ] Add cloud logging (Google Sheets or Firebase)
- [ ] Add GUI for dataset collection
- [ ] Add button for manual override
- [ ] Add auto-training after adding new person

---

## 📜 License

MIT License

---

## 👤 Author

**Utkarsh Jha**  
GitHub: [@Utkarshjha09](https://github.com/Utkarshjha09)
