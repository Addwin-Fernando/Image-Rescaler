import cv2 as cv
url = input("enter the path of the image: ")
percent = float(input("enter the Percentage the image should be resized: "))

path = input("enter the url for the image to be saved: ")
save_url = path + '/resized.jpg'


scales = percent/100


img = cv.imread(url)

def rescaleFrame(frame, scale = scales):
    width = int(frame.shape[1] * scale)
    hieght = int(frame.shape[0] * scale)
    dimentions = (width,hieght)

    return cv.resize(frame,dimentions, interpolation=cv.INTER_AREA)

rescaled = rescaleFrame(img)

cv.imwrite(save_url,rescaled)
    
    
cv.imshow("rescaled",rescaled)
cv.waitKey(0)