import numpy as np 
import matplotlib.pyplot as plt


data = np.array([[152,51],[156,53],[160,54],[164,55],
                 [168,57],[172,60],[176,62],[180,65],
                 [184,69],[188,72]])


print(data.shape)
x, y = data[:,0].reshape(-1,1),data[:,1]
plt.scatter(x, y, color='black')
# 画x,y轴的标题
plt.xlabel('height (cm)')
plt.ylabel('weight (kg)')
plt.show() # 展示