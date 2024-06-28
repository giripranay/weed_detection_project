import rospy
from gazebo_msgs.msg import ModelStates
from sensor_msgs.msg import Image

class ObjectDetector:
    def __init__(self):
        self.model_states = None

    def model_states_callback(self, msg):
        self.model_states = msg

    def image_callback(self, msg):
        if self.model_states is not None:
            #print(self.model_states) 
            # Assuming you have a function to convert pixel coordinates to 3D world coordinates
            # Replace the following line with your logic to map image coordinates to 3D world coordinates
            # For simplicity, this example assumes the x, y pixel coordinates directly correspond to world coordinates
            detected_objects = self.detect_objects_from_image_coordinates(msg.width, msg.height)
	    
	    
            # Extract and print the model names
            #print(detected_objects)
            model_names = [obj.model_name for obj in detected_objects]
            rospy.loginfo("Detected models: %s", model_names)

    def detect_objects_from_image_coordinates(self, image_width, image_height):
        # Example logic to map image coordinates to world coordinates and determine the detected objects
        # Replace this with your actual logic based on known object locations
        detected_objects = []

        for i, model_name in enumerate(self.model_states.name):
            # Assuming the model name is indicative of the object type (e.g., "plant", "weed")
            
            #object_type = "big_plant" if "plant" in model_name else "weed"
            object_type = ""
            if "big_plant" in model_name:
                object_type = "plant"
            elif "small_plant" in model_name:
                object_type = "weed"    

            # Assuming the x, y pixel coordinates directly correspond to world coordinates
            x = self.model_states.pose[i].position.x
            y = self.model_states.pose[i].position.y

            # Check if the object is within the image boundaries
            if 0 <= x < image_width and 0 <= y < image_height and object_type=="plant":
                detected_objects.append({"model_name": model_name, "object_type": object_type})

        return detected_objects

def main():
    rospy.init_node('object_detection_node')

    detector = ObjectDetector()

    # Subscribe to ModelStates to get information about object locations
    rospy.Subscriber("/gazebo/model_states", ModelStates, detector.model_states_callback)

    # Modify the topic name based on your robot's camera topic
    camera_topic = "/agribot/front_camera/image_raw"
    rospy.Subscriber(camera_topic, Image, detector.image_callback)

    # Spin to keep the script from exiting
    rospy.spin()

if __name__ == '__main__':
    main()

