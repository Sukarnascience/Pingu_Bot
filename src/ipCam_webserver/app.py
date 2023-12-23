# Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Create a VideoCapture object for the camera (change the index if needed)
cap = cv2.VideoCapture(0)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for streaming the camera feed
def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Encode the frame into JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in the response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for taking a snapshot and downloading the image
@app.route('/take_snap', methods=['POST'])
def take_snap():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'snapshot_{timestamp}.jpg'
    
    # Capture a single frame
    _, frame = cap.read()

    # Save the frame as an image
    cv2.imwrite(filename, frame)

    # Return the filename to the client
    return filename

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')

# Release the camera and close the application when finished
cap.release()
cv2.destroyAllWindows()
