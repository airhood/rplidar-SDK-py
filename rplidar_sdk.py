import ctypes
from typing import List, Tuple, Optional


sdk = ctypes.CDLL("./libsdk.so")


u_result = ctypes.c_uint32
_u32 = ctypes.c_uint32
_u16 = ctypes.c_uint16
_u8 = ctypes.c_uint8


class RPlidarDriver(ctypes.Structure):
    pass

class rplidar_response_device_health_t(ctypes.Structure):
    pass

class rplidar_response_device_info_t(ctypes.Structure):
    pass

class rplidar_response_measurement_node_t(ctypes.Structure):
    pass

class rplidar_response_measurement_node_hq_t(ctypes.Structure):
    pass

class w_RplidarScanMode(ctypes.Structure):
    pass

class rplidar_ip_conf_t(ctypes.Structure):
    pass


w_RPlidarDriverPtr = ctypes.POINTER(RPlidarDriver)
w_RplidarScanModePtr = ctypes.POINTER(w_RplidarScanMode)

CHANNEL_TYPE_SERIALPORT = 0x0
DEFAULT_TIMEOUT = 2000


sdk.CreateDriver.argtypes = [_u32]
sdk.CreateDriver.restype = w_RPlidarDriverPtr

sdk.connect.argtypes = [w_RPlidarDriverPtr, ctypes.c_char_p, _u32, _u32]
sdk.connect.restype = u_result

sdk.disconnect.argtypes = [w_RPlidarDriverPtr]
sdk.disconnect.restype = None

sdk.isConnected.argtypes = [w_RPlidarDriverPtr]
sdk.isConnected.restype = ctypes.c_bool

sdk.reset.argtypes = [w_RPlidarDriverPtr, _u32]
sdk.reset.restype = u_result

sdk.clearNetSerialRxCache.argtypes = [w_RPlidarDriverPtr]
sdk.clearNetSerialRxCache.restype = u_result

sdk.getTypicalScanMode.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(_u16), _u32]
sdk.getTypicalScanMode.restype = u_result

sdk.startScan.argtypes = [w_RPlidarDriverPtr, ctypes.c_bool, ctypes.c_bool, _u32, w_RplidarScanModePtr]
sdk.startScan.restype = u_result

sdk.startScanExpress.argtypes = [w_RPlidarDriverPtr, ctypes.c_bool, _u16, _u32, w_RplidarScanModePtr, _u32]
sdk.startScanExpress.restype = u_result

sdk.getHealth.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_response_device_health_t), _u32]
sdk.getHealth.restype = u_result

sdk.getDeviceInfo.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_response_device_info_t), _u32]
sdk.getDeviceInfo.restype = u_result

sdk.setMotorPWM.argtypes = [w_RPlidarDriverPtr, _u16]
sdk.setMotorPWM.restype = u_result

sdk.startMotor.argtypes = [w_RPlidarDriverPtr]
sdk.startMotor.restype = u_result

sdk.stopMotor.argtypes = [w_RPlidarDriverPtr]
sdk.stopMotor.restype = u_result

sdk.checkMotorCtrlSupport.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(ctypes.c_bool), _u32]
sdk.checkMotorCtrlSupport.restype = u_result

sdk.setLidarIpConf.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_ip_conf_t), _u32]
sdk.setLidarIpConf.restype = u_result

sdk.getLidarIpConf.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_ip_conf_t), _u32]
sdk.getLidarIpConf.restype = u_result

sdk.getDeviceMacAddr.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(_u8), _u32]
sdk.getDeviceMacAddr.restype = u_result

sdk.stop.argtypes = [w_RPlidarDriverPtr, _u32]
sdk.stop.restype = u_result

sdk.grabScanDataHq.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_response_measurement_node_hq_t), ctypes.POINTER(ctypes.c_size_t), _u32]
sdk.grabScanDataHq.restype = u_result

sdk.ascendScanData.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_response_measurement_node_hq_t), ctypes.c_size_t]
sdk.ascendScanData.restype = u_result

sdk.getScanDataWithInterval.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_response_measurement_node_t), ctypes.POINTER(ctypes.c_size_t)]
sdk.getScanDataWithInterval.restype = u_result

sdk.getScanDataWithIntervalHq.argtypes = [w_RPlidarDriverPtr, ctypes.POINTER(rplidar_response_measurement_node_hq_t), ctypes.POINTER(ctypes.c_size_t)]
sdk.getScanDataWithIntervalHq.restype = u_result


