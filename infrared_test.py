import subprocess
import cgsensor
import datetime
import time

bme280 = cgsensor.BME280(i2c_addr=0x77)
tsl2572 = cgsensor.TSL2572()


def run(command_str):
    proc = subprocess.run(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    return proc.stdout


while True:
    now = datetime.datetime.now()
    tsl2572.single_auto_measure()
    if now.hour == 21 and now.minute == 34 and now.second == 00:
        while tsl2572.illuminance > 30:
            run(['cgir send -c /home/pi/codes.json light_sw'])
            tsl2572.single_auto_measure()
            time.sleep(0.2)


