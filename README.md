# Face Biometric Attendance System

A comprehensive face recognition-based attendance system with anti-spoofing capabilities. This system uses deep learning models to detect and recognize faces while preventing spoofing attacks using printed photos or replay attacks.

## Features

- **Face Detection**: YOLOv5-based face detection
- **Anti-Spoofing**: Protection against photo and video replay attacks
- **Face Recognition**: Deep learning-based face recognition for attendance
- **User Management**: Easy registration of new users
- **Real-time Processing**: Live video feed processing for attendance marking
- **GUI Interface**: User-friendly interface for registration and attendance

## Project Structure

```
face-Biometric-Attendance/
├── main.py                     # Main application entry point for attendance
├── new_user.py                 # User registration interface
├── video_predict.py            # Real-time video processing and face detection
├── face_rec.py                 # Face recognition and matching logic
├── output_window.py            # Results display window
├── requirements.txt            # Python dependencies
├── data_preparation.py         # Data preprocessing utilities
├── train.py                    # Model training script
├── model_to_onnx.py           # Model conversion utilities
├── loading_function.py         # Loading utilities
├── saved_models/              # Pre-trained model files
│   ├── yolov5s-face.onnx      # YOLOv5 face detection model
│   ├── AntiSpoofing_bin_*.onnx # Anti-spoofing models (binary classification)
│   ├── AntiSpoofing_bin_*.pth  # PyTorch anti-spoofing models
│   ├── AntiSpoofing_print-replay_*.onnx # Print-replay detection models
│   └── AntiSpoofing_print-replay_*.pth  # PyTorch print-replay models
├── src/                       # Source code modules
│   ├── FaceAntiSpoofing.py    # Anti-spoofing implementation
│   ├── NN.py                  # Neural network architectures
│   ├── antispoof_pretrained.py # Pre-trained anti-spoofing models
│   ├── config.py              # Configuration settings
│   ├── dataset_loader.py      # Dataset loading utilities
│   ├── train_main.py          # Training pipeline
│   ├── utility.py             # Utility functions
│   └── face_detector/         # Face detection module
│       ├── __init__.py
│       ├── YOLO.py            # YOLOv5 implementation
│       └── utils.py           # Detection utilities
└── temp pic/                  # Temporary image storage
    └── images.png
```

## Requirements

### System Requirements
- Python 3.7 or higher
- Webcam or camera device
- At least 4GB RAM
- GPU support recommended for better performance

### Python Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

The main dependencies include:
- **opencv-python**: Computer vision operations
- **torch & torchvision**: PyTorch deep learning framework
- **numpy**: Numerical computing
- **onnx & onnxruntime**: ONNX model inference
- **pandas**: Data manipulation
- **tqdm**: Progress bars
- **tensorboardX**: Tensorboard logging
- **scikit-learn**: Machine learning utilities

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/Shauryarana05/face-Biometric-Attendance.git
cd face-Biometric-Attendance
```

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 3: Verify Model Files
Ensure all pre-trained models are present in the `saved_models/` directory:
- `yolov5s-face.onnx`
- Anti-spoofing models (*.onnx and *.pth files)

## Usage Instructions

### Step 1: Register New Users

Before using the attendance system, you need to register users in the system.

```bash
python new_user.py
```

This will open a GUI interface where you can:
1. Enter user ID (numeric)
2. Enter first name and last name
3. Capture user photos using the webcam
4. Save the user profile to the system

**Important Notes for Registration:**
- Ensure good lighting conditions
- Look directly at the camera
- Capture multiple angles for better recognition
- Avoid wearing accessories that cover the face

### Step 2: Test Attendance System

Once users are registered, run the main attendance system:

```bash
python main.py
```

This will:
1. Start the video capture (`video_predict.py`)
2. Detect faces in real-time
3. Perform anti-spoofing checks
4. Recognize registered users
5. Display attendance results (`output_window.py`)
6. Clean up temporary files

## How It Works

### Face Detection
- Uses YOLOv5 model specifically trained for face detection
- Provides accurate bounding boxes for faces in the video feed

### Anti-Spoofing
- Implements multiple anti-spoofing techniques:
  - **Binary Classification**: Real vs Fake detection
  - **Print-Replay Detection**: Detects printed photos and video replay attacks
- Uses deep learning models trained on spoofing datasets

### Face Recognition
- Extracts facial features using deep neural networks
- Compares features with registered user database
- Uses similarity thresholds for accurate identification

### Attendance Logging
- Records attendance with timestamps
- Prevents duplicate entries within a session
- Generates attendance reports

## Configuration

### Camera Settings
- Default camera index: 0 (can be modified in `video_predict.py`)
- Frame resolution can be adjusted based on performance requirements

### Detection Thresholds
- Face detection confidence threshold
- Anti-spoofing sensitivity levels
- Face recognition similarity thresholds

These can be modified in `src/config.py` for fine-tuning.

## Troubleshooting

### Common Issues

1. **Camera not detected**: 
   - Check camera permissions
   - Verify camera index in code
   - Ensure no other applications are using the camera

2. **Poor recognition accuracy**:
   - Ensure good lighting during registration and testing
   - Re-register users with multiple photos
   - Check camera focus and resolution

3. **Model loading errors**:
   - Verify all model files are present in `saved_models/`
   - Check file permissions
   - Ensure sufficient memory for model loading

4. **Dependencies issues**:
   - Update pip: `pip install --upgrade pip`
   - Install packages individually if batch installation fails
   - Check Python version compatibility

## Training Custom Models

If you want to train your own models:

1. **Prepare your dataset** using `data_preparation.py`
2. **Configure training parameters** in `src/config.py`
3. **Start training** with `python train.py`
4. **Convert to ONNX** using `model_to_onnx.py` for deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the repository for license details.

## Acknowledgments

- YOLOv5 for face detection capabilities
- Anti-spoofing research community for model architectures
- OpenCV community for computer vision tools

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review existing issues in the repository
3. Create a new issue with detailed description and logs

---

**Note**: This system is designed for educational and small-scale deployment purposes. For production use, additional security measures and optimizations may be required.

## credits 
The Face Anti-Spoofing model was originally developed by hairymax and is available on GitHub: https://github.com/hairymax/Face-AntiSpoofing.git.
I have made modifications to the video_predict.py file to ensure compatibility with my module and specific requirements..
