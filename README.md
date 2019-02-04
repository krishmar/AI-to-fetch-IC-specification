Introduction

   Recently when I was working in AI related projects, I had the following
thought - "How COOL it will be, if we have a program that can take a snap
shot of an IC... after recognizing the IC number it automatically search 
for the specification in the net and give you the result".
   This python script will do exactly the same. To make it simple I had
uploaded an image of an IC. Copy the whole code including the image file and 
run the code. You can change the image file path in the code accordingly. 
Make sure you have proper internet connection in order to run the 
script with out any error. 

How it is working


tesseract API form Google is made use to detect the strings from the image file. 
Before using tesseract, preprocessing of the image is performed using CV.
The extracted strings from the message is used to serach in the net with the 
help of soup.

How to make it Working in your PC


Step1: Prerequisites

Make sure you have the following modules installed in your PC. You can use PIP 
install to install all the modules mentioned. I am using Spyder with Anaconda installation
	1. tesseract		5. re
	2. cv2				6. BeautifulSoup 
	3. soup				7. PIL
	4. numpy			8. requests
	

Make sure all the above items are working fine with your python environment before
proceed with the following steps.

Step2 

Download the Zip file to your local folder in your PC. Make sure you have the image
file of an IC. Make sure to change the image path name as per the loaction in your PC.

Step3 

Make sure all the above steps are fine and Run the script.
If everything is working fine - you should be able to see the electronics website
address with the IC specification.

Final note

You can use different IC image file or real time read from a webcam.
If pytesseract cannot read the string from the image file, you need to fine tune the preprocessing 
portion done with CV.

WISH YOU GOOD LUCK.
