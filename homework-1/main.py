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
from draw import draw_tree

def load_data(file_path = 'data.txt'):
    '''
    *@description: load data from file
    *@param: file_path
    *@return: data and label
    '''
    data = []
    label = []
    with open(file_path, 'r',encoding='utf-8') as f:
        for line in f:
            data.append(line.strip().split(' ')[1:-1])
            label.append(line.strip().split(' ')[-1])
    return data, label

def gini_index(data,label):
    '''
    *@description: calculate gini index
    *@param: data
    *@return: gini_index
    '''
    gini_index = 0
    for i in range(len(data)):
        if len(data[i]) == 0:
            continue
        sub_gini_index = 0
        cnt_true = 0
        cnt_false = 0
        for j in data[i]:
            if label[j]=='是':
                cnt_true += 1
            else:
                cnt_false += 1
        #print(cnt_true,cnt_false)
        sub_gini_index = 1 - (cnt_true / len(data[i])) ** 2 - (cnt_false / len(data[i])) ** 2
        gini_index += (len(data[i]) / len(label)) * sub_gini_index
    #print(gini_index)
    return gini_index

def entropy_index(data,label):
    '''
    *@description: calculate entropy index
    *@param: data
    *@return: entropy_index
    '''
    entropy_index = 0
    for i in range(len(data)):
        if len(data[i]) == 0:
            continue
        sub_entropy_index = 0
        cnt_true = 0
        cnt_false = 0
        for j in data[i]:
            if label[j]=='是':
                cnt_true += 1
            else:
                cnt_false += 1
        #print(cnt_true,cnt_false)
        if cnt_false != 0 and cnt_true != 0:
            sub_entropy_index = -(cnt_true / len(data[i])) * math.log2(cnt_true / len(data[i])) - (cnt_false / len(data[i])) * math.log2(cnt_false / len(data[i]))
        elif cnt_false == 0:
            sub_entropy_index = -(cnt_true / len(data[i])) * math.log2(cnt_true / len(data[i]))
        elif cnt_true == 0:
            sub_entropy_index = -(cnt_false / len(data[i])) * math.log2(cnt_false / len(data[i]))
        entropy_index += (len(data[i]) / len(label)) * sub_entropy_index
    #print(entropy_index)
    return entropy_index


def house_index(args,data,label,id=0):
    
    result = [[] for _ in range(2)]
    
    for i in range(len(data)):
        if data[i][id] == "否":
            result[0].append(i)
        else:
            result[1].append(i)
    #print(result)
    if args.gini:
        return gini_index(result,label)
    elif args.entropy:
        return entropy_index(result,label)

def married_index(args,data,label,id=1):
    
    result = [[] for _ in range(2)]
    
    for i in range(len(data)):
        
        if data[i][id] == "已婚":
            result[0].append(i)
        else:
            result[1].append(i)
            
    if args.gini:
        return gini_index(result,label)
    elif args.entropy:
        return entropy_index(result,label)

def income_index(args,data,label,id=2):
        
    incomings = []
    
    for i in range(len(data)):
        incomings.append(int(data[i][id][:-1]))
    min_income = min(incomings)
    max_income = max(incomings)
    
    min_index = 1
    finial_income = 0
    
    for income in range(min_income,max_income+1):
        result = [[] for _ in range(2)]

        for i in range(len(data)):
            if int(data[i][id][:-1]) < income:
                result[0].append(i)
            else:
                result[1].append(i)
        #print(result)
        if args.gini:
            if gini_index(result,label) < min_index:
                min_index = gini_index(result,label)
                #print(min_index)
                finial_income = income
        elif args.entropy:
            if entropy_index(result,label) < min_index:
                min_index = entropy_index(result,label)
                finial_income = income
        #print(income,min_index)
    # print(finial_income)
    # print(min_index)
    return [finial_income,min_index]
    

def main(args):
    '''
    *@description: main function
    *@param: args
    *@return: None
    '''
    if not args.gini and not args.entropy:
        print('Please choose one of the following: gini or entropy, check README.md for more information')
        return
    
    data,label  = load_data(args.file)
    # print(data,label)
    tags = {
        'house':house_index,
        'married':married_index,
        'income':income_index
    }
    indexes = {}
    
    for id,key in enumerate(tags.keys()):
        indexes[key] = tags[key](args,data,label,id)
    print(indexes)
            
    if args.draw:
        if args.gini:
            draw_tree(data,indexes,'gini')
        elif args.entropy:
            draw_tree(data,indexes,'entropy')
        else:
            raise Exception('Please choose one of the following: gini or entropy, check README.md for more information')
        print('Draw tree successfully')

    print('Done')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='data.txt', help='file path')
    parser.add_argument('--gini', action='store_true', help='use gini index')
    parser.add_argument('--entropy', action='store_true', help='use entropy index')
    parser.add_argument('--draw', action='store_true', help='draw the data in Graphviz')
    args = parser.parse_args()
    main(args)