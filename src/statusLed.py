from flask import Flask, request
import RPi.GPIO as GPIO
import serial
import time

app = Flask(__name__)

# Define the serial port
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
time.sleep(1)
# Define GPIO pin numbers
LED_RED = 17
LED_GREEN = 27
LED_BLUE = 22

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

# Turn off all LEDs initially
GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_BLUE, GPIO.LOW)

def statusLed(color):
    # Set the specified LED color
    if color == 'red':
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.LOW)
    elif color == 'green':
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.HIGH)
        GPIO.output(LED_BLUE, GPIO.LOW)
    elif color == 'blue':
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.HIGH)
    else:
        # Turn off all LEDs for unknown colors
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.LOW)

@app.route('/statusLed', methods=['GET'])
def set_led():
    color = request.args.get('color')

    if color:
        statusLed(color)
        return f"LED status set to {color}\n"
    else:
        return "Color parameter missing\n"

@app.route('/statusHead', methods=['GET'])
def send_head_command():
    head_command = request.args.get('head')

    if head_command:
        send_command_to_arduino(head_command)
        return f"Head command sent: {head_command}\n"
    else:
        return "Head command parameter missing\n"

def send_command_to_arduino(command):
    ser.write(command.encode())

if __name__ == '__main__':
    try:
        app.run(port=5500, host='0.0.0.0')
    finally:
        # Cleanup GPIO on exit
        GPIO.cleanup()
        ser.close()
