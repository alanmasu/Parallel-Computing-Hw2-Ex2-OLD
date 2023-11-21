#importo le librerie
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

infoFile = open('./results/infoFile.csv', 'r')
info = infoFile.readline()
infoarr = info.split(',')

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
def filter(row):
    cores = row.compilation_notes.split(';')
    # print(cores)
    if cores[1] == 'SERIAL_CODE':
        return 0
    return cores[1]
    
df_strong = df[(df['compilation_notes'].str.contains('WEAK_SCALING') == True) & (df['run_notes']==infoarr[1])]
df_strong['cores'] = df_strong.apply(lambda row: filter(row), axis=1)

print('df_strong',df_strong)

# print('df_serial',df_serial)
# print('df_serial_block',df_serial_block)
# print('df_avx',df_avx)
# #print(df_ftree)


########### Normal Transpose ###########
# # Create a scatter plot
sns.lineplot(x=df_strong['cores'].astype(str), y='matTpar_wallTime[us]', data=df_strong, color='red', label='Parallel')
sns.lineplot(x=df_strong['cores'].astype(str), y='matT_wallTime[us]', data=df_strong, color='blue', label='Serial')

# # # Add title and axis names
plt.title('Strong scaling')
plt.xlabel('Cores')
plt.ylabel('Time [us]')
# plt.xscale('log')
plt.yscale('log')

ticks = []
ticks_labels = []
ticks.append(0)
ticks_labels.append('Serial')

for i in range(0, 7):
    ticks.append(i+1)
    ticks_labels.append(str(2**i))

plt.xticks(ticks, ticks_labels)
# plt.legend()
plt.savefig(img_filename+ '-weakScaling-' + infoarr[1] + '.png')
plt.show()

# plt.yscale('log')
# plt.savefig(img_filename + '-log.png')

########### Block Transpose ###########
# plt.clf()

# # # Create a scatter plot
# sns.lineplot(x='matrix_size', y='matBlockT_wallTime[us]', data=df_serial_block, hue=df_serial_block['blockSize'].astype(str), palette='colorblind', legend='full')

# # # Add title and axis names
# plt.title('Wall time')
# plt.xlabel('Size')
# plt.ylabel('$t [us]$')
# plt.xscale('log')

# # # Add tiks to x axis
# ticks = []
# ticks_labels = []

# for i in range(4, 12):
#     ticks.append(2**i)
#     ticks_labels.append('$2^{' + str(i) + '}$')
    
# plt.xticks(ticks, ticks_labels)
# plt.legend()
# # # Save the plot
# plt.savefig(img_filename_block + '.png')
# plt.show()

# # # Change the y axis scale to log and save the plot
# plt.yscale('log')
# plt.ylabel('$log_2(t) [us]$')

# plt.savefig(img_filename_block + '-log.png')