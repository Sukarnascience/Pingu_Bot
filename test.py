import picamera
import time

def record_video(output_path, duration):
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_recording(output_path)
        camera.wait_recording(duration)
        camera.stop_recording()

if __name__ == "__main__":
    video_output = "output_video.h264"
    recording_duration = 60  # in seconds

    record_video(video_output, recording_duration)
