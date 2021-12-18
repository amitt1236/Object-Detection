import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    global cord
    if event == cv2.EVENT_LBUTTONDOWN:
        cord = (x, y)


'''
coordinates 
'''
topLeft = None
bottomLeft = None
topRight = None
bottomRight = None
cord = None
end = False

# initial text
text = 'hello'

# video feed
video_path = './video/3.mov'
vid = cv2.VideoCapture(video_path)
print(int(vid.get(cv2.CAP_PROP_FPS)))
while True:
    ret, frame = vid.read()
    if not ret:
        break
    # mask = np.ones((512, 512))  # (height, width)
    # myROI = [(1698, 657), (1168, 789), (2737, 1093), (2253, 1387)]  # (x, y)
    # cv2.fillPoly(mask, [np.array(myROI)], 0)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, text, (0, 100), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    key = cv2.waitKey(1)
    if key == ord('1'):
        text = 'top left'
    if key == ord('2'):
        text = 'bottom left'
    if key == ord('3'):
        text = 'top right'
    if key == ord('4'):
        text = 'bottom right'

    if text == 'top left':
        topLeft = cord
    if text == 'bottom left':
        bottomLeft = cord
    if text == 'top right':
        topRight = cord
    if text == 'bottom right' and cord != topRight:
        bottomRight = cord

    '''
    display selected points
    '''
    if topLeft is not None:
        cv2.circle(frame, topLeft, 10, (0, 0, 255), -1)
    if bottomLeft is not None:
        cv2.circle(frame, bottomLeft, 10, (0, 0, 255), -1)
    if topRight is not None:
        cv2.circle(frame, topRight, 10, (0, 0, 255), -1)
    if bottomRight is not None:
        cv2.circle(frame, bottomRight, 10, (0, 0, 255), -1)

    if topLeft is not None and bottomLeft is not None:
        cv2.line(frame, bottomLeft, topLeft, (0, 0, 255), 3)
    if topRight is not None and bottomRight is not None:
        cv2.line(frame, topRight, bottomRight, (0, 0, 255), 3)

    # Display the resulting frame
    cv2.imshow('user', frame)
    cv2.setMouseCallback("user", click_event)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1)  # wait until any key is pressed

print('top left:' + ','.join([str(val) for val in topLeft]))
print('bottom left:' + ','.join([str(val) for val in bottomLeft]))
print('top right' + ','.join([str(val) for val in topRight]))
print('bottom right' + ','.join([str(val) for val in bottomRight]))

# When everything done, release the capture
cv2.destroyAllWindows()
