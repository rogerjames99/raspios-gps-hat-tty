# raspios-gps-hat-tty

Instructions and examples of setting up gpsd with a gps hat connected via the gpio serial port.

The hat I used for this example is the Waveshare GSM/GPRS/GNSS hat mounted on a Pi Zero W. The aim is to to initialise the hat when the Pi is booted and automatically start a gpsd instance to capture messages from the serial port normally present at gpio header pins 8 (TX) and 10(RX). I do this using a udev rule and a script. You will find the rule in the file 98-gnss.rules and the script in the file gnss in this repository.

The Waveshare hat uses the SIMCOM SIM868 module to provide GPS/GPRS/GNSS services.

The starting point for this example is a clean install of Raspios Debian lite (V11.2).

## Preparation

1. Check that the jumpers on the hat are in the B (centre) position, the GPS antenna is connected.
2. Connect a display and a keyboard to the Pi, and insert a fresh Raspbian Lite sd card. Do not apply power anywhere yet.
3. Mount the hat on the Pi.
4. Apply power to the assembly. You can use either the power connector on the Pi or the one on the hat.
5. Wait until the Pi has fully booted. I suggest that you give it a few seconds after the login prompt first appears and then press return a couple of times. This will stop you getting confused by the remaining few boot messages appearing whilst you are trying to type a username or password.
6. Log in.

## Run raspi-config

Use raspi-config to :-

1. Set up the serial port to not be a console and to to be available to use.
2. Set up wifi connectivity if you need it.
3. Set up remote sshd access.

## Install the required packages

Install the required packages using apt-get

```
apt-get install git gpsd gpsd-tools gpsd-clients gpiod minicom
```

## Set up the SIM868 module

```
minicom -s
```

In the minicom configuration menu scroll down to "Serial port setup" and press return to select it. In the serial port setup menu change the serial device to "/dev/ttyS0",  make sure the hardware and software flow control options are set to "No", and set the Bps/Par/bits to "115200 8N1" . Press return to go back the the configuration menu.  Scroll to "Save setup as dfl" and select this option.  Select the "Exit" option this will take you into the the minicom terminal screen.  Press "at" followed by return. Repeat this until you see an "OK" response. At this point the SIM868 will have setup the correct baud rate and framing. Issue the following commands to the SIM868 module.

```
ate0
at&w
```

The first first command turns off the echoing of commands. The second writes the current configuration to NVRAM.

## Clone this git repo

```
git clone https://github.com/rogerjames99/raspios-gps-hat-tty
cd raspios-gps-hat-tty
```

## Set up the udev rules

```
sudo cp 98-gnss.rules /etc/udev/rules.d
```
