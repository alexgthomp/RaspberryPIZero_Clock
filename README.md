# RaspberryPIZero_Clock
This program is a full screen clock designed for a 480x320 screen attached to a raspberry pi zero. The program is writen in python and utilizes the tkinter, datetime and pyautogui libraries to create a basic clock.

You will need to set the background variable to the path of your chosen background photo. The photo also has to be in a gif format.

Follow these steps if you want your clock to run on boot:

    1. Create a shell script that contains:
        #!/bin/sh
        sudo python /where/ever/you/put/ClockGUI.py

    3. make the shell script executable:
        chmod 755 shellscriptname.sh

    4. Edit autostart:
        sudo vim /home/pi/.config/lxsession/LXDE-pi/autostart

    5. add to the bottom of autostart:
        @sh /where/ever/you/put/the/shellscript.sh
    6. reboot


Developer note: this is my first program using python so I'm sure this can be improved

