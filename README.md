# 🌍 Multimodal Machine Translation System

## Overview
This project implements a **Multimodal Machine Translation (MMT)** system that converts **spoken audio** into **translated text** in real-time.  
It leverages **OpenAI Whisper** for **speech-to-text transcription** and **Transformer-based Neural Machine Translation (NMT)** models (e.g., MarianMT, M2M100) for multilingual translation.

The system demonstrates a complete **speech-to-speech translation pipeline**, focusing on **cross-lingual accessibility** and **multilingual communication**.

---

## 🎯 Key Features
- 🎙️ **Speech Recognition:** High-accuracy transcription using OpenAI’s Whisper model.  
- 🌐 **Language Translation:** Transformer-based multilingual translation pipeline.  
- ⚡ **Real-Time Processing:** Low-latency inference and live output.  
- 🖥️ **Interactive UI:** Built with Streamlit for audio upload, playback, and translation output.  
- 🧠 **Automatic Language Detection:** Dynamically identifies input speech language.  

---

## 🧩 System Architecture

             ┌───────────────────────────────────────────┐
             │        Multimodal Translation Flow         │
             └───────────────────────────────────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Audio Input (.mp3)  │
                 └──────────────────────┘
                            │
                            ▼
              ┌──────────────────────────────┐
              │   Whisper Speech Recognition  │
              │ (Transcription + Lang Detect) │
              └──────────────────────────────┘
                            │
                            ▼
            ┌───────────────────────────────────┐
            │ Transformer-based NMT Model (e.g. │
            │ MarianMT / M2M100 / Helsinki-NLP) │
            └───────────────────────────────────┘
                            │
                            ▼
                ┌────────────────────────┐
                │  Translated Text Output │
                └────────────────────────┘
                            │
                            ▼
            ┌────────────────────────────────────┐
            │   Streamlit Frontend Visualization  │
            │ (Audio Upload, Display, Translation)│
            └────────────────────────────────────┘
