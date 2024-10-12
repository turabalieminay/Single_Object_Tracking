# Single_Object_Tracking

# Single Object Tracking using OpenCV

This project demonstrates how to implement single object tracking using OpenCV's built-in tracking algorithms. The user can select an object in the video stream, and the system will track this object frame by frame. A random tracking algorithm is chosen each time the program runs, and a colored bounding box is drawn around the object being tracked.

## Project Overview

This project is a Python-based solution for single object tracking. The user can manually select a region of interest (ROI) from a video or webcam feed, and the system will track the selected object using one of OpenCV's tracking algorithms. The tracker is chosen randomly from a list of algorithms every time the program runs. The tracked object is highlighted with a colored bounding box, which is also generated randomly for each session.

## Features

- **Single Object Tracking**: Users can select one object to track in real-time using the mouse to draw a bounding box.
- **Random Tracker Selection**: The program randomly selects one of the following OpenCV tracking algorithms:
  - **BOOSTING**
  - **MIL**
  - **KCF**
  - **CSRT**
  - **TLD**
  - **MEDIANFLOW**
  - **MOSSE**
  
- **Colored Bounding Boxes**: A random color is generated for the bounding box that tracks the selected object.

## How It Works

1. **Tracker Selection**: 
   - The program randomly selects one of the available tracking algorithms listed above.
   
2. **ROI Selection**:
   - The first frame from the video stream is displayed, and the user is prompted to select the object they want to track by drawing a bounding box using their mouse.
   
3. **Tracking**:
   - Once the object is selected, the tracking algorithm begins following the object across the video frames.
   - A colored bounding box is drawn around the object, and the location coordinates are updated in real-time.

4. **Stopping the Program**:
   - Press the 'q' key to stop the tracking process and close the program.

## How to Run

### Dependencies

To run this project, you need to have the following libraries installed:
- `opencv-python`
- `opencv-contrib-python`

You can install these dependencies using `pip`:
```bash
pip install opencv-python opencv-contrib-python
