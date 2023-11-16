#importo le librerie
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = './results/matTFile'
img_filename = './results/matTImg'

# Set the style
sns.set_style("whitegrid")
# sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 2.5})

# Read the data
df = pd.read_csv(filename + '.csv')
# df['wall_clock_time_routine2'].replace(to_replace=0, value=0.0000001, inplace=True)
print(df)

# Filter the data
df_serial = df[df['compilation_notes'] == 'SERIAL_CODE']
# df_avx = df[df['notes'] == 'avx'][df['node'] == 'hpc-c11-node23.unitn.it']
# #df_ftree = df[df['notes'] == 'ftree'][df['node'] == 'hpc-c11-node23.unitn.it']


print('df_serial',df_serial)
# print('df_avx',df_avx)
# #print(df_ftree)

# # Create a scatter plot
sns.lineplot(x='matrix_size', y='matT_wallTime[us]', data=df_serial, label='Serial', color='red')
# sns.lineplot(x='n', y='wall_clock_time_routine2', data=df_serial, label='Restrict flag', color='blue')
# sns.lineplot(x='n', y='wall_clock_time_routine2', data=df_avx, label='Vectorized + flag', color='green')

# # Add title and axis names
plt.title('Wall time')
plt.xlabel('Size')
# plt.ylabel('Time [s]')
plt.ylabel('$log_2(t) [s]$')
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