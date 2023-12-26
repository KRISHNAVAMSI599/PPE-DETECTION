print("PPE DETECTION USING MACHINE LEARNING")
print("Select the option")
print("1.video")
print("2.webcam")
print("3.External cam")
n=int(input())
if(n==1):
    from ultralytics import YOLO
    import cv2
    import cvzone
    import math

    # cap = cv2.VideoCapture(1)  # For Webcam --with code
    #cap = cv2.VideoCapture(0)  # inbuilt cam
    #cv2.namedWindow("Window")  # inbuilt cam
    #cap.set(3, 1280)  # cam
    #cap.set(4, 720)  # cam
    # cap = cv2.VideoCapture("../Videos/ppe-3.mp4")  # For Video
    cap = cv2.VideoCapture("C:/Users/krish/Desktop/new project/Videos/ppe-1.mp4")
    model = YOLO("ppe.pt")  # train model

    classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
                  'Safety Vest', 'machinery', 'vehicle']
    myColor = (0, 0, 255)
    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))

                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100
                # Class Name
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                print(currentClass)
                if conf > 0.5:
                    if currentClass == 'NO-Hardhat' or currentClass == 'NO-Safety Vest' or currentClass == "NO-Mask":
                        myColor = (0, 0, 255)
                    elif currentClass == 'Hardhat' or currentClass == 'Safety Vest' or currentClass == "Mask":
                        myColor = (0, 255, 0)
                    else:
                        myColor = (255, 0, 0)

                    cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                                       (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor,
                                       colorT=(255, 255, 255), colorR=myColor, offset=5)
                    cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

        # cv2.imshow("Image", img) #webcam
        cv2.imshow("Window", img)  # inbuilt camera&videos
        cv2.waitKey(1)
elif(n==2):
    from ultralytics import YOLO
    import cv2
    import cvzone
    import math

    # cap = cv2.VideoCapture(1)  # For Webcam --with code
    cap = cv2.VideoCapture(0)  # inbuilt cam
    cv2.namedWindow("Window")  # inbuilt cam
    cap.set(3, 1280)  # cam
    cap.set(4, 720)  # cam
    # cap = cv2.VideoCapture("../Videos/ppe-3.mp4")  # For Video
    # cap = cv2.VideoCapture("C:/Users/krish/Desktop/new project/Videos/ppe-4.mp4")
    model = YOLO("ppe.pt")  # train model

    classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
                  'Safety Vest', 'machinery', 'vehicle']
    myColor = (0, 0, 255)
    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))

                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100
                # Class Name
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                print(currentClass)
                if conf > 0.5:
                    if currentClass == 'NO-Hardhat' or currentClass == 'NO-Safety Vest' or currentClass == "NO-Mask":
                        myColor = (0, 0, 255)
                    elif currentClass == 'Hardhat' or currentClass == 'Safety Vest' or currentClass == "Mask":
                        myColor = (0, 255, 0)
                    else:
                        myColor = (255, 0, 0)

                    cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                                       (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor,
                                       colorT=(255, 255, 255), colorR=myColor, offset=5)
                    cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

        # cv2.imshow("Image", img) #webcam
        cv2.imshow("Window", img)  # inbuilt camera&videos
        cv2.waitKey(1)
elif(n==3):
    from ultralytics import YOLO
    import cv2
    import cvzone
    import math

    cap = cv2.VideoCapture(1)  # For Webcam --with code
    #cap = cv2.VideoCapture(0)  # inbuilt cam
    cv2.namedWindow("Window")  # inbuilt cam
    cap.set(3, 1280)  # cam
    cap.set(4, 720)  # cam
    # cap = cv2.VideoCapture("../Videos/ppe-3.mp4")  # For Video
    # cap = cv2.VideoCapture("C:/Users/krish/Desktop/new project/Videos/ppe-4.mp4")
    model = YOLO("ppe.pt")  # train model

    classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
                  'Safety Vest', 'machinery', 'vehicle']
    myColor = (0, 0, 255)
    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))

                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100
                # Class Name
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                print(currentClass)
                if conf > 0.5:
                    if currentClass == 'NO-Hardhat' or currentClass == 'NO-Safety Vest' or currentClass == "NO-Mask":
                        myColor = (0, 0, 255)
                    elif currentClass == 'Hardhat' or currentClass == 'Safety Vest' or currentClass == "Mask":
                        myColor = (0, 255, 0)
                    else:
                        myColor = (255, 0, 0)

                    cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                                       (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor,
                                       colorT=(255, 255, 255), colorR=myColor, offset=5)
                    cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

        # cv2.imshow("Image", img) #webcam
        cv2.imshow("Window", img)  # inbuilt camera&videos
        cv2.waitKey(1)

