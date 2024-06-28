import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

detected_objects = {}

def image_callback(msg):
    # Convert ROS Image message to OpenCV image
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

    # Convert the image to grayscale for contour detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a blur to reduce noise and improve contour detection
    
    
    # Apply adaptive thresholding to highlight objects
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        
    thresh = cv2.bitwise_not(thresh)

    # Convert the thresholded image to a 3-channel image
    thresh_colored = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    # Darken the background by subtracting the thresholded image from the original frame
    result = cv2.subtract(gray,thresh)	
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using the Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 350]

    # Draw bounding boxes around the detected objects
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(img, f"Weed", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        
        

    # Display the live detection on frames
    cv2.imshow("Live Object Detection", img)
    cv2.waitKey(100)

def object_detection_node():
    rospy.init_node('object_detection_node', anonymous=True)
    rospy.Subscriber("/agribot/front_camera/image_raw", Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    object_detection_node()

