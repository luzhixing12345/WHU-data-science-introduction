'''
*Copyright (c) 2022 All rights reserved
*@description: preprocess datasets data
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''
import numpy as np

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
        

def GetDataset(name):
    '''
    load k means dataset
    '''
    dataset = K_means_Dataset(name)
    dataset.ShowDatasetInformation()
    return dataset