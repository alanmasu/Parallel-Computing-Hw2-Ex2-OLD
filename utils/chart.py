#importo le librerie
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import create_run_folder as crf

## Create the run folder
runDir = crf.createFolder()
if 'error' in runDir :
    print('Error on create run folder')
    runDir = './results'

filename = runDir + '/matTFile'
img_filename = runDir + '/matTImg'

filename_block = runDir + '/matBlockTFile'
img_filename_block = runDir + '/matBlockTImg'

infoFileName = runDir + '/infoFile.csv'

infoFile = open(infoFileName, 'r')
info = infoFile.readline()
infoarr = info.split(',')



# Set the style
sns.set_style("whitegrid")
# sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 2.5})

# Read the data
df = pd.read_csv(filename + '.csv')
df.dropna(inplace=True)
print(df)

# # Filter the data
df_serial = df[df['compilation_notes'].str.contains('TEST_PARALLELISM')]


# print('df_serial',df_serial)
# print('df_serial_block',df_serial_block)
# print('df_avx',df_avx)
# #print(df_ftree)


########### Normal Transpose ###########
# # Create a scatter plot
sns.lineplot(x='matrix_size', y='matT_wallTime[us]', data=df_serial, label='Serial', color='red')
sns.lineplot(x='matrix_size', y='matTpar_wallTime[us]', data=df_serial, label='Parallel', color='blue')
# sns.lineplot(x='n', y='wall_clock_time_routine2', data=df_serial, label='Restrict flag', color='blue')
# sns.lineplot(x='n', y='wall_clock_time_routine2', data=df_avx, label='Vectorized + flag', color='green')

# # Add title and axis names
plt.title('Wall time')
plt.xlabel('Size')
plt.ylabel('Time [us]')
plt.xscale('log')

ticks = []
ticks_labels = []

for i in range(9, 14):
    ticks.append(2**i)
    ticks_labels.append(str(2**i))
    
plt.xticks(ticks, ticks_labels)
plt.legend()
plt.savefig(img_filename + '-test-par.png')
plt.show()

plt.yscale('log')
plt.savefig(img_filename + '-test-par-log.png')

# ########### Block Transpose ###########
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