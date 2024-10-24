# Speech-to-Text Implementation in React Native (Expo)

## Overview

Implement speech-to-text functionality in a React Native (Expo) application using OpenAI Whisper and Flask for creating the API for the backend.

## Technologies Used

- **Frameworks/Libraries**:
  - `React Native (Expo)`
  - `Flask`
  - `expo-av`
- **Tools**:
  - `OpenAI Whisper`
  - `Ngrok` (For temporarily exposing port 5000 for testing)
  - `ffmpeg` (Installed separately using chocolatey)

## Installation of Dependencies

To install all Node.js dependencies and run the app, run:

```bash
npm install
```

<br>

Under `./stt-api` to create a virtual environment, install dependencies and run the API backend, run:

```bash
cd stt-api
```

```bash
python -m venv <Name of your environment>
```

```bash
source <Name of your environment>/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python app-whisper.py
```

<br>

(Optional) <br>
If you want to expose port 5000 for testing using `ngrok`

```bash
ngrok http 5000
```

<br>

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code for personal, commercial, and open-source purposes without the need for attribution.

See the [LICENSE](/LICENSE) file for more details.
