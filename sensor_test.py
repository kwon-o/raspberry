import cgsensor

bme280 = cgsensor.BME280(i2c_addr=0x77)
tsl2572 = cgsensor.TSL2572()

tsl2572.single_auto_measure()
bme280.forced()  # Forcedモードで測定を行い, 結果をtemperature, pressure, humidityに入れる
print('気温 {}°C'.format(bme280.temperature))  # 気温を取得して表示
print('湿度 {}%'.format(bme280.humidity))  # 湿度を取得して表示
print('気圧 {}hPa'.format(bme280.pressure))  # 気圧を取得して表示
print('明るさ {}lux'.format(tsl2572.illuminance))
