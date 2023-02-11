import cv2


def get_frame(video_source = 0):
    cap = cv2.VideoCapture(video_source)

    while True:
        _, frame = cap.read()
        if _:
            resized_frame = cv2.resize(frame, (640, 360))
            resized_frame = cv2.imencode('.jpg', resized_frame)[1].tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + resized_frame + b'\r\n')
        else:
            pass

def get_frame_cam1():
    return get_frame("controllers/test_videos/768x576.avi")

def get_frame_cam2():
    return get_frame("controllers/test_videos/test4.mp4")