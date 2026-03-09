# VoxScribe-AI 🎙️

### Real-Time Offline AI Speech-to-Text Assistive System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![AI](https://img.shields.io/badge/AI-Speech%20Recognition-purple)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-green)
![Faster Whisper](https://img.shields.io/badge/Inference-Faster--Whisper-red)
![Interface](https://img.shields.io/badge/UI-Gradio-orange)
![Mode](https://img.shields.io/badge/Mode-Offline%20AI-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Overview

**VoxScribe-AI** is an AI-powered **real-time speech-to-text transcription system** designed to help **hearing-impaired individuals understand spoken conversations instantly**.

The system converts speech into readable text using **OpenAI Whisper** through the **Faster-Whisper inference engine**, and provides a clean, browser-based interface built with **Gradio**.

Unlike many commercial speech recognition tools, this system runs **fully offline**, ensuring:

* 🔒 Data privacy
* 🌐 No internet dependency
* ⚡ Low latency transcription
* 💻 Accessibility on standard hardware

---

## ✨ Key Features

* 🎤 Real-time microphone transcription
* 📁 Audio file upload transcription (wav, mp3, m4a, ogg)
* 🤖 Whisper AI speech recognition model
* ⚡ Faster-Whisper optimized inference
* 🌍 Multilingual speech recognition
* 🔇 Noise filtering with Voice Activity Detection (VAD)
* 📡 Streaming transcription output
* 🖥 Simple browser-based UI with Gradio
* 🔐 Fully offline speech processing

---

## 🧠 System Architecture

The system follows a modular AI pipeline:

```
Audio Input
     ↓
Audio Preprocessing (VAD / Noise Handling)
     ↓
Feature Extraction (Log-Mel Spectrogram)
     ↓
Whisper AI Model (Faster-Whisper Inference)
     ↓
Text Post-Processing
     ↓
Real-Time Transcription Display (Gradio UI)
```

---

## 🛠 Tech Stack

**Programming Language**

* Python

**AI & ML**

* OpenAI Whisper
* Faster-Whisper
* PyTorch

**Interface**

* Gradio

**Supporting Libraries**

* NumPy
* Pathlib
* FFmpeg
* OS

---

## 📂 Project Structure

```
VoxScribe-AI
│
├── app.py
├── requirements.txt
├── README.md
│
├── screenshots
│   ├── interface.png
│   ├── TranscribeTerminal.png
│   ├── Transcribing.png
│   └── transcription.png
│
└── stt
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/VoxScribe-AI.git

cd VoxScribe-AI
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Linux / macOS

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Install FFmpeg

Whisper requires **FFmpeg**.

Linux

```
sudo apt install ffmpeg
```

Mac

```
brew install ffmpeg
```

Windows

Download from:

https://ffmpeg.org/download.html

---

## ▶️ Running the Application

Start the application:

```
python app.py
```

Open the browser at:

```
http://127.0.0.1:7860
```

---

## 🎯 How to Use

1. Launch the application
2. Select Whisper model size
3. Choose language (or auto-detect)
4. Record audio using microphone **or** upload an audio file
5. Click **Transcribe**
6. View real-time transcription

---

## 🌍 Supported Languages

The system supports multilingual transcription including:

* English
* Hindi
* Kannada
* Tamil
* Telugu
* Marathi
* Bengali
* Gujarati
* Malayalam
* Punjabi
* Urdu

---

## 📊 Model Size Guide

| Model    | Speed     | Accuracy  |
| -------- | --------- | --------- |
| tiny     | Very Fast | Basic     |
| base     | Fast      | Good      |
| small    | Balanced  | High      |
| medium   | Slower    | Very High |
| large-v3 | Slowest   | Best      |

Recommended for CPU systems:

```
base or small
```
## 🚀 Applications

* Assistive technology for hearing-impaired users
* Real-time meeting transcription
* Lecture captioning
* Interview transcription
* Accessibility tools
* Offline speech recognition systems

---

## 🔮 Future Improvements

* 👥 Speaker identification
* 🌐 Speech translation
* 🧾 Automatic summarization
* 📱 Mobile application
* 🧠 Context-aware transcription
* 🕶 Smart glasses integration

---

## 👩‍💻 Contributors

* Aishwarya Bhavikatti
* Anusha Kumbar
* Deepa Gonal
* Priyanka Ranagatti
---

## 📄 License

This project is developed for **educational and research purposes**.

---

## 🙏 Acknowledgement

This project uses the **Whisper speech recognition model developed by OpenAI** and the **Faster-Whisper implementation for optimized inference**.
