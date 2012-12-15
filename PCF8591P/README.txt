PCF8591P I2C 4 chan ADC 1 chan DAC Class for use this Raspberry Pi

History
-------

0.0.3	15 Dec 12	Added acknowledgements, comments & instructions.
0.0.2	14 Dec 12	Added methods for enabling, disabling and setting the DAC output value
0.0.1	11 Dec 12	First attempt.  Methods for reading ADC channels.

Acknowledgements
----------------

Help with getting started with this device came from Mike 'Grumpy' Cook on the
Raspberry Pi Forums (http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=15578)

Mike's very interesting site can be found at: http://www.thebox.myzen.co.uk/Site/Welcome.html

Introduction
------------

This class provides methods to control the PCF8591P ADC/DAC integrated circuit.  Datasheet
can be found at http://www.nxp.com/documents/data_sheet/PCF8591.pdf.

The class provides the following functionality:

	Construct a PCF8581 object by passing the the SMB Bus object and device I2C address
	Read a single ADC channel
	Read all ADC channels
	Set the DAC output
	Enable & disable the DAC output

Instructions
------------

An introduction on how to connect up the device can be found at http://blog.jacobean.net/?p=258
ADC inputs should be grounded when not in use.

Instructions for configuring the Raspberry Pi to use I2C can be found at:
http://blog.jacobean.net/?p=64

Code Example
------------

    from smbus import SMBus
    
    i2c = SMBus(0) # on a Rev 1 board
    # i2c = SMBus(1) # if on a Rev 2 board
    
    # Create a PCF8591P object
    sensor = PCF8591P(i2c, 0x48)
    
    # Read individual ADC channels
    reading = sensor.readADC(0)
    print "0: {0}".format(reading)
    reading = sensor.readADC(1)
    print "1: {0}".format(reading)
    reading = sensor.readADC(2)
    print "2: {0}".format(reading)
    reading = sensor.readADC(3)
    print "3: {0}".format(reading)

	# Read all ADC channels
    reading = sensor.readAllADC()
    print reading
    
    # Set DAC output and enable
    sensor.writeDAC(255)
    
    # Disable DAC output  
    sensor.disableDAC()
    
    # Enable DAC output
    sensor.enableDAC()
    
    
