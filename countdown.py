import time

inp = int(input("Please Enter Time in Second: "))


for i in range(inp, 0, -1):
  sec = i%60
  min = int(i/60) % 60
  hrs = int(i/3600) % 24
  days = int(i/86400)

  print(f"{days:02}:{hrs:02}:{min:02}:{sec:02}")
  time.sleep(1)

print("Time Up!")
