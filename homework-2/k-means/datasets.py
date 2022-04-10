'''
*Copyright (c) 2022 All rights reserved
*@description: preprocess datasets data
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''
import numpy as np
import os
import random
from utils import draw_clusters

class K_means_Dataset:
    def __init__(self,name) -> None:
        self.name = name
        
        self.data = []
        self.class_name = {
            '1':0,
            '2':1,
            '3':2,
            'B':0,
            'L':1,
            'R':2,
            'Iris-setosa':0,
            'Iris-versicolor':1,
            'Iris-virginica':2
        }
        
        file = open(f'datasets/{name}/{name}.data','r')
        contents = file.readlines()
        for content in contents:
            datas = content[:-1].split(',')
            #print(datas)
            if name == 'Iris':
                self.data.append([
                    [float(i) for i in datas[:-1]],
                    self.class_name[datas[-1]]
                ])
            else:
                self.data.append([
                    [float(i) for i in datas[1:]],
                    self.class_name[datas[0]]
                ])
        file.close()
        self.data = np.array(self.data,dtype = object)
    
    def ShowDatasetInformation(self):
        print(f"\ndataset: {self.name}")
        print(f'size : {len(self.data)}')
        print('attribute numbers: '+str(len(self.data[0][0])))
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)
        

def get_standard_dataset(name):
    '''
    load k means dataset
    '''
    dataset = K_means_Dataset(name)
    dataset.ShowDatasetInformation()
    return dataset


def generator_dataset(cfg):
    '''
    generator dataset base on cfg and return dataset
    '''
    name = cfg['NAME']
    
    if not os.path.exists(f'datasets/{name}/{name}.data'):
        os.makedirs(f'datasets/{name}')
        
    file = open(f'datasets/{name}/{name}.data','w')
    
    data = generate_data(cfg)
    for i in range(len(data)):
        for j in range(len(data[i])):
            file.write(f'{data[i][j][0]},{data[i][j][1]},{i}\n')
    
    file.close()
    print(f'{name} dataset generated in datasets/{name}/{name}.data')
    
    dataset = reshape_standard_dataset(data)
    return dataset


def generate_data(cfg):
    '''
    generate data base on cfg
    create random points (x,y) in data_range in square of radius
    '''
    kernel_numbers = cfg['K']
    radius = cfg['RADIUS']
    data_range = cfg['RANGE']
    size = cfg['SIZE']
    
    data = [[] for _ in range(kernel_numbers)]
    for i in range(kernel_numbers):
        kernel_position = [random.uniform(data_range['min'],data_range['max']) for i in range(2)]
        # generate random data in square of radius with kernel_position as center
        for _ in range(size):
            x = random.uniform(-radius,radius)
            y = random.uniform(-radius,radius)
            data[i].append([x+kernel_position[0],y+kernel_position[1]])
            
    data = np.array(data,dtype = object)
    
    draw_clusters(data,kernel_numbers)
            
    # if dataset doesn't satisfy the requirement, restart
    
    restart = input('Does the data satisfy? Do you want to restart?(y/n)')
    if restart == 'y':
        return generate_data(cfg)
    else:   
        return data
    
def reshape_standard_dataset(data):
    '''
    reshape dataset to standard shape
    '''

    dataset = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            dataset.append([[data[i][j][0],data[i][j][1]],i])
    dataset = np.array(dataset,dtype = object)
    return dataset
