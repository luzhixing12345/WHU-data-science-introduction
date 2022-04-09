'''
*Copyright (c) 2022 All rights reserved
*@description: main function for K means
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''


import argparse
from config import ReadConfigFile
from datasets import GetDataset
from k_means import K_means


def main():
    '''
    the whole configuration is in `config.yaml`, I use the hyper parameters in the paper by default.
    Or you could manually change it as you like.
    '''
    
    cfg = ReadConfigFile()      
    for dataset in cfg['DATASETS']:
        dataset = GetDataset(dataset)
        while K_means(dataset,cfg['K'],cfg['THRESHOLD'])=='RESTART':
            print('restart')
        
    








if __name__ == "__main__":
    
  main()
