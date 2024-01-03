import os
import subprocess

def run_file(file_path):
    subprocess.run(['python', file_path])

def run_file_onSUDO(file_path):
    subprocess.run(['sudo','python', file_path])

if __name__ == "__main__":
    # Get the path of the current script
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)

    # Navigate to the ipCam_webserver folder
    app_folder_path = os.path.join(script_directory, 'ipCam_webserver')

    # List of Python files to run in the current folder
    files_to_run = ['display01_stats.py']  # Add your file names

    # Run each file in parallel (from the current folder)
    for file_name in files_to_run:
        file_path = os.path.join(script_directory, file_name)
        run_file(file_path)

    # Run the app.py file (from the ipCam_webserver folder)
    app_file_path = os.path.join(app_folder_path, 'app.py')
    run_file_onSUDO(app_file_path)

    print("All files have been executed.")
