# Face-Recognition

**INTRODUCTION**

Face recognition is the technique in which the identity of a human being can be identified using ones individual face. Such kind of systems can be used in photos, videos, or in real time machines. The objective of this report is to provide a simpler and easy method in machine technology. With the help of such a technology one can easily detect the face by the help of dataset in similar matching appearance of a person. The method in which with the help of python and OpenCV in deep learning is the most efficient way to detect the face of the person. This method is useful in many fields such as the military, for security, schools, colleges and universities, airlines, banking, online web applications, gaming etc. this system uses powerful python algorithm through which the detection and recognition of face is very easy and efficient.

Here, we are using the Python programming language for detecting faces in images and videos. It requires the installation of additional packages such as OpenCV. OpenCV stands for Open Source Computer Vision. In OpenCV,all the images are converted to or from numpy arrays. This makes it easier to integrate it with other librabries that uses numpy.

After installing OpenCV, we need to install some specific librabries.
Such as,
odlib
oface_recognition

We also need a working webcam. .it includes some basic performance tweaks to make things to run faster.
oonly detect faces from every other frame.

We will use Haar-cascade for face detection.

For detect the face from the video,we need a VideoCapture object.We will learn about this further.

   **PROBLEM STATEMENT**
The main aim or objective of this paper is to provide or develop a system that will use the camera of the computer or the system that would detect and recognize the person’s face or the face of the individual using the tool in OpenCV called as the Open Face and python programming language in deep learning domain.


**Arrangement For System Design:**

In order to create this system first we will have to make the datasets. When the image quality becomes favourable different procedures will take place in the face recognition system the tasks are performed using the python queries “python encode_faces.py”. The input will be taken from the dataset which will be received in the “encodings.py”. There will be precision formatting in the system wherein face embedding for each face will occur. Secondly a file “recognize_faces_images.py” will contain all the required methods and the techniques for the process of identification of the face of the person from the given image of the dataset.

The given file will be executed by the python command “python recognize_faces_image.py- encodings”. We can resize or turn the image for approximity with the goal for getting the desired output. The present classifier along with OpenCV libraries will enhance the outcome or results in the face recognition system.

<img width="449" alt="image" src="https://user-images.githubusercontent.com/59791131/154797484-52d79d12-3a71-4810-881e-7d4bba78e873.png">
Figure 1: face recognition system design using python and OpenCV.


**FACE RECOGNITION FROM WEBCAM**

**Capture Video from Camera:**

Often, we have to capture live stream with camera. OpenCV provides a very simple interface to this. Let’s capture a video from the camera (we are using the in-built webcam of my laptop), convert it into grayscale video and display it. Just a simple task to get started.
Firstly, we use face_recognition library.

face_recognition library in Python can perform a large number of tasks:
Find all the faces in a given image
Find and manipulate facial features in an image
Identify faces in images
Real-time face recognition

Here, we will talk about the 3rd use case – identify faces in images or videos.
To capture a video, we need to create a VideoCapture object. Its argument can be either the device index or the name of a video file. Device index is just the number to specify which camera. Normally one camera will be connected (as in our case). So, I simply pass 0 (or -1). We can select the second camera by passing 1 and so on. After that, we can capture frame-by- frame. But at the end, don’t forget to release the capture. After this, we have to load the sample picture and learn how to recognize it.

Then we have to grab the single frame from the video, resize it and convert the image from BGR color to RGB color. Find all the faces and face encoding in the current frame of video. Then we have to compare the face. So we can say that is unknown face or known face. And we can use the known face with the smallest distance to the new face. And then we use cv2.rectangle and cv2.putText to draw a box around the face and a label with a name below the face.Then it will show the result.

**Function (Modules) used:**

**cv2. VideoCapture( )** :It is used to get a video capture object for the camera. Which is helpful to capture videos through webcam.

**cv2.resize()**:resizing an image means changing the dimensions of it, be it width alone, height alone or both.

