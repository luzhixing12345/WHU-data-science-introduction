'''
*Copyright (c) 2022 All rights reserved
*@description: useful functions
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import random

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


def ClusterGroup(dataset,kernels,threshold):
    '''
    cluster datset by kernels
    '''
    k = len(kernels)
    up_groups = [[ ] for i in range(k)]
    down_groups = [[ ] for i in range(k)]
 
    for data in dataset:    
        
        distances = [EuclideanDistance(data[0],kernels[i]) for i in range(k)]
        min_distance = min(distances)
        index = distances.index(min_distance)
        
        for i in range(k):
            if i == index:
                continue
            if distances[i]-min_distance<threshold:
                down_groups[i].append([
                    data[0],
                    data[1]
                ])
        #print(index)
        #print(data[0],data[1])
        up_groups[index].append([
            data[0], # data
            data[1]  # label
        ])
    # for group in groups:
    #     print(len(group))
        #print('\n')
    #groups = np.array(groups,dtype=object)
    return up_groups,down_groups
    
def UpdateClusterKernels(up_groups,down_groups,dimension,dataset,omega):
    '''
    update cluster kernels' postion
    new kernels are calculated by omega
    '''
    new_kernels = []
    for up_group,down_group in zip(up_groups,down_groups):
        if len(up_group)+len(down_group)!=0:
            kernel = [CalculatePosition(up_group,down_group,i,omega) for i in range(dimension)]
        else:
            kernel = InitClusterKernels(dataset,only_one=True)
        new_kernels.append(kernel)
        
    return new_kernels

def CalculatePosition(up_group,down_group,dimension,omega):
    up_sum = 0
    down_sum = 0
    up_cnt = 0
    down_cnt = 0
    for data,_ in up_group:
        up_sum+=data[dimension]
        up_cnt+=1
    
    for data,_ in down_group:
        down_sum+=data[dimension]
        down_cnt+=1
        
    answer = 0
    if up_cnt:
        answer += omega*(up_sum/up_cnt)
    if down_cnt:
        answer += (1-omega)*(down_sum/down_cnt)
    return answer

def EuclideanDistance(a,b):
    '''
    calculate euclidean distance between point A and point B
    '''
    assert len(a)==len(b)
    
    distance = 0
    for i in range(len(a)):
        distance += (a[i]-b[i])**2
    return distance**0.5
    
