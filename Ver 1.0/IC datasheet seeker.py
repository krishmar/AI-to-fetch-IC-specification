############################################################
# IC datasheet seeker:                                     #
#~~~~~~~~~~~~~~~~~~~~                                      #
# Image from the CAM is processed using CV module.         #
# pytesseract module is used to detect the string          #
# the processed image. Detected string is used by bs4      #
# module to collect the data sheet from the internet       #
############################################################

import cv2, pytesseract, requests, 
import numpy as np
import lxml, re
from PIL import Image
from bs4 import BeautifulSoup

# make sure the path is correct where your 'tesseract.exe' is located
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# function to get the IC image from the CAM
def get_Image():
    
    windowName = 'IC Seeker'
    # path where clear image of the IC is saved
    outpath = r'D:\CV\studyIC.jpg'

    cv2.namedWindow(windowName)
    
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    cv2.imshow(windowName, img1)
    
    cv2.waitKey(0)       # This is necessary to save a clear image
    cv2.imwrite(outpath,img1)
   
    cv2.destroyWindow(windowName)
    cap.release()

###############################################
# ~~~~~~~~~~~~~ Read string from IC  ~~~~~~~~~~
###############################################

# function to read string from the collected image
def get_string():
    # path of image from CAM module 
    img_path = r'D:\CV\studyIC.jpg'
    
    # path to store the processed image
    outpath = r"D:\CV\updatedIC.jpg"
    
    # Step1: Read Image for the given path
    img = cv2.imread(img_path,1)
        
    # Step2: Process image' 
    resize = img * 4.0
    cv2.imwrite(outpath, resize)
    
    result = pytesseract.image_to_string(Image.open(outpath))
    
    return result


# get_Image()

foundStr = get_string()
print(foundStr)
needStr = re.findall("\w{1,3}\d{3,4}\w{1,2}", foundStr)
#print("----Done-----")
print(needStr[0])

text = needStr[0]

###############################################
# ~~~~~~~~~~~~~ Collect data from net  ~~~~~~~~
############################################### 


params = {
    "q": text,
    "hl": "en",         # language
    "gl": "us",         # country of the search, US -> USA
    "start": 0,         # number page by default up to 0
    "filter": 0         # show all pages by default up to 10
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

while True:
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, 'lxml')
    
    for result in soup.select(".tF2Cxc"):
        title = f'Title: {result.select_one("h3").text}'
        link = f'Link: {result.select_one("a")["href"]}'

        print(title, link, sep="\n", end="\n\n")

    if soup.select_one('.d6cvqb a[id=pnnext]'):
        params["start"] += 10
    else:
        break
        

###############################################
# ~~~~~~~~~~~~~ Result ouput ~~~~~~~~~~~~~~~~
###############################################

# if everything working is fine, after executing the py file you should see 
# the following result in your console window screen.(Example shown here for 
# an IC CD4017)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Title: CD4017 - A Decade Counter with Decoded Output
# Link: https://www.build-electronic-circuits.com/4000-series-integrated-circuits/ic-4017/

# Title: 4017-ic-datasheet.pdf
# Link: https://www.electroschematics.com/wp-content/uploads/2011/04/4017-ic-datasheet.pdf

# Title: CD4017 Texas Instruments | Logic
# Link: https://www.digikey.com/en/products/base-product/texas-instruments/296/CD4017/19806

# Title: Understanding Decade Counter CD4017
# Link: https://www.engineersgarage.com/understanding-decade-counter-cd4017/

# Title: CD4017 Datasheet
# Link: https://www.futurlec.com/4000Series/CD4017.shtml

# Title: CD4017 datasheet & Pinout and working explained
# Link: https://www.eleccircuit.com/ic-4017-datasheet/

# Title: 5 pcs of CD4017 4017 IC & 5 pcs of 16 Pin DIP IC Sockets ...
# Link: https://www.amazon.com/CD4017-4017-Sockets-Integrated-Circuit/dp/B00I6ICVCS

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
