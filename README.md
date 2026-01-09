# Virtual Mouse using Computer Vision 🖱️

Control your computer mouse using hand gestures with OpenCV and MediaPipe!

## Features

- **Index finger** → Move mouse cursor
- **Thumb + Index close together** → Mouse click
- **Press ESC** → Exit the program

## Requirements

- Python 3.11 or 3.12 (Python 3.14 not supported yet)
- Webcam

## Installation

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

4. Generate requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

## Usage

```bash
python main.py
```

## How It Works

The program uses:
- **OpenCV** for webcam capture
- **MediaPipe** for hand landmark detection
- **PyAutoGUI** for mouse control

The index finger tip (landmark 8) controls cursor position, and pinching thumb (landmark 4) close to index finger triggers a click.

## License

MIT
