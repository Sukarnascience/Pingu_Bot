import subprocess
import os
import time

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def capture_image(output_folder, file_prefix):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_name = f"{file_prefix}_{timestamp}.jpg"
    file_path = os.path.join(output_folder, file_name)
    
    command = f"libcamera-still -t 200 -o {file_path}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Set the duration for image capture (in seconds)
    capture_duration = 300  # 5 minutes

    # Set the output folder and create it if it doesn't exist
    output_folder = "all_pic"
    create_folder(output_folder)

    start_time = time.time()

    try:
        while time.time() - start_time < capture_duration:
            # Capture an image and save it to the output folder
            capture_image(output_folder, "img")

    except KeyboardInterrupt:
        print("Image capture stopped.")
