from pyzbar import pyzbar
import cv2

class BarcodeScanner:
    def __int__(self):
        self.data = ''

    def scan_tc(self):
        scanned_id_numbers = []
        cap = cv2.VideoCapture(0)
        while True:
            _, img = cap.read()
            # detect and decode
            decoded_objects = pyzbar.decode(img)
            # check if there is a QRCode in the image
            if decoded_objects:
                for obj in decoded_objects:
                    data = str(obj[0])[2:-1]
                    if not self.search(scanned_id_numbers, data) and len(data) == 11 and data.isdigit():
                        print("Scanned TC number:", data)
                        scanned_id_numbers.append(data)

            # display the result
            cv2.imshow("QRCodeScanner", img)
            if cv2.waitKey(1) == ord("\r"):
                break
        cap.release()
        cv2.destroyAllWindows()
        return scanned_id_numbers

    def search(self, list, val):
        for item in list:
            if val == item:
                return True
        return False


if __name__ == "__main__":
    scan = BarcodeScanner()
    print(scan.scan_tc())


