'''
Created on 12 Dec 2012

@author: Jamie
'''
'''
Created on 28 Nov 2012
@author: Jamie
'''

# First version of PCF8591P I2C ADC/DAC class.
# ToDo:
#    Add DAC functionality


class I2CaddressOutOfBoundsError(Exception):
    message = 'I2C Exception: I2C Address Out of Bounds'

class PCF8591PchannelOutOfBoundsError(Exception):
    message = 'PCF8591P Exception: ADC Channel Out of Bounds'

class PCF8591P:

    def __init__(self, __i2cBus, __addr):
        self.__bus = __i2cBus
        self.__addr = self.__checkI2Caddress(__addr)
        
    def __checkI2Caddress(self, __addr):
        if type(__addr) is not int:
            raise I2CaddressOutOfBoundsError
        elif (__addr < 0):
            raise I2CaddressOutOfBoundsError
        elif (__addr > 127):
            raise I2CaddressOutOfBoundsError
        return __addr

    def __checkChannelNo(self, __chan):
        if type(__chan) is not int:
            raise PCF8591PchannelOutOfBoundsError
        elif (__chan < 0):
            raise PCF8591PchannelOutOfBoundsError
        elif (__chan > 3):
            raise PCF8591PchannelOutOfBoundsError
        return __chan


    def readADC(self, __chan = 0):
        __checkedChan = self.__checkChannelNo(__chan)
        self.__bus.write_byte(self.__addr, __checkedChan) # set control register to read channel 0
        __reading = self.__bus.read_byte(self.__addr) # seems to need to throw away first reading
        __reading = self.__bus.read_byte(self.__addr) # read A/D
        return __reading
        
    def readAllADC(self):
        __readings = []
        self.__bus.write_byte(self.__addr, 0x44)
        __reading = self.__bus.read_byte(self.__addr) # seems to need to throw away first reading
        for i in range (4):
            __readings.append(self.__bus.read_byte(self.__addr)) # read ADC
        return __readings       

if __name__ == "__main__":

    from smbus import SMBus
    
    i2c = SMBus(0)

    try:
        sensor = PCF8591P()
    except Exception as e:
        print "Passed:  missing parameters" + e.message
    try:
        sensor = PCF8591P(i2c)
    except Exception as e:
        print "Passed:  missing address parameter" + e.message
    try:
        sensor = PCF8591P(i2c, 'cheese')
    except I2CaddressOutOfBoundsError as e:
        print "Passed:  " + e.message
    try:
        sensor = PCF8591P(i2c, -1)
    except I2CaddressOutOfBoundsError as e:
        print "Passed:  " + e.message
    try:
        sensor = PCF8591P(i2c, 128)
    except I2CaddressOutOfBoundsError as e:
        print "Passed:  " + e.message
    try:
        sensor = PCF8591P(i2c, 0x48)
    except Exception as e:
        print "Fail!!  Something went wrong!!" + e.message

    try:
        sensor.readADC()
        print "Passed:  default parameter"
    except PCF8591PchannelOutOfBoundsError as e:
        print "Fail!!  Something went wrong!!" + e.message
    try:
        print sensor.readADC(-1)
    except PCF8591PchannelOutOfBoundsError as e:
        print "Passed:  " + e.message
    try:
        print sensor.readADC(4)
    except PCF8591PchannelOutOfBoundsError as e:
        print "Passed:  " + e.message
    try:
        print sensor.readADC('cheese')
    except PCF8591PchannelOutOfBoundsError as e:
        print "Passed:  " + e.message

    reading = sensor.readADC(0)
    print "0: {0}".format(reading)
    reading = sensor.readADC(1)
    print "1: {0}".format(reading)
    reading = sensor.readADC(2)
    print "2: {0}".format(reading)
    reading = sensor.readADC(3)
    print "3: {0}".format(reading)

    reading = sensor.readAllADC()
    print reading
