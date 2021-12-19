import cv2

input_size = 512
video_path = './video/3.mov'

vid = cv2.VideoCapture(video_path)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./video/2.avi', codec, fps, (512, 512))

while True:
    ret, frame = vid.read()
    if ret:
        sized = cv2.resize(frame, (512, 512), interpolation=cv2.INTER_AREA)
        out.write(sized)
    else:
        out.release()
        break
