import subprocess

def run_file(file_name):
    subprocess.run(['python', file_name])

if __name__ == "__main__":
    # List of Python files to run
    files_to_run = ['display01_stats.py', 'statusLed.py']  # Add your file names

    # Run each file in parallel
    processes = []
    for file_name in files_to_run:
        process = subprocess.Popen(['python', file_name])
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.wait()

    print("All files have been executed.")
