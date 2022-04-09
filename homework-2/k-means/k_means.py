'''
*Copyright (c) 2022 All rights reserved
*@description: rough k means algorithm
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import time
from turtle import st
from evaluation import RandIndex,KappaIndex
from utils import ClusterGroup, EuclideanDistance, InitClusterKernels, UpdateClusterKernels


def K_means(dataset,k,threshold):

    # fig 1: omega from 0.1 to 0.9
    
    #for omega in range(8,10):

    start_time = time.time()
    omega = 1
    print(f'using omega {omega}')
    kernels,dimension = InitClusterKernels(dataset,k)
    #print(kernels)
    up_groups,down_groups = ClusterGroup(dataset,kernels,threshold)
    new_kernels = UpdateClusterKernels(up_groups,down_groups,dimension,dataset,omega)
    #print(new_kernels)
    
    step = 0
    while(new_kernels!=kernels):
        if step%5000 == 0:
            #tick = time.time()
            for i in range(k):
                print(EuclideanDistance(kernels[i],new_kernels[i]))
            print('----')
            # if tick-start_time > 50:
            #     return 'RESTART'
        step+=1
        kernels = new_kernels
        up_groups,down_groups = ClusterGroup(dataset,new_kernels,threshold)
        new_kernels = UpdateClusterKernels(up_groups,down_groups,dimension,dataset,omega)
    
    Rand_index , Kappa_index = RandIndex(dataset,new_kernels),KappaIndex(dataset,new_kernels)
    print(f'omege: ',omega)
    print('step: ',step)
    print('Rand: ',Rand_index)
    print('Kappa: ',Kappa_index)
    return 'END'