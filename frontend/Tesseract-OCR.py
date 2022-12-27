import cv2
import pytesseract
import re

# class DetectIdInfoWebcam:
#     def __init__(self):
#         self.data = None
#
#     def detect(self):
#         cap = cv2.VideoCapture(0)
#         while True:
#             _, img = cap.read()
#             # detect and decode
#             detected_objects = self.detectIdInfo(img)
#             print(detected_objects)
#             if detected_objects:
#                 self.data = detected_objects
#                 break
#             # display the result
#             cv2.imshow("QRCodeScanner", img)
#             if cv2.waitKey(1) == ord("q"):
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#         return self.data
#
#     def detectIdInfo(self, img):
#         # img = cv2.imread(src)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         # print(pytesseract.image_to_string(img))
#
#         # Detecting Words
#         boxes = pytesseract.image_to_data(img)
#         data = []
#         for x, b in enumerate(boxes.splitlines()):
#             if x != 0:
#                 b = b.split()
#                 # print(b)
#                 if len(b) == 12:
#                     if len(b[11]) == 11 and b[11].isdigit():
#                         data.append(b[11])
#                     if len(b[11]) > 25:
#                         data.append(b[11])
#                     # Draw rectangles on detected text
#                     # x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#                     # cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
#                     # print(b[11], len(b[11])) # Print all detected words
#                     # Write detected words on image
#                     # cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 50, 50), 1)
#
#         # print(data)
#         idInfo = []
#         if len(data) == 4:
#             tc = data[0]
#             name = data[3].split('<', 1)
#             lastName = name[0]
#             firstName = re.findall("[A-Z]+", name[1])
#             year = data[2][0:2]
#             month = data[2][2:4]
#             day = data[2][4:6]
#             if int(year) > 23:
#                 birthday = day + "-" + month + "-19" + year
#             else:
#                 birthday = day + "-" + month + "-20" + year
#             sex = data[2][7]
#             idInfo = [tc, firstName, lastName, birthday, sex]
#
#         # Show image
#         # cv2.imshow("Result", img)
#         # cv2.waitKey(0)
#
#         return idInfo

class DetectIdInfo:
    def __init__(self):
        self.detectedData = []
        self.analyzedData = []

    def detect(self):
        cap = cv2.VideoCapture(0)
        while True:
            _, img = cap.read()
            cv2.imshow("QRCodeScanner", img)
            if cv2.waitKey(1) == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()
        self.detectIdInfo(img)

    def detectIdInfo(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data = self.detectWords(img)
        self.detectedData = data
        self.analyzedData = self.analyzeDetected()
        return self.analyzedData

    def detectIdInfoSrc(self, src):
        img = cv2.imread(src)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data = self.detectWords(img)
        self.detectedData = data
        self.analyzedData = self.analyzeDetected()
        return self.analyzedData

    def detectWords(self, img):
        boxes = pytesseract.image_to_data(img)
        data = []
        for x, b in enumerate(boxes.splitlines()):
            if x != 0:
                b = b.split()
                if len(b) == 12:
                    if len(b[11]) == 11 and b[11].isdigit():
                        data.append(b[11])
                    if len(b[11]) > 25:
                        data.append(b[11])
                    # Draw rectangles on detected text
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
                    # print(b[11], len(b[11])) # Print all detected words
                    # Write detected words on image
                    # cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 50, 50), 1)
        cv2.imshow("Result", img)
        cv2.waitKey(0)
        return data
    def analyzeDetected(self):
        data = self.detectedData
        if data:
            if len(data) == 3:
                name = data[2].split('<', 1)
                lastName = name[0]
                firstName = re.findall("[A-Z]+", name[1])
                year = data[1][0:2]
                month = data[1][2:4]
                day = data[1][4:6]
                if int(year) > 23:
                    birthday = day + "-" + month + "-19" + year
                else:
                    birthday = day + "-" + month + "-20" + year
                sex = data[1][7]
                return [firstName, lastName, birthday, sex]
            if len(data) == 4:
                tc = data[0]
                name = data[3].split('<', 1)
                lastName = name[0]
                firstName = re.findall("[A-Z]+", name[1])
                year = data[2][0:2]
                month = data[2][2:4]
                day = data[2][4:6]
                if int(year) > 23:
                    birthday = day + "-" + month + "-19" + year
                else:
                    birthday = day + "-" + month + "-20" + year
                sex = data[2][7]
                return [tc, firstName, lastName, birthday, sex]


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

detect = DetectIdInfo()

detect.detect()

# detect.detectIdInfoSrc('Images/12345678901.png')

print(detect.detectedData)
print(detect.analyzeDetected())