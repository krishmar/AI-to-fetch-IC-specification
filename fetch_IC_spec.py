import cv2
import numpy as np
import pytesseract
from PIL import Image
import re
import requests
from bs4 import BeautifulSoup


def get_string(img_path):
    
    'Step1: Read Image for the given path'
    img_path = "D:\\CV\\1.jpg"
    img = cv2.imread(img_path,1)
    
    'Step2: Process image and write image to different file' 
    outpath = "D:\\CV\\2.jpg"
    resize = img*4.0
    cv2.imwrite(outpath, resize)
    
    'Step3: Read string content from the image'
    result = pytesseract.image_to_string(Image.open(outpath))
    return result
    
print('---Detected strings--')
print(get_string('1.jpg'))
print("----Done-----")

foundStr = get_string('1.jpg')
needStr = re.findall("\w{1,3}\d{3,4}\w{1,2}", foundStr)
print(needStr[0])

'Step4: Search the string content in the Web'

text = needStr[0]

url = 'https://www.google.co.in/search?q=' + text

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
for item in soup.select('.r a'):
    f_url = item.get('href')
    myurl = f_url.replace(f_url[:7], '')
    myurl = myurl.split('&')
    myurl = myurl[0]
    print(myurl)
    break
  
print('Searching from' + myurl)
f_response = requests.get(myurl)
f_soup = BeautifulSoup(f_response.text, 'lxml')
