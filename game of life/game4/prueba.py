import time

print(float(10.0-9.2))

t = 0
t0 = 0.2
while True:
    time.sleep(t0)
    t += t0
    print(t)