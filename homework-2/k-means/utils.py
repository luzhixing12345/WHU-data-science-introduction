'''
*Copyright (c) 2022 All rights reserved
*@description: useful functions
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import matplotlib.pyplot as plt

    
def draw_clusters(groups,kernels,step = False):
    '''
    draw clusters with kernels in different colors by matplotlib
    '''
    colors = ['r','g','b','c','m','y','k']
    for i in range(kernels):
        if step:
            x = []
            y = []
            for j in groups[i]:
                x.append(j[0][0])
                y.append(j[0][1])
            plt.scatter(x,y,color = colors[i])
        else:
            plt.scatter(groups[i][:,0],groups[i][:,1],color=colors[i])
    
    # wait for 2 seconds and close the figure
    if not step:
        plt.show(block=False)
        plt.savefig('clusters_before.png')
        plt.pause(2)
        plt.close()
    else :
        plt.savefig('clusters_after.png')
