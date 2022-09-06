# Objectives
The purpose of this work is to develop an image content extractor as an API. The API development is done using flask plus an authentification token for security purpose. The API will take as input an image file converted into base63 format. After being decoded, PaddleOCR used as the OCR engine, extract the image content as flask return the response as a Json file. Docker is use here to package the application into a container.

# Dependencies
 - Flask
 - Base64
 - Flask_cors
 - Json
 - PaddleOCR
 - PIL
 - IO
 
 # Dockerise our API and run it from a server
 ```
 To Dockerise our API, we need to create ou dockerfile that contain all the requirements to run our program. Once in our main folder we have the dockerfile, the API file, we run the following commands:
  - docker build -t ocr_api  # build the docker image that we will call ocr_api
  - docker images # visualize the create image
  - docker run -d -p 5000:5000 ocr_api # run our image ocr_api. flask runs by default on port 5000, that is the second 5000 in our command. By using docker, we redirect the flask running port to docker 5000 port too.
  - docker ps  # visualize the running images
  ```
## Important:
  When the code is run locally without docker, we run on the terminal **python label_detection_API.py** to turn on the flask server and in another terminal run the **test_file.py** . The default IP address of flask is 127.0.0.1 on port 5000.
  
  When the code is run on docker, after running the above commands to create and run our docker image, we run on the terminal **test_file.py**. However the IP address shoud be modify to be the same as your server.
  
  
 # Process
  ![api_process_picture](https://user-images.githubusercontent.com/48753146/188553961-4c807379-842e-4c0f-a8d5-32b3c288e131.PNG)
  
 # Test (Token + API output)
  ### Test Image
![wire_label_content_1](https://user-images.githubusercontent.com/48753146/188554989-453bad94-4c34-451f-90cb-4180b545fd94.PNG)

 ### Test the API with a good authentification token
 ![ok_test](https://user-images.githubusercontent.com/48753146/188554329-c9f55d4d-7f35-4df3-b750-a165a379c5db.PNG)

 ### Test the API with a wrong authentification token
![no_ok_test](https://user-images.githubusercontent.com/48753146/188554342-f9fc3afc-c81e-4167-8cec-36f56f940be7.PNG)

Remark:
 - You need to have docker installed in your machine in order to use it.
