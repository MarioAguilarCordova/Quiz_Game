
import os
import matplotlib.pyplot as plt
import numpy as np
import time

# x = [[3,4],[4,3]]

# xpoints = np.array([3,4])
# ypoints = np.array([5,6])

# plt.plot(xpoints,ypoints)
# plt.show()

flags = os.O_RDWR | os.O_CREAT

path = './caramelo.txt'

cara = os.open(path,flags)

print("File Opened successfully")

str4cara = "Hello my poochie I love you lots"

os.write(cara,str4cara.encode())

print("String written to file destination")

os.lseek(cara, 0, 0)

str4cara = os.read(cara, os.path.getsize(path))

print("\nString read from the file descriptor.")
print(str4cara.decode())

# Close the file descriptor

os.close(cara)

print("\nFile descriptor closed succesfully")



# answer = np.prod(x)

time.sleep(5)

print("")

print("Hello World")

# print(answer)


