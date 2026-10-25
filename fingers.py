import cv2
import mediapipe as mp

TIPS = [8,12,16,20]
PIPS = [6,10,14,18]

# def count_one_hand(p):
#     count = sum(p[tip].y < p[pip].y for tip, pip in zip(TIPS, PIPS))
#     count += abs(p[4].x - p[17].x > abs(p[3].x - p[17].x))
#     return count
def count_one_hand(p):
    count = sum(
        p[tip].y < p[pip].y
        for tip, pip in zip(TIPS, PIPS)
    )

    if abs(p[4].x - p[17].x) > abs(p[3].x - p[17].x):
        count += 1

    return count
class HandCounter:
    def __init__(self, max_hands, confidence):
        self.hands = mp.solutions.hands.Hands(max_num_hands = max_hands, min_detection_confidence=confidence)
        
    def count(self,frame):
        result = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        total = 0
        for hand in result.multi_hand_landmarks or []:
            mp.solutions.drawing_utils.draw_landmarks(
    frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            total += count_one_hand(hand.landmark)
        return total 
        
    def close(self):
        self.hands.close()
    
    