from multiprocessing.connection import wait
import sys, cv2, pytesseract, pyautogui, time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def update():

    def __init__(self):
        self.name = ""
        self.bundle_num = 1
        self.lowest = 0
        self.recent = 0
        self.avg_day = 0
        self.cheapest = 0

        self.monitor = pyautogui.size()

    def get_item_name(self):
        """get item name from screenshot"""
        pyautogui.moveTo(
            ( self.monitor.width / 2 ) - ( self.monitor.width / 6.8 ),
            ( self.monitor.height / 2 ) - ( self.monitor.height / 5 ))

        time.sleep(0.1)
        
        s = pyautogui.screenshot(region=(
            ( self.monitor.width / 2 ) - ( self.monitor.width / 12 ),  #x1
            ( self.monitor.height / 2 ) - ( self.monitor.height / 4.75 ),  #y1
            ( self.monitor.width / 9.1 ),  #x2
            ( self.monitor.height / 25 )))  #y2

        s.save("name.png")
        self.name = pytesseract.image_to_string(cv2.imread("name.png"))

update()