import cv2 as cv

img = cv.imread('Photos/cats.jpg')
# cv.imshow('Cats', img)

def rescaleFrame(frame, scale=0.75):
    # works for images videos and live video
    width = int(frame.shape[1] * scale)
    height =  int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img, 0.25)
cv.imshow('resized image', resized_image)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, .3)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # break out of loop if d is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# def change_res(width, height):
#     # only works for live video
#     capture.set(3, width)
#     capture.set(4, height)

# wait for a specific delay for a key to be pressed. 
cv.waitKey(0) 
