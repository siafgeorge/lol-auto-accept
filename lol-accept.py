#League of legends auto pressing accept
#SIAFGEORGE DID IT!!

#Importing libraries
import cv2
import pytesseract
import pyautogui as pg
import time
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#The program loops until decline button pop-up
found = False
while not found:
    print("Starting...")
    #Here the program is taking a screenshot
    img = pg.screenshot()
    img.save(r'before.png')
    #Then the program is reading it with cv2
    img = cv2.imread("before.png")

    ##Detecting Words
    hImg, wImg, _ = img.shape
    #Here the program is creating an array with the data of the screen
    boxes = pytesseract.image_to_data(img)
    #Here the program is searching every box
    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                #Here the program is looking for the decline button
                if "DECLINE" in b[11]:
                    pg.moveTo(x+w/2, y-h-40)
                    pg.click()
                    found = True
                    print("Found")
                    # break
                else:
                    print("not found")
                #The program is creating a rectangle around the word
                cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 1)
                #here the program is putting the text on the up left corner of the rectangle
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (50, 50, 255), 1)
    #here the program is waiting 3 sec before the next try
    if not found:
        print("Going to sleep")
        time.sleep(3)
    else:
        print("Program ended")
#here the program saves the image of the result
#YOU CAN COMMENT THIS - it's just to see what happened
cv2.imwrite("after.png", img = img)

