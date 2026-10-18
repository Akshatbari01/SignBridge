🌉 SignBridge: AI-Powered ASL Interpreter
Breaking the Silence with the Power of AI. > Built for the GDG TechSprint Hackathon (Open Innovation Track)

📖 Overview
SignBridge is a real-time, bidirectional communication tool designed to bridge the gap between the deaf community and the hearing world. Using standard webcam technology, it translates American Sign Language (ASL) gestures into fluent, spoken English.

Unlike traditional classifiers that only detect letters, SignBridge leverages Generative AI to understand context, converting broken sign language gloss (e.g., "ME HUNGRY TIME") into natural sentences (e.g., "I am hungry, is it time to eat?").

✨ Key Features
🖐️ Real-Time 3D Tracking: Uses Google MediaPipe to track 21 hand landmarks with depth perception (Z-axis).
🧠 Hybrid AI Architecture: Combines a custom TensorFlow Neural Network for speed with Google Gemini for intelligence.
🗣️ Smart Translation: Converts raw gestures into grammatically correct, fluent English sentences.
🔊 Text-to-Speech: Instantly vocalizes the translated sentence for seamless two-way conversation.
🔒 Privacy-First: Video processing happens locally on the device; only text tokens are sent to the cloud.
💻 Accessible: Runs on standard laptops without expensive sensory gloves or depth cameras.
🛠️ Tech Stack & Google Technologies
This project integrates three major Google technologies into a single pipeline:

Component	Technology	Role
Vision	Google MediaPipe	Ultra-low latency hand landmark detection & 3D coordinate extraction.
Classification	TensorFlow / Keras	Custom Deep Neural Network (DNN) to classify gestures into text tokens.
Intelligence	Google Gemini 1.5 API	Semantic engine for grammar correction and natural language generation.
Language	Python 3.x	Core logic and integration.
Interface	OpenCV	Real-time video feed and dashboard UI.
⚙️ Installation
Prerequisites
Python 3.10 or higher
A Webcam
Google Gemini API Key (Get one here)
🚀 Usage Guide This project is modular. Follow these steps to build and run the system:

Step 1: Collect Data (Optional) If you want to add your own gestures, run the collector.

Bash

python collect_data.py Instructions: Press the key corresponding to the letter you want to train (e.g., press 'A' to save 'A' samples).

Step 2: Train the Model Train the TensorFlow Neural Network on the 3D dataset.

Bash

python train_model_tf.py Output: Generates asl_model_tf.keras and label_encoder.p.

Step 3: Run the Interpreter Launch the main dashboard.

Bash

python main_app.py Sign Mode: Perform gestures in front of the camera.

Translate: Press ENTER to have Gemini fix the grammar and speak the sentence.

Edit: Press Backspace to delete the last character.

📂 Project Structure Plaintext

SignBridge/ ├── collect_data.py # Capture 3D hand landmarks ├── train_model_tf.py # Train the TensorFlow Neural Network ├── main_app.py # Main Dashboard (MediaPipe + TF + Gemini) ├── hand_data_3d.csv # Dataset (x, y, z coordinates) ├── asl_model_tf.keras # Trained Model File ├── label_encoder.p # Label Mapping File └── README.md # Documentation 🔮 Future Scope 📱 Mobile App: Porting the model to TensorFlow Lite (TFLite) for Android deployment.

🌍 Multi-Language: Integrating Google Cloud Translation API for instant Hindi/Spanish support.

🤟 Dynamic Gestures: Upgrading the model to LSTM (Long Short-Term Memory) to support moving signs like "J" and "Z".
