# Compute Gravitational Time Dilation #
# Ratio is ratio of circum/circum(hole) #
# time2 elapsed time, near black hole #
# time1 elapsed time, far away from hole #


import pandas as pd
import math

# Initialize lists to store values
steps = []
c_ch = []
time1_list = []
time2_list = []

ratio = 0.0
time2 = 0.0
time1 = 1.0
i = 0

print("Steps  C/Ch  Time 1 (days)  Time2 (days) \n")
for j in range(21):
    ratio = 1 + (0.5 ** i)
    i += 1
    time2 = time1 / math.sqrt(1.0 - 1.0 / ratio)

    # Append values to lists
    steps.append(j)
    c_ch.append(ratio)
    time1_list.append(time1)
    time2_list.append(time2)

# Create a DataFrame using Pandas
data = {
    'Steps': steps,
    'C/Ch': c_ch,
    'Time 1 (days)': time1_list,
    'Time 2 (days)': time2_list
}

df = pd.DataFrame(data)
print(df)
