**Project Description: PPE Detection Using Machine Learning**

This project implements a real-time Personal Protective Equipment (PPE) detection system utilizing machine learning technologies. Users are presented with three options: video input, webcam input, or an external camera. The system employs the Ultralytics YOLO (You Only Look Once) framework, known for its efficiency in object detection.

**Implementation Overview:**

1. **Video Input (Option 1):**
   - Users can choose a pre-recorded video file for PPE detection.
   - The YOLO model processes each frame of the video stream, identifying various objects related to personal protective equipment.
   - Detected objects include hardhats, masks, safety vests, machinery, vehicles, and more.

2. **Webcam Input (Option 2):**
   - Real-time PPE detection using the inbuilt webcam.
   - The YOLO model analyzes the webcam stream and highlights detected objects with bounding boxes.
   - Confidence scores and class labels are displayed, indicating the likelihood of the detected object being a specific PPE item.

3. **External Camera Input (Option 3):**
   - Real-time PPE detection through an external camera connected to the system.
   - The YOLO model processes the video feed, providing instantaneous feedback on the presence of various PPE items.
   - Similar to the webcam option, detected objects are labeled with confidence scores.

**Key Components:**
- **YOLO Model:** The object detection model is based on the YOLO architecture, which efficiently processes images for real-time detection of multiple object classes.
- **OpenCV:** Utilized for video capture, image processing, and display, OpenCV enhances the project's capabilities in handling visual data.
- **CVZone:** Used for adding text and visual elements to the output, enhancing the user interface and providing clear feedback on detected objects.
- **Object Classes:** The system is trained to recognize various PPE items, including hardhats, masks, safety vests, machinery, vehicles, persons, safety cones, etc.

**Visual Feedback:**
- Detected objects are visually highlighted in the video feed, providing a clear indication of their presence.
- Bounding boxes and text labels include confidence scores, allowing users to assess the reliability of each detection.

**Potential Enhancements:**
- Integration with alarm systems or notifications for immediate alerts in case of non-compliance.
- Extension of the model to recognize additional PPE classes for broader applicability.
- Deployment in industrial or safety-critical environments to enhance workplace safety.

**Note:** The accuracy of detection may vary based on environmental conditions, lighting, and camera quality.

This project aims to contribute to workplace safety by automating the monitoring of personnel adherence to safety protocols, ultimately fostering a safer work environment.
