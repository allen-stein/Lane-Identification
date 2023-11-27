# Lane Detection using OpenCV

This project demonstrates lane detection in a video stream using computer vision techniques with the OpenCV library. The code captures a video (in this case, "test2.mp4"), applies edge detection, identifies the region of interest, and detects and overlays the lanes.

## Code Overview

The main script is provided in the Python file `lane_detection.py`. The script includes the following functions:

1. `make_coordinate(image, line_parameters)`: Computes the coordinates of the lane lines based on slope and intercept parameters.
2. `average_slope_intercept(image, lines)`: Averages the slope and intercept of detected lines to determine the position of left and right lanes.
3. `canny(image)`: Applies edge detection using the Canny algorithm.
4. `display_lines(image, lines)`: Displays detected lane lines on a black image.
5. `region_of_interest(image)`: Masks out the region of interest in the image.
6. The main script captures frames from a video, applies the edge detection, finds lane lines using the Hough Transform, averages and displays the detected lanes, and finally combines the result with the original frame.

## Usage

1. Ensure you have Python and OpenCV installed.
2. Run the script using the command: `python lane_detection.py`.
3. The output window will display the video stream with detected lane lines.
4. Press 'q' to exit the video stream.

## Customization

You can customize the script to work with other videos by changing the video file path in the `cv2.VideoCapture` function.

```python
cap = cv2.VideoCapture("your_video.mp4")
