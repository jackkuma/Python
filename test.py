T = random.uniform(16,17.5)
H = random.uniform(54,55.5)
temperature = round(T, 1)
humidity = round(H, 1)
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

prevT = random.uniform(16,17.0)
prevTemp = round(prevT, 1)
prevH = random.uniform(54,55.0)
prevHum = round(prevH, 1)
print('前次溫度：', prevTemp, ' & 前次濕度：', prevHum)

if temperature < 17.1:
    temperature = temperature
else:
    print('實際溫度：', temperature)
    temperature = prevTemp

if humidity < 55.1:
    humidity = humidity
else:
    print('實際濕度：', humidity)
    humidity = prevHum

print('溫度：', temperature, ' & 濕度：', humidity, ' 取得時間：', date)
