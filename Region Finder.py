import pyautogui

def get_mouse_position(prompt):
    input(prompt)
    return pyautogui.position()

def main():
    print("📍 REGION CAPTURE TOOL (Manual Test Mode)")

    # Get top-left corner
    top_left = get_mouse_position("Move your mouse to the TOP-LEFT corner and press Enter...")
    x1, y1 = top_left
    print(f"Top-Left: ({x1}, {y1})")

    # Get bottom-right corner
    bottom_right = get_mouse_position("Now move to the BOTTOM-RIGHT corner and press Enter...")
    x2, y2 = bottom_right
    print(f"Bottom-Right: ({x2}, {y2})")

    # Calculate width and height
    width = x2 - x1
    height = y2 - y1

    # Output result
    print("\n📐 REGION INFO:")
    print(f"X: {x1}")
    print(f"Y: {y1}")
    print(f"Width: {width}")
    print(f"Height: {height}")

if __name__ == "__main__":
    main()

