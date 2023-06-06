# This project is a personal project for the purpose of 
# getting used to computer vision and image processing.

# Importing the necessary libraries
import cv2

def webCam():
    cv2.namedWindow("QR Scan")
    vc = cv2.VideoCapture(1)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    
    else:
        rval = False

    while rval:
        # Reads the frame
        rval, frame = vc.read()

        # convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # blur
        blur = cv2.GaussianBlur(gray, (0,0), sigmaX=33, sigmaY=33)

        # divide
        divide = cv2.divide(gray, blur, scale=255)

        # otsu threshold
        thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

        # apply morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        preproccessed_frame = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Display the resulting frame
        cv2.imshow("QR Scan", preproccessed_frame)

        # Exit the program on ESC key
        key = cv2.waitKey(20)
        if key == 27:
            break

    vc.release()
    cv2.destroyAllWindows()

# main function
def main():
    # Run WebCam
    webCam()

    return

# Calling the main function
if __name__ == "__main__":
    main()