from pathlib import Path
Messages = {
    0:"không",1:"một", 2:"hai", 3:"ba", 4: "bốn", 5:"năm",
    6:"sáu", 7:"bảy", 8:"tám", 9:"chín", 10:"mười"
}


CAMERA_INDEX = 0
MAX_HANDS = 2
DETECTION_CONFIDENCE = 0.7
STABLE_FRAME = 7

FONT_PATHS = [Path(__file__).parent / "font.ttf",
              "C:/Windows/Fonts/arial.ttf"]

FONT_SIZE = 72
TEXT_COLOR = (255,230,0)