**cv2.rectangle()**:it is used to draw a rectangle on any image.

**cv2.putText()**: It is used to draw a text string on any image.

**cv2.imshow()**:It is used to display an image in a window.the window automatically fits to image size.

**cv2.destroyAllWindows()**: simply destroys all the windows we created.

**cv2.waitKey()**:It waits for specified milliseconds for any keyword even.

**face_recognition.face_encoding()**:given an image, return the 128 dimension face encoding for each face in the image.

 **face_recognition.face_location()**:returns an 2d array of bounding boxes of human faces in a image using the cnn face detector.

**face_recognition.face_distance()**:given a list of face encodings, compare them to a known face encoding and get a Euclidean distance for each comparison face. The distance tell us how similar the faces are.

haarcascade_frontalface_default. xml : Detects faces. haarcascade_eye. xml : Detects the left and right eyes on the face haarcascade_smile.xml: Detects the simle
**COMPARE TWO FACES:**

We start by importing the packages we’ll need face_recognition for recognizing the face, NumPy for numerical processing, and cv2 for our OpenCV bindings.

Then we locate the image at some fix address loaded it and then encoded it. And then we have to define the function for compamring the faces. And then we use cv2.rectangle and cv2.putText to draw a box around the face and a label with a name below the face. Then it will show the result.

**OUTPUT OF THE CODE (SCREENSHOTS):**

<img width="451" alt="image" src="https://user-images.githubusercontent.com/59791131/154797544-22f1011b-4011-4d35-9247-1b5e1249faa9.png">

<img width="452" alt="image" src="https://user-images.githubusercontent.com/59791131/154797557-93ad586a-3780-4771-8753-11b823a3fb09.png">

<img width="451" alt="image" src="https://user-images.githubusercontent.com/59791131/154797565-b1bf6d1a-8a25-4468-b564-151271ac31df.png">

<img width="232" alt="image" src="https://user-images.githubusercontent.com/59791131/154797585-98d0eb6b-7891-4065-a2a6-9607becf7f73.png">

<img width="452" alt="image" src="https://user-images.githubusercontent.com/59791131/154797619-d82412ab-8fa5-4f71-9cb5-f98af7dcef69.png">

<img width="452" alt="image" src="https://user-images.githubusercontent.com/59791131/154797609-5bd2e4e3-0470-4235-a344-7bd424234725.png">


**ADVANTAGES AND DISADVANTAGES:**

The advantages of the face recognition system include faster processing, automation of the identity, breach of privacy, massive data storage, best results, enhanced security, real time face recognition of students in schools and colleges, employees at corporate offices, smartphone unlock and many more in day-to-day life.

Few disadvantages in this system include the costing, or the funding, very good cameras of high definition are required, poor image quality may limit the effectiveness of this system, size of the image will matter because it becomes difficult to recognize the face in small images, Face angles can limit the face recognition reliability, massive storage is required for this system to work effectively.

**CONCLUSION**

Face recognition systems are currently associated with many top technological companies and industries making the work of face recognition easier.Face recognition technology has come a long way in the last twenty years. In this project, we learned about some interesting library of OpecCV. We have done to detect the images through the webcam and also from the video. We can recognise three faces at a time. We have tried to recognise more faces at a time. And we go away from the webcam then it cannot detect the face properly. And also, we have learned to compare the two faces. This system is very important and useful system now a days. These applications usually work in controlled environments and recognition algorithms can take advantage of the environmental constraints to obtain high recognition accuracy. However, next generation face recognition systems are going to have widespread application in smart environments -- where computers and machines are more like helpful assistants.

The use of python programming and OpenCV makes it an easier and handy tool or system which can be made by anyone according to their requirement. The proposed system discussed in this project will be helpful for many as it is user friendly and cost_ efficient system. Hence by the use of python and OpenCV the face recognition system can be designed for various purposes.

