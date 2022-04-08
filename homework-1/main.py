'''
*Copyright (c) 2022 All rights reserved
*@description: Homework 1
*@author: Zhixing Lu
*@date: 2022-04-08
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import argparse
import math

def load_data(file_path = 'data.txt'):
    '''
    *@description: load data from file
    *@param: file_path
    *@return: data
    '''
    data = []
    with open(file_path, 'r',encoding='utf-8') as f:
        for line in f:
            data.append(line.strip().split(' '))
    return data

def gini_index(data):
    '''
    *@description: calculate gini index
    *@param: data
    *@return: gini_index
    '''
    gini_index = 0
    for i in range(len(data)):
        gini_index += (len(data[i]) / len(data)) * (1 - (len(data[i]) / len(data[i])))
    return gini_index

def entropy_index(data):
    '''
    *@description: calculate entropy index
    *@param: data
    *@return: entropy_index
    '''
    entropy_index = 0
    for i in range(len(data)):
        entropy_index += (len(data[i]) / len(data)) * (math.log2(len(data[i]) / len(data[i])))
    return entropy_index

def gini():
    pass

def entropy():
    pass

def main(args):
    '''
    *@description: main function
    *@param: args
    *@return: None
    '''
    data = load_data(args.file)
    
    if args.gini:
        gini()

    elif args.entropy:
        entropy()
        
    else :
        print('Please choose one of the following: gini or entropy, check README.md for more information')
        
    if args.draw:
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='data.txt', help='file path')
    parser.add_argument('--gini', action='store_true', help='use gini index')
    parser.add_argument('--entropy', action='store_true', help='use entropy index')
    parser.add_argument('--draw', action='store_true', help='draw the data in Graphviz')
    args = parser.parse_args()
    main(args)