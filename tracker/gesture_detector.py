import cv2
import numpy as np

# ──────────────────────────────────────────
# Detect fingers using convexity defects
# ──────────────────────────────────────────
def count_fingers(contour, defects):
    finger_count = 0

    if defects is None:
        return 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        depth = d / 256.0

        if depth > 20:  # filter noise
            finger_count += 1

    # convexity defects = gaps between fingers
    # fingers = gaps + 1 (capped at 5)
    return min(finger_count + 1, 5)


# ──────────────────────────────────────────
# Gesture name from finger count + shape
# ──────────────────────────────────────────
def detect_gesture(finger_count, solidity):
    if solidity > 0.90:
        return "Fist ✊"
    if finger_count == 1:
        return "Pointing ☝️"
    if finger_count == 2:
        return "Peace ✌️"
    if finger_count == 3:
        return "Three Fingers 🤟"
    if finger_count == 4:
        return "Four Fingers"
    if finger_count == 5:
        return "Open Hand ✋"
    return "Unknown"


# ──────────────────────────────────────────
# Main
# ──────────────────────────────────────────
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Region of Interest box (where you put your hand)
ROI_TOP, ROI_BOTTOM = 100, 500
ROI_LEFT, ROI_RIGHT = 400, 900

# Background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500, varThreshold=50, detectShadows=False
)

print("Place your hand in the GREEN BOX.")
print("Press B to reset background | Press Q to quit")

frame_count = 0
gesture = "Warming up..."

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    roi = frame[ROI_TOP:ROI_BOTTOM, ROI_LEFT:ROI_RIGHT]

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(roi)

    # Clean up mask
    kernel = np.ones((5, 5), np.uint8)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
    fg_mask = cv2.GaussianBlur(fg_mask, (5, 5), 0)
    _, fg_mask = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours and frame_count > 60:  # wait for bg to stabilize
        # Get largest contour (the hand)
        hand_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(hand_contour) > 3000:
            # Convex hull
            hull = cv2.convexHull(hand_contour)
            hull_area = cv2.contourArea(hull)
            hand_area = cv2.contourArea(hand_contour)

            # Solidity = how "filled" the shape is (fist = high, open = low)
            solidity = hand_area / hull_area if hull_area > 0 else 0

            # Convexity defects
            hull_indices = cv2.convexHull(hand_contour, returnPoints=False)
            if hull_indices is not None and len(hull_indices) > 3:
                defects = cv2.convexityDefects(hand_contour, hull_indices)
                finger_count = count_fingers(hand_contour, defects)
                gesture = detect_gesture(finger_count, solidity)

            # Draw on ROI
            cv2.drawContours(roi, [hand_contour], -1, (0, 255, 0), 2)
            cv2.drawContours(roi, [hull], -1, (0, 0, 255), 2)

    frame_count += 1

    # Draw ROI box on main frame
    cv2.rectangle(frame,
                  (ROI_LEFT, ROI_TOP),
                  (ROI_RIGHT, ROI_BOTTOM),
                  (0, 255, 0), 2)

    # UI
    cv2.putText(frame, "Hand Gesture Detector", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    cv2.putText(frame, f"Gesture: {gesture}", (10, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    cv2.putText(frame, "B = Reset BG  |  Q = Quit", (10, 125),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (150, 150, 150), 1)

    if frame_count <= 60:
        cv2.putText(frame, "Calibrating background...", (ROI_LEFT, ROI_TOP - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 165, 255), 2)

    # Show mask (debug window)
    cv2.imshow("Mask (debug)", fg_mask)
    cv2.imshow("Hand Gesture Detector", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("b"):
        bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=500, varThreshold=50, detectShadows=False
        )
        frame_count = 0
        gesture = "Recalibrating..."

cap.release()
cv2.destroyAllWindows()