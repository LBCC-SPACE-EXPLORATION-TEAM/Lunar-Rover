==Enable the camera connection==
Run: sudo raspi-config
Select "Interfacing Options"
Select "Camera" and select "Enable"

==Test the camera ==
Run: raspistill -o cam.jpg

This will save a still image from the camera.

==Install the motion package==
Run: sudo apt-get install motion
Run: sudo modprobe bcm2835-v4l2

==Set the camera driver to start automatically==
Run: sudo nano /ect/modules
At the end of the file add the line:
bcm2835-v4l2

save the file and exit

==Set the camera server to run as a daemon and start automatically==
Run: sudo nano /etc/default/motion
Find and uncomment the line:
# start_motion_daemon=yes

save the file and exit

==Update the motion configuration file==
Copy the backup motion.conf file to /etc/motion/motion.conf
This will replace the default config file

==Start the motion server==
Run: sudo service motion start
Open a browser and go to "http://localhost:8081"
You should see a live video preview
