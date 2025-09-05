# rplidar-SDK-py
c++ rplidar sdk wrapper for python

## How to use (linux)
Clone rplidar_sdk repository (https://github.com/Slamtec/rplidar_sdk)

Put `wrapper.cpp` inside `rplidar_sdk/sdk/src`

Add `wrapper.cpp` to `Makefile` at `rplidar_sdk/sdk` :

```
CXXSRC += src/sl_lidar_driver.cpp \
          src/hal/thread.cpp \
          src/sl_crc.cpp \
	      src/sl_serial_channel.cpp \
	      src/sl_lidarprotocol_codec.cpp \
          src/sl_async_transceiver.cpp \
          src/sl_tcp_channel.cpp \
	      src/sl_udp_channel.cpp \
          src/rplidar_driver.cpp \
          src/wrapper.cpp
```

cd to `rplidar_sdk/sdk`
```
cd rplidar_sdk/sdk
```

Build using make :
```
make
```

Then `libsdk.so` should be created at `rplidar_sdk/sdk`

Move `libsdk.so` to your python project directory

Put `rplidar_sdk.py` to your python project directory

Now you can use the sdk by importing RPlidar :
``` py
from rplidar_sdk.py import RPlidar
```
