# pi_camera_on_boot
Fullscreen preview of Raspberry Pi camera on bootup

## Set up to boot on startup
0. Make sure the camera is enabled in the Raspberry Pi Configs.
1. Save the 'camera_preview_stream.py' file anywhere in the pi. For example in `/home/<user_name>/Documents/`.
2. Navigate to `/etc/xdg/lxsession/LXDE-pi` and add this line to the bottom of the file `@/usr/bin/python /home/<user_name>/Documents/camera_preview_stream.py`. If your python is `python3` then do `@/usr/bin/python3 /home/<user_name>/Documents/camera_preview_stream.py`.





based on this: https://forums.raspberrypi.com/viewtopic.php?t=352224
