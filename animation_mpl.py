# %%
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import pandas as pd
# Load the data
df = pd.read_csv(
    '/home/mrrobot/Documents/GitHub/posdoc_papers/analisis/scripts/analysis2.csv')

start = 14
stop = 16

df = df[(df['time'] >= start * 60) & (df['time'] <= stop * 60)]

# Total duration in seconds
total_duration = (stop - start) * 60  # 5 minutes (from 12 to 17 minutes)

# Number of frames
num_frames = len(df)

# Frame rate
frame_rate = num_frames / total_duration

# Create a new figure and axes
fig, ax = plt.subplots()

# Initialize the scatter plot and the label
scatter = ax.scatter([], [])
label = ax.text(0, 0, '', va='center')

# Define the initialization function
def init():
    ax.set_xlim(df['hx.m'].min(), df['hx.m'].max())
    ax.set_ylim(df['hy.m'].min(), df['hy.m'].max())
    return scatter, label

# Define the update function


def update(i, st=0):
    scatter.set_offsets(df[['hx.m', 'hy.m']].iloc[i])
    state = df['state_hmm_'].iloc[i]
    
    substate = df[f'substate_hmm{st}'].iloc[i]
    label.set_text(f'state {state}: {substate}')

    return scatter, label


# Create the animation
ani = FuncAnimation(fig, update, frames=len(
    df), init_func=init, blit=True, interval=1000 / frame_rate)

# Save the animation as a .mp4 file
ani.save('/home/mrrobot/Videos/anim.mp4', writer='ffmpeg', fps=frame_rate)

# %%
