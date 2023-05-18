import matplotlib.pyplot as plt
import numpy as npy
import pandas as pd
from matplotlib.animation import FuncAnimation



df=pd.read_csv("flightSimulatorResults.csv")

time=df['Time']
time=time[::10]
alt=df['Altitude']
alt=alt[::10]
vel=df['Velocity']
vel=vel[::10]
acc=df['Acceleration']
acc=acc[::10]
thr=df['Thrust']
thr=thr[::10]

fig, axis = plt.subplots(2, 2, figsize=(12,9))

axis[0,0].set_xlim(0, 50)
axis[0,0].set_ylim(0, 150)
axis[0,0].set_title('Time Vs Altitude')
axis[0,0].set_xlabel('time')
axis[0,0].set_ylabel('Altitude')

axis[0,1].set_xlim(0, 50)
axis[0,1].set_ylim(-10, 60)
axis[0,1].set_title('Time Vs Velocity')
axis[0,1].set_xlabel('time')
axis[0,1].set_ylabel('Velocity')

axis[1,0].set_xlim(0, 50)
axis[1,0].set_ylim(-10, 40)
axis[1,0].set_title('Time Vs Acceleration')
axis[1,0].set_xlabel('time')
axis[1,0].set_ylabel('Acceleration')

axis[1,1].set_xlim(0, 50)
axis[1,1].set_ylim(0, 25)
axis[1,1].set_title('Time Vs Thrust')
axis[1,1].set_xlabel('time')
axis[1,1].set_ylabel('Thrust')

for i in range(len(time)):
    axis[0,0].plot(time[:i], alt[:i], 'b-')
    axis[0,1].plot(time[:i], vel[:i], 'b-')
    axis[1,0].plot(time[:i], acc[:i], 'b-')
    axis[1,1].plot(time[:i], thr[:i], 'b-')
    fig.canvas.draw()
    plt.pause(0.000001)

plt.show()


