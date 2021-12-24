import math

import cv2


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
video_path = './video/5.mov'
vid = cv2.VideoCapture(video_path)
ret, frame = vid.read()
while True:
    if not ret:
        break
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, text, (0, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
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
        cv2.circle(frame, topLeft, 5, (0, 0, 255), -1)
    if bottomLeft is not None:
        cv2.circle(frame, bottomLeft, 5, (0, 0, 255), -1)
    if topRight is not None:
        cv2.circle(frame, topRight, 5, (0, 0, 255), -1)
    if bottomRight is not None:
        cv2.circle(frame, bottomRight, 5, (0, 0, 255), -1)

    if topLeft is not None and bottomLeft is not None:
        cv2.line(frame, bottomLeft, topLeft, (0, 0, 255), 2)
    if topRight is not None and bottomRight is not None:
        cv2.line(frame, topRight, bottomRight, (0, 0, 255), 2)

    if bottomRight is not None:
        m1 = (topLeft[1] - bottomLeft[1]) / (topLeft[0] - bottomLeft[0])
        m2 = (topRight[1] - bottomRight[1]) / (topRight[0] - bottomRight[0])
        b1 = topLeft[1] - (m1 * topLeft[0])
        b2 = topRight[1] - (m2 * topRight[0])
        dist1 = math.sqrt(math.pow(topLeft[1] - bottomLeft[1], 2) + math.pow(topLeft[0] - bottomLeft[0], 2))
        dist2 = math.sqrt(math.pow(topRight[1] - bottomRight[1], 2) + math.pow(topRight[0] - bottomRight[0], 2))
        cv2.putText(frame, 'y1 = ' + str(m1) + 'x' + ' + ' + str(b1) + ' d = ' + str(dist1), (0, 320), font, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, 'y2 = ' + str(m2) + 'x' + ' + ' + str(b2) + ' d = ' + str(dist2), (0, 350), font, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)

    # y = mx + b
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

# When everything done, release.
cv2.destroyAllWindows()