class RPlidar:
    def __init__(self, driver_type: int = CHANNEL_TYPE_SERIALPORT):
        self.driver = sdk.CreateDriver(driver_type)
        if not self.driver:
            raise RuntimeError("Failed to create RPLidar driver")
    
    def connect(self, path: str, port_or_baud: int, flag: int = 0) -> int:
        path_bytes = path.encode('utf-8')
        return sdk.connect(self.driver, path_bytes, port_or_baud, flag)
    
    def disconnect(self) -> None:
        sdk.disconnect(self.driver)
    
    def is_connected(self) -> bool:
        return sdk.isConnected(self.driver)
    
    def reset(self, timeout: int = DEFAULT_TIMEOUT) -> int:
        return sdk.reset(self.driver, timeout)
    
    def clear_net_serial_rx_cache(self) -> int:
        return sdk.clearNetSerialRxCache(self.driver)
    
    def get_typical_scan_mode(self, timeout: int = DEFAULT_TIMEOUT) -> Tuple[int, int]:
        mode = _u16()
        result = sdk.getTypicalScanMode(self.driver, ctypes.byref(mode), timeout)
        return result, mode.value
    
    def start_scan(self, force: bool = False, use_typical_scan: bool = True, options: int = 0) -> int:
        return sdk.startScan(self.driver, force, use_typical_scan, options, None)
    
    def start_scan_express(self, force: bool = False, scan_mode: int = 0, options: int = 0, timeout: int = DEFAULT_TIMEOUT) -> int:
        return sdk.startScanExpress(self.driver, force, scan_mode, options, None, timeout)
    
    def get_health(self, timeout: int = DEFAULT_TIMEOUT) -> int:
        health = rplidar_response_device_health_t()
        return sdk.getHealth(self.driver, ctypes.byref(health), timeout)
    
    def get_device_info(self, timeout: int = DEFAULT_TIMEOUT) -> int:
        info = rplidar_response_device_info_t()
        return sdk.getDeviceInfo(self.driver, ctypes.byref(info), timeout)
    
    def set_motor_pwm(self, pwm: int) -> int:
        return sdk.setMotorPWM(self.driver, pwm)
    
    def start_motor(self) -> int:
        return sdk.startMotor(self.driver)
    
    def stop_motor(self) -> int:
        return sdk.stopMotor(self.driver)
    
    def check_motor_ctrl_support(self, timeout: int = DEFAULT_TIMEOUT) -> Tuple[int, bool]:
        support = ctypes.c_bool()
        result = sdk.checkMotorCtrlSupport(self.driver, ctypes.byref(support), timeout)
        return result, support.value
    
    def set_lidar_ip_conf(self, ip_conf, timeout: int = DEFAULT_TIMEOUT) -> int:
        return sdk.setLidarIpConf(self.driver, ctypes.byref(ip_conf), timeout)
    
    def get_lidar_ip_conf(self, timeout: int = DEFAULT_TIMEOUT) -> Tuple[int, rplidar_ip_conf_t]:
        conf = rplidar_ip_conf_t()
        result = sdk.getLidarIpConf(self.driver, ctypes.byref(conf), timeout)
        return result, conf
    
    def get_device_mac_addr(self, timeout: int = DEFAULT_TIMEOUT) -> Tuple[int, str]:
        mac_array = (_u8 * 6)()
        result = sdk.getDeviceMacAddr(self.driver, mac_array, timeout)
        mac_str = ':'.join([f'{b:02x}' for b in mac_array])
        return result, mac_str
    
    def stop(self, timeout: int = DEFAULT_TIMEOUT) -> int:
        return sdk.stop(self.driver, timeout)
    
    def grab_scan_data_hq(self, max_count: int = 8192, timeout: int = DEFAULT_TIMEOUT) -> Tuple[int, int, ctypes.Array]:
        nodes = (rplidar_response_measurement_node_hq_t * max_count)()
        count = ctypes.c_size_t(max_count)
        
        result = sdk.grabScanDataHq(self.driver, nodes, ctypes.byref(count), timeout)
        return result, count.value, nodes
    
    def ascend_scan_data(self, nodes: ctypes.Array, count: int) -> int:
        return sdk.ascendScanData(self.driver, nodes, count)
    
    def get_scan_data_with_interval(self, max_count: int = 8192) -> Tuple[int, int, ctypes.Array]:
        nodes = (rplidar_response_measurement_node_t * max_count)()
        count = ctypes.c_size_t(max_count)
        
        result = sdk.getScanDataWithInterval(self.driver, nodes, ctypes.byref(count))
        return result, count.value, nodes
    
    def get_scan_data_with_interval_hq(self, max_count: int = 8192) -> Tuple[int, int, ctypes.Array]:
        nodes = (rplidar_response_measurement_node_hq_t * max_count)()
        count = ctypes.c_size_t(max_count)
        
        result = sdk.getScanDataWithIntervalHq(self.driver, nodes, ctypes.byref(count))
        return result, count.value, nodes
