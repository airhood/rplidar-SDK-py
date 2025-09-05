#include "rplidar.h"

#define w_RPlidarDriver rp::standalone::rplidar::RPlidarDriver
#define w_RplidarScanMode rp::standalone::rplidar::RplidarScanMode

extern "C" {
    w_RPlidarDriver* CreateDriver(_u32 drivertype = sl::CHANNEL_TYPE_SERIALPORT) {
        return w_RPlidarDriver::CreateDriver(drivertype);
    }

    u_result connect(w_RPlidarDriver* driver, const char* path, _u32 portOrBaud, _u32 flag = 0) {
        return driver->connect(path, portOrBaud, flag);
    }

    void disconnect(w_RPlidarDriver* driver) {
        driver->disconnect();
    }

    bool isConnected(w_RPlidarDriver* driver) {
        return driver->isConnected();
    }

    u_result reset(w_RPlidarDriver* driver, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {\
        return driver->reset(timeout);
    }

    u_result clearNetSerialRxCache(w_RPlidarDriver* driver) {
        return driver->clearNetSerialRxCache();
    }

    u_result getAllSupportedScanModes(w_RPlidarDriver* driver, std::vector<w_RplidarScanMode>& outModes, _u32 timeoutInMs = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->getAllSupportedScanModes(outModes, timeoutInMs);
    }

    u_result getTypicalScanMode(w_RPlidarDriver* driver, _u16& outMode, _u32 timeoutInMs = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->getTypicalScanMode(outMode, timeoutInMs);
    }

    u_result startScan(w_RPlidarDriver* driver, bool force, bool useTypicalScan, _u32 options = 0, w_RplidarScanMode* outUsedScanMode = NULL) {
        return driver->startScan(force, useTypicalScan, options, outUsedScanMode);
    }

    u_result startScanExpress(w_RPlidarDriver* driver, bool force, _u16 scanMode, _u32 options = 0, w_RplidarScanMode* outUsedScanMode = NULL, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->startScanExpress(force, scanMode, options, outUsedScanMode);
    }

    u_result getHealth(w_RPlidarDriver* driver, rplidar_response_device_health_t& health, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->getHealth(health, timeout);
    }

    u_result getDeviceInfo(w_RPlidarDriver* driver, rplidar_response_device_info_t& info, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->getDeviceInfo(info, timeout);
    }

    u_result setMotorPWM(w_RPlidarDriver* driver, _u16 pwm) {
        return driver->setMotorPWM(pwm);
    }

    u_result startMotor(w_RPlidarDriver* driver) {
        return driver->startMotor();
    }

    u_result stopMotor(w_RPlidarDriver* driver) {
        return driver->stopMotor();
    }

    u_result checkMotorCtrlSupport(w_RPlidarDriver* driver, bool& support, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->checkMotorCtrlSupport(support, timeout);
    }

    u_result setLidarIpConf(w_RPlidarDriver* driver, const rplidar_ip_conf_t& conf, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->setLidarIpConf(conf, timeout);
    }

    u_result getLidarIpConf(w_RPlidarDriver* driver, rplidar_ip_conf_t& conf, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->getLidarIpConf(conf, timeout);
    }

    u_result getDeviceMacAddr(w_RPlidarDriver* driver, _u8* macAddrArray, _u32 timeoutInMs = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->getDeviceMacAddr(macAddrArray, timeoutInMs);
    }

    u_result stop(w_RPlidarDriver* driver, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->stop(timeout);
    }

    u_result grabScanDataHq(w_RPlidarDriver* driver, rplidar_response_measurement_node_hq_t* nodebuffer, size_t& count, _u32 timeout = w_RPlidarDriver::DEFAULT_TIMEOUT) {
        return driver->grabScanDataHq(nodebuffer, count, timeout);
    }

    u_result ascendScanData(w_RPlidarDriver* driver, rplidar_response_measurement_node_hq_t* nodebuffer, size_t count) {
        return driver->ascendScanData(nodebuffer, count);
    }

    u_result getScanDataWithInterval(w_RPlidarDriver* driver, rplidar_response_measurement_node_t* nodebuffer, size_t& count) {
        return driver->getScanDataWithInterval(nodebuffer, count);
    }

    u_result getScanDataWithIntervalHq(w_RPlidarDriver* driver, rplidar_response_measurement_node_hq_t* nodebuffer, size_t& count) {
        return driver->getScanDataWithIntervalHq(nodebuffer, count);
    }
}
