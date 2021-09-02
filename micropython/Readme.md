
# Prerequisites and Requirements

## Download Micropython

You should have an ESP32-Board running a version of Micropython. You can download 
a binary distribution [here](https://micropython.org/download/esp32/). 
The following tutorial was tested against the firmware version 
[esp32-idf4-v1.14 (Download here)](https://micropython.org/resources/firmware/esp32-idf4-20210202-v1.14.bin)


## Install the ESP Tool 

You need Python installed as well as the `esptool`. You can install it using the following command line (e.g. inside anaconda terminal):

```
pip install --upgrade esptool
```

### Common Issues while installing ESP Tool

* The ESP tool needs a C++-Compiler for the installation procedure (can be seen in
in the error message if the installation failes). 
    * On Windows, install the [Microsoft Build Tools for C++](https://visualstudio.microsoft.com/de/visual-cpp-build-tools/), be sure to mark the C++-Package during the installation.
    * On Mac, the Xcode Command Line Tools are needed. You can install them by opening a terminal and entering the command `xcode-select --install`. 

## Flash the Micropython firmware to the ESP32 

### How to determine the correct serial Port 

You have to identify the 
correct serial port of your ESP32 (on Windows: something like `COM3` or `COM4`, on 
Mac something like `/dev/cu.usbseral-0001`). 

* On Windows, start the device manager (in German: Gerätemanager), plug in the ESP32 and look for the correct device in the _Ports_-Section (in German: _Anschlüsse_). The device is called something like _CP210x UART Bridge_ (not exactly, but something similar). A COM Port should be listed in the name. 
  * If the device is listed as _Unknown_ or _Other Devices_ , you need to install a [CP210x Device Driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers), the Universal Windows Driver works fine (tested agains version v10.1.10). 
* On Mac, start a terminal, navigate to the `/dev`-Folder and look for a file called `/dev/cu.usbserial-0001`(or a similar name). 
* __If the device is not detected at all, it is very likely that your USB cable is 
source of the error! Try another cable.__ 

### Flash the firmware 

After `esptool` is installed and the serial port is determined, you can install the downloaded firmware image of micropython using the following command lines: 

```
esptool.py --chip esp32 -p <USB-to-Serial Port> erase_flash

esptool.py --chip esp32 -p <USB-to-Serial Port> write_flash -z 0x1000 <path to .bin>
```

The first line erases the flash memory on the esp32, the second line writes 
the micropython firmware image to flash memory. 

# Load the code to the ESP32 

General things about the two example files: 

* The `boot.py`- File runs first to initialze the device. In this file, WLAN-Credentials as well as MQTT-Server, username and password is entered 
(_you should adjust this file to your needs!_)
* The `main.py`- File contains the main program. It connects to the MQTT broker 
and sends and receives messages. You should extend this file with your custom parts (e.g. sensor readings, data aggregation etc.)

## Download an appropriate IDE 

For Micropython development, it is recommended to use an appropriate IDE. For 
this lecture, [Thonny](http://thonny.org) is recommended. In the settings, 
configure Thonny to use the correct serial port. You can copy/paste the code 
snippets and save (and run) them directly on the ESP32.


# Useful Links

[Projekte mit MicroPython und dem ESP8266/ESP32](https://www.az-delivery.de/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/projekte-mit-micropython-und-dem-esp8266-esp32-teil-1)

[SparkFun](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/esp32-thing)

[Randomnerd-Tutorial: how to use Thonny](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/)