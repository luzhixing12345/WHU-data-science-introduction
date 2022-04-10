'''
*Copyright (c) 2022 All rights reserved
*@description: k means algorithm
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import time
import random
from evaluation import RandIndex
import matplotlib.pyplot as plt
from utils import *
import numpy as np

def K_means(dataset,k,show_each_step = False):
    '''
    k-means algorithm for clustering dataset
    '''
    start_time = time.time()
    kernels,dimension = InitClusterKernels(dataset,k)
    #print(kernels)
    groups = ClusterGroup(dataset,kernels)
    new_kernels = UpdateClusterKernels(groups,dimension,dataset)
    #print(new_kernels)
    print('start clustering...')
    step = 0
    plt.ion()
    while(new_kernels!=kernels):
        if step%5000 == 0:
            tick = time.time()
            # for i in range(k):
            #     print(EuclideanDistance(kernels[i],new_kernels[i]))
            # print('----')
            if tick-start_time > 50:
                return 'RESTART'
        step+=1
        kernels = new_kernels
        groups = ClusterGroup(dataset,new_kernels)
        if show_each_step:
            draw_clusters(groups,k,show_each_step)
            plt.pause(0.1)
        new_kernels = UpdateClusterKernels(groups,dimension,dataset)
    plt.ioff()
    print('-----------------------------------------------------\n')
    print('K-means algorithm finished!')
    plt.show(block=False)
    plt.pause(1)
    Rand_index = RandIndex(k,groups)
    print('total step: ',step)
    print('Rand: ',Rand_index)
    return 'END'


def InitClusterKernels(dataset,k = 3,only_one = False):
    '''
    return k kernels from dataset
    '''
    kernels = []
    
    dimension = len(dataset[0][0])
    value_ranges = []
    for d in range(dimension):
        value_ranges.append({
            'max': max(dataset[:,0][d]),
            'min': min(dataset[:,0][d])
        })
    
    for _ in range(k):
        kernel = []
        for d in range(dimension):
            kernel.append(random.uniform(value_ranges[d]['min'],value_ranges[d]['max']))
        if only_one:
            return kernel
        kernels.append(kernel)
    return kernels,dimension


def ClusterGroup(dataset,kernels):
    '''
    cluster datset by kernels
    '''
    k = len(kernels)
    groups = [[] for _ in range(k)]
    for data in dataset:    
        
        distances = [EuclideanDistance(data[0],kernels[i]) for i in range(k)]
        min_distance = min(distances)
        index = distances.index(min_distance)
        
        #print(index)
        #print(data[0],data[1])
        groups[index].append([
            data[0], # data
            data[1]  # label
        ])
    # for group in groups:
    #     print(len(group))
        #print('\n')
    groups = np.array(groups,dtype=object)
    return groups
    
def UpdateClusterKernels(groups,dimension,dataset):
    '''
    update cluster kernels' postion
    '''
    new_kernels = []
    for group in groups:
        if len(group)!=0:
            kernel = [CalculatePosition(group,i) for i in range(dimension)]
        else:
            kernel = InitClusterKernels(dataset,only_one=True)
        new_kernels.append(kernel)
        
    return new_kernels

def CalculatePosition(group,dimension):
    
    sum = 0
    cnt = 0
    
    for data in group:
        sum += data[0][dimension]
        cnt += 1
    return sum/cnt
        


def EuclideanDistance(a,b):
    '''
    calculate euclidean distance between point A and point B
    '''
    assert len(a)==len(b)
    
    distance = 0
    for i in range(len(a)):
        distance += (a[i]-b[i])**2
    return distance**0.5