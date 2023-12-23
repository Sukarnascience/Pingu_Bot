import time
import picamera

def capture_image(output_path):
    with picamera.PiCamera() as camera:
        # Adjust camera settings if needed (optional)
        # camera.resolution = (width, height)
        # camera.rotation = 180  # Rotate the image if needed
        # ...

        # Capture an image
        camera.capture(output_path)

if __name__ == "__main__":
    # Set the output path for the captured image
    output_path = "captured_image.jpg"

    # Capture an image
    capture_image(output_path)

    print(f"Image captured and saved to {output_path}")
