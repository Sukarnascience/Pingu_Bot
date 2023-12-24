# Document Process
> Its A User friendly Robot runs on Raspberry Pi 3B+ 32Bit, Due to limitaion of resources we will go with Cloud Robotics Concept.


## Issue with Pi Updates
```sh
mybot@mybot:~ $ sudo apt-get update
Hit:1 http://raspbian.raspberrypi.com/raspbian bookworm InRelease              
Hit:2 http://archive.raspberrypi.com/debian bookworm InRelease  
Reading package lists... Done                                   
W: http://raspbian.raspberrypi.com/raspbian/dists/bookworm/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
```
*Still issue is not fixed*

## Issue with Local 
_ERROR LOOK LIKE THIS_:

```sh
/bin/bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)
/bin/bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)
```

_TO FIX_ :

It seems like the issue is persistent, and the locale settings are still not being set as desired. In this case, we can try a more manual approach to set the locale directly:

1. Open the locale configuration file:

```bash
sudo nano /etc/environment
```

2. Add the following lines:

```plaintext
LANG=en_GB.UTF-8
LC_ALL=en_GB.UTF-8
LANGUAGE=en_GB:en
```

Save the file and exit the text editor.

3. Reboot your Raspberry Pi:

```bash
sudo reboot
```

After the reboot, check if the issue is resolved. This approach sets the locale environment variables globally. If the problem persists, there may be other system-specific issues that need further investigation.

## Issue with Python
I am running all this stuffs in 32Bit SBC (Raspberry Pi 3b+) so i was facing issue with ```pip``` ,I was getting error something like this:

```sh
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    For more information visit http://rptl.io/venv

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

So, to fix this i am running my eniter code inside virtual environment

## Autostart the code
> i maid a ```start_bot.sh``` file which will help me to start all the responsible code to run the robot

Got it. Let's modify the service file accordingly:

1. Open the service file for editing:

    ```bash
    sudo nano /etc/systemd/system/my_script.service
    ```

2. Update the content to reflect the correct path:

    ```ini
    [Unit]
    Description=My Script Service
    After=network.target

    [Service]
    ExecStart=/home/your_username/Documents/pingu_bot/start_bot.sh
    WorkingDirectory=/home/your_username/Documents/pingu_bot
    StandardOutput=inherit
    StandardError=inherit
    Restart=always
    User=your_username

    [Install]
    WantedBy=multi-user.target
    ```

    - Replace `your_username` with your actual username.

3. Save the file and exit the editor.

4. Reload systemd:

    ```bash
    sudo systemctl daemon-reload
    ```
    > when ever you change something you shoud reload it

5. Enable the service:

    ```bash
    sudo systemctl enable my_script.service
    ```

6. Start the service:

    ```bash
    sudo systemctl start my_script.service
    ```

Now, your `start_bot.sh` script should run automatically on boot. Remember to replace `your_username` with your actual username.


REBOOT 
```sudo apt install libraspberrypi-dev libffi-dev```
https://circuitdigest.com/microcontroller-projects/how-to-install-python-opencv-on-raspberry-pi#comment-31289
```sudo apt-get install libopencv-dev python3-opencv```

1. PORT:5001 for Camera
2. PORT:5002 for Head + RGB Status LED (Pingu)