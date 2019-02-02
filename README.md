Introduction:

Recently when I was working in AI related projects, I had the following
thought - "How COOL it will be, if we have a program that can take a snap
shot of an IC... after recognizing the IC number it automatically search 
for the specification in the net and give you the result".
	  This python script will do exactly the same. To make it simple I had
uploaded an image of an IC. Copy the whole code including the image file and 
run the code. Make sure you have proper internet connection in order to run 
the script with out any error.

How it is working.

tesseract API form Google is made use to detect the strings from the image file. 
Before using tesseract, preprocessing of the image is performed using CV.
The extracted strings from the message is used to serach in the net with the 
help of soup.

Steps:
1. Prerequisites:
Make sure you have the following modules installed in your PC. You can use PIP 
install to install all the modules mentioned. I am using Spyder with Anaconda installation
	a. tesseract
	b. cv2 
	c. soup
	b. numpy
	
Make sure all the above items are working fine with your python environment before
proceed with the following steps.

2. Download the Zip file to your local folder in your PC. Make sure you have the image
file of an IC in your working directory. Run the script.

3. If everything is working fine - you should be able to see the electronics website
address with the IC specification.

You can different IC image file or real time read from a webcam.
If pytesseract cannot read the string from the image file, you need to fine the preprocessing 
portion done with CV.

WISH YOU GOOD LUCK.

   


