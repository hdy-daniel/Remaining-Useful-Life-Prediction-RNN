# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:19:33 2018

@author: lankuohsing
"""
# In[]
import numpy as np
import matplotlib.pyplot as plt
# In[]
S_list_2_130_25=[1253.8735450749314, 912.2786049269263, 833.3056242979882, 931.7096363800715,
 690.3143590508137, 1440.5369103393743, 993.975509552794, 1043.800252911044,
 1193.4032230119244, 918.070971173198, 1138.515062467922, 943.4362636111415,
 1069.807096456989, 775.8677288172244, 554.5347192116654, 1173.469458571364,
 1029.2290553257253, 830.0690112478753, 940.0054739277376, 673.6626921400181,
 1181.7956780746504, 925.2070590039439, 753.2382028455427, 770.1278915060424,
 677.843577878913, 994.0913498866823, 1299.6649629316373, 1119.830455578564,
 942.0013185223937, 647.9088342890474, 978.3388469114789, 918.8780057954466,
 771.0203151477928, 648.8584830303209, 580.0144959595906, 1065.8297994539787,
 1027.172134194293, 736.3482549258597, 789.7535829980512, 502.14772821160307]
S_np=np.array(S_list_2_130_25).reshape((2,4,5))
# In[]
num_layers_np=np.array([1,2])
lstm_size_np=np.array([100,110,120,130])
num_steps_np=np.array([5,10,15,20,25])
linestyle=['cx--','mo:','kp-.','bs--','p*:'] #红，绿，黄，蓝，粉,每个折线给不同的颜色
lstm_size_list=['100','110','120','130']
for i in range(S_np.shape[0]):
    plt.title('Test Result Analysis')
    plt.figure(i,figsize=(8,6))
    for j in range(S_np.shape[1]):

        plt.plot(num_steps_np,S_np[i,j,:],linestyle[j],label='lstm_size='+lstm_size_list[j])
        plt.tick_params(labelsize=20)
    plt.legend() # 显示图例
    plt.savefig('plot_test/'+'num_layers='+str(num_layers_np[i])+
                    '_lstm_size='+str(lstm_size_np[j])+'.png')
    plt.show()

# In[]
