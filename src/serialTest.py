import serial
import time

# Replace 'COMx' with the actual serial port your Arduino is connected to (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
time.sleep(1)
try:
    print("Sending")
    # Send 'y' over the serial connection
    time.sleep(1)
    ser.write(b'y')

    # Optional: Wait for a moment (e.g., 1 second)
    time.sleep(1)
finally:
    print("Closing")
    # Close the serial connection when done
    ser.close()
