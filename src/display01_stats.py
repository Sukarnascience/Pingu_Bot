import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

cycle = 0
RST = None

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Load default font.
font = ImageFont.load_default()
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
start_time = time.time()


def get_raspberry_pi_temp():
    try:
        # Run the command to get the temperature
        cmd = "vcgencmd measure_temp"
        temp_result = subprocess.check_output(cmd, shell=True)
        
        # Extract the temperature value from the result
        temp_str = temp_result.decode("utf-8").strip()
        temp_value = float(temp_str.split("=")[1].split("'")[0])
        
        return temp_value

    except Exception as e:
        return f"Error: {e}"

while True:
    
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    IP_str = IP.decode('utf-8').strip()
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    CPU_str = CPU.decode('utf-8').strip()
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    MEM_str = MemUsage.decode('utf-8').strip()
    elapsed_time = time.time() - start_time
    formatted_time = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
    raspi_temp = get_raspberry_pi_temp()

    draw.text((0, 0),f"Pingu Bot | Cloud down" ,  font=font, fill=255)
    draw.text((0, 14),"IP                  : " + IP_str,  font=font, fill=255)
    draw.text((0, 23),"Temp        : " + str(raspi_temp) + f"°C", font=font, fill=255)
    draw.text((0, 32),"UP Time  : " + formatted_time, font=font, fill=255)
    #draw.text((0, 38),"CPU           : " + CPU_str, font=font, fill=255)
    #draw.text((0, 47),"Memory  : " + MEM_str, font=font, fill=255)
    draw.text((0, 44),CPU_str, font=font, fill=255)
    draw.text((0, 53),MEM_str, font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    
    time.sleep(1)
