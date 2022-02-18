# WORK IN PROGRESS

This not quite ready for release yet. Currently the set up is working but as soon as gpsd runs it stops the hat logging fixes.

# raspios-gps-hat-tty

Instructions and examples of setting up gpsd with a gps hat connected via the gpio serial port.

The hat I used for this example is the Waveshare GSM/GPRS/GNSS hat mounted on a Pi Zero W. The aim is to to initialise the hat and when the Pi is booted and automatically start a gpsd instance to capture messages from the serial port normally present at gpio header pins 8 (TX) and 10(RX). I do this using a udev rule and a script. You will find the rule in the file 98-gnss.rules and the script in the file gnss in this repository.

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
apt-get install git gpsd-tools gpiod
```

## Clone this git repo

```
git clone https://github.com/rogerjames99/raspios-gps-hat-tty
cd raspios-gps-hat-tty
```

