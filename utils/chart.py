#importo le librerie
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = './results/matTFile'
img_filename = './results/matTImg'

filename_block = './results/matBlockTFile'
img_filename_block = './results/matBlockTImg'

# Set the style
sns.set_style("whitegrid")
# sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 2.5})

# Read the data
df = pd.read_csv(filename + '.csv')
df_block = pd.read_csv(filename_block + '.csv')
# df['wall_clock_time_routine2'].replace(to_replace=0, value=0.0000001, inplace=True)
# print(df)
# print(df_block)

# Filter the data
df_serial = df[df['compilation_notes'] == 'SERIAL_CODE']
df_serial_block = df_block[df_block['compilation_notes'] == 'SERIAL_CODE']
# df_avx = df[df['notes'] == 'avx'][df['node'] == 'hpc-c11-node23.unitn.it']
# #df_ftree = df[df['notes'] == 'ftree'][df['node'] == 'hpc-c11-node23.unitn.it']


# print('df_serial',df_serial)
# print('df_serial_block',df_serial_block)
# print('df_avx',df_avx)
# #print(df_ftree)


########### Normal Transpose ###########
# # Create a scatter plot
sns.lineplot(x='matrix_size', y='matT_wallTime[us]', data=df_serial, label='Serial', color='red')
# sns.lineplot(x='n', y='wall_clock_time_routine2', data=df_serial, label='Restrict flag', color='blue')
# sns.lineplot(x='n', y='wall_clock_time_routine2', data=df_avx, label='Vectorized + flag', color='green')

# # Add title and axis names
plt.title('Wall time')
plt.xlabel('Size')
# plt.ylabel('Time [s]')
plt.ylabel('$log_2(t) [us]$')
plt.xscale('log')
# plt.yscale('log')

ticks = []
ticks_labels = []

for i in range(4, 12):
    ticks.append(2**i)
    ticks_labels.append('$2^{' + str(i) + '}$')
    
plt.xticks(ticks, ticks_labels)
plt.legend()
plt.savefig(img_filename + '.png')
plt.show()

plt.yscale('log')
plt.savefig(img_filename + '-log.png')

########### Block Transpose ###########
plt.clf()

# # Create a scatter plot
sns.lineplot(x='matrix_size', y='matBlockT_wallTime[us]', data=df_serial_block, hue=df_serial_block['blockSize'].astype(str), palette='colorblind', legend='full')

# # Add title and axis names
plt.title('Wall time')
plt.xlabel('Size')
plt.ylabel('$log_2(t) [us]$')
plt.xscale('log')

# # Add tiks to x axis
ticks = []
ticks_labels = []

for i in range(4, 12):
    ticks.append(2**i)
    ticks_labels.append('$2^{' + str(i) + '}$')
    
plt.xticks(ticks, ticks_labels)
plt.legend()
plt.savefig(img_filename_block + '.png')
plt.show()
plt.yscale('log')
plt.savefig(img_filename_block + '-log.png')