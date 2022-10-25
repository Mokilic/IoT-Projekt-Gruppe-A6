'''
Using the MPU6050 inertial unit (accelerometer + gyrometer) with a Raspberry Pi Pico.
For more info:
bekyelectronics.com/raspberry-pi-pico-and-mpu-6050-micropython/
'''

from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time
from machine import Pin, I2C
import tm1637

tm = tm1637.TM1637(clk=Pin(4), dio=Pin(2))

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)

# Temperature display
print("Temperature: ", round(imu.temperature,2), "°C")

stadie = False
faldet = False
fald_count = 0


while True:
    # reading values
    acceleration = imu.accel
    gyroscope = imu.gyro
#     print("z:", round(acceleration.z,2))
    print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
           "z: ", round(acceleration.z,2))

    print ("gyroscope x: ", round(gyroscope.x,2), " y:", round(gyroscope.y,2),
           "z: ", round(gyroscope.z,2))

# data interpretation (accelerometer)

    if abs(acceleration.x) > 0.8:
        if (acceleration.x > 0):
            print("The x axis points upwards")
            stadie = False
            faldet = True
          
        else:
            print("The x axis points downwards")
            stadie = False
            faldet = True
           

    if abs(acceleration.y) > 0.8:
        if (acceleration.y > 0):
            print("The y axis points upwards")
            stadie = True
            faldet = False
            
        else:
            print("The y axis points downwards")
            stadie = False
            faldet = True
            

    if abs(acceleration.z) > 0.8:
        if (acceleration.z > 0):
            print("The z axis points upwards")
            stadie = False
            faldet = True
            
        else:
            print("The z axis points downwards")
            stadie = False
            faldet = True
           

# data interpretation (gyroscope)

#     if abs(gyroscope.x) > 20:
#         print("Rotation around the x axis")
# 
#     if abs(gyroscope.y) > 20:
#         print("Rotation around the y axis")
# 
#     if abs(gyroscope.z) > 20:
#         print("Rotation around the z axis")
    
    time.sleep(0.1)

#     if faldet == True:
#         print("jeg er faldet")
#     if stadie == True:
#         print("jeg står op")

        
    if faldet == True and stadie == False:
        fald_count = fald_count + 1
        print("tacklinger:", fald_count)
        time.sleep(5)

        
    if faldet == False and stadie == True:
        print("tacklinger:", fald_count)
        
        
    if stadie == True:
        print("STADIE ER TRUE")
    else:
        print("STADIE ER FALSE")
        
    if faldet == True:
        print("FALDET ER TRUE")
    else:
        print("FALDET ER FALSE")
   




        
        
        
    