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
from datasets import generator_dataset, get_standard_dataset
from k_means import K_means


def main(args):
    '''
    the whole configuration is in `config.yaml`, I use the hyper parameters in the paper by default.
    Or you could manually change it as you like.
    '''
    
    cfg = ReadConfigFile(args.config)
    
    if args.random:
        dataset = generator_dataset(cfg)
        while K_means(dataset,cfg['K'],show_each_step=True)=='RESTART':
            print('restart')
    else:
        for dataset in cfg['DATASETS']:
            dataset = get_standard_dataset(dataset)
            while K_means(dataset,cfg['K'])=='RESTART':
                print('restart')
    print('END')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.yaml', help='config file')
    parser.add_argument('-r','--random', action='store_true', help='randomly generate the dataset')
    args = parser.parse_args()
    main(args)
