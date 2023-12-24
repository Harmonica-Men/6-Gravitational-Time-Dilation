# Compute Gravitational Time Dilation #
# Ratio is ratio of circum/circum(hole) #
# time2 elapsed time, near black hole #
# time1 elapsed time, far away from hole #

import math

ratio = 0.0
time2 = 0.0
time1 = 1.0
i = 0

print("Steps  C/Ch  Time 1 (days)  Time2 (days) \n")
for j in range(21):
   ratio = 1 + (0.5 ** i)
   i += 1
   time2 = time1 / math.sqrt(1.0 - 1.0 / ratio)
   print(f"j={j}, ratio={ratio}  time1={time1}  time2={time2}")
