from collections import Counter, deque

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import config
from fingers import HandCounter

Window = "Hand Counter - nhan q hoac esc de thoat"


def load_font():
    for path in config.FONT_PATHS:
        try:
            return ImageFont.truetype(str(path), config.FONT_SIZE)
        except OSError:
            pass
    print("[Canh bao] khong tim thay font .ttf")
    return ImageFont.load_default()


def draw_text(frame, text, font):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    ImageDraw.Draw(image).text((40,30), text, font=font, fill= config.TEXT_COLOR,
    stroke_width = 3, stroke_fill = (0,0,0))
    
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    
def main():
    camera = cv2.VideoCapture(config.CAMERA_INDEX)
    if not camera.isOpened():
        raise SystemExit(f"khong mo dc camera {config.CAMERA_INDEX}. Thu doi CAMERA_INDEX trong config.py")
    counter = HandCounter(config.MAX_HANDS, config.DETECTION_CONFIDENCE)
    font = load_font()
    history = deque(maxlen = config.STABLE_FRAME)
        
        
    while True:
        ok, frame = camera.read()
        if not ok:
            print("ko doc dc hinh tu camera")
            break
        frame = cv2.flip(frame, 1)
            
        history.append(counter.count(frame))
        total = Counter(history).most_common(1)[0][0]
        
        if total in config.Messages:
            frame = draw_text(frame,config.Messages[total], font)
        cv2.putText(
            frame,
            f"Fingers: {total}",
            (20, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        cv2.imshow(Window,frame)
        
        
        if cv2.waitKey(1) & 0xFF in (ord("q"), 27) or cv2.getWindowProperty(Window, cv2.WND_PROP_VISIBLE) < 1:
            break
        
    camera.release()
    camera.close()
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()