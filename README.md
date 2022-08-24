# collision_detection
Pipeline to detect contacts between drone and balls being shot at a drone

TODO: train drone detector (script already written, need to figure out xml annotation input)<br/>
      re-evaluate ball detector (maybe try different videos/angles, also use range_detector.py in helpers to get color ranges for ball)<br/>
      detect an overlap between these two items<br/>
      
# Usage
collision_detection.py is the main script that will call all helper functions.<br/>
python3 collision_detection.py --video {path to video file being used}<br/>

range_detector.py can be used with a screenshot from a test video or other image to determine the proper HSV ranges for the balls<br/>
python3 range_detector.py --filter HSV --image {path to image}<br/>

train_detector.py is used to train the drone detector using dlib and the database found at https://www.kaggle.com/datasets/dasmehdixtr/drone-dataset-uav?resource=download-directory <br/>
python3 train_detector.py -c {path to image directory} -a {path to annotation directory} -o {output path}<br/>

