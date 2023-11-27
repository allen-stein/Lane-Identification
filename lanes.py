import cv2
import numpy as np
import matplotlib.pyplot as plt


def make_coordinate(image,line_parameters):
    slope,intercept=line_parameters
    print(image.shape)
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])




def average_slope_intercept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)   ##get x and y cordinate of the 2 points
        parameters = np.polyfit((x1,x2),(y1,y2),1) ##make a best fut line from the 2 points
        slope=parameters[0]             ##first section of the paramter is slope
        intercept=parameters[1]       ##the second set of parameter is intercept length
        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average=np.average(left_fit,axis=0)
    right_fit_average=np.average(right_fit,axis=0)
    left_line=make_coordinate(image,left_fit_average)
    right_line=make_coordinate(image,right_fit_average)
    #print(left_fit_average,'left')
    #print(right_fit_average,'right')
    return np.array([left_line,right_line])

def canny(image):    #for edge detection, does blur and uses canny function to get edge
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)  ##gives edge detection
    return canny

def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None :
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image

def region_of_interest(image):     ##masking out the region of interest in the image parameter
    height= image.shape[0]
    polygons = np.array([
    [(200,height),(1100,height),(550,250)]
    ])   ##making a triangular mask, the y axis value increase downwards

    mask = np.zeros_like(image)        ##create a black pic with shape similar to image
    cv2.fillPoly(mask,polygons,255)  ##put the triangle on black mask, inside fill with white-255
    masked_image=cv2.bitwise_and(image,mask)    ##uses and to get only the area inside the triangle
    return masked_image


#image=cv2.imread('test_image.jpg')
# lane_image=np.copy(image)
# canny_image = canny(lane_image)   ##calling the function
# cropped_image=region_of_interest(canny_image)
# lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5) ##finding lines in the cropped image
# averaged_lines= average_slope_intercept(lane_image,lines)
# line_image=display_lines(lane_image,averaged_lines) ##display lines over lane_image
# combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)
# cv2.imshow('result',combo_image)  ##prints output
# cv2.waitKey(0)




cap =cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)   ##calling the function
    cropped_image=region_of_interest(canny_image)
    lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5) ##finding lines in the cropped image
    averaged_lines= average_slope_intercept(frame,lines)
    line_image=display_lines(frame,averaged_lines) ##display lines over lane_image
    combo_image=cv2.addWeighted(frame,0.8,line_image,1,1)
    cv2.imshow('result',combo_image)  ##prints output
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
