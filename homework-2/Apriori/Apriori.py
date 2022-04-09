'''
*Copyright (c) 2022 All rights reserved
*@description: apriori algorithm
*@author: Zhixing Lu
*@date: 2022-04-09
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import argparse
from itertools import chain
import re
from record import record

def load_dataset(args):
    '''
    *@description: load data from file
    *@param: args
    *@return: data and label
    '''
    data = []
    file_name = 'dataset.txt' if args.dataset else 'example.txt'
        
    file = open(file_name, 'r')
    for line in file:
        values = re.findall(r'\d+', line)[1:]
        data.append(values)
    file.close()

    return data


def generate_components(keys,number):
    '''
    @description: generate all possible combinations of keys 
    @param: keys, number
    @return: components
    '''
    components = []
    dfs([],0,number,keys,components)
    return components


def dfs(component_set,pointer,k,keys,components):
    '''
    *@description: use dfs to generate all possible combinations of keys
    *@param: k: length of combination, keys: all possible keys, components: all possible combinations
    *@return: None
    '''
    if k==0:
        components.append(tuple(component_set))
        return
    if pointer == len(keys):
        return
    while pointer < len(keys):
        component_set.append(keys[pointer])
        dfs(component_set.copy(),pointer+1,k-1,keys,components)
        component_set.pop()
        pointer += 1

def build_frequent_itemsets(keys, data, min_support):
    '''
    *@description: build frequent itemsets
    *@param: keys, data, min_support
    *@return: frequent_itemsets
    '''
    frequent_itemsets = {}
    for key in keys:
        frequent_itemsets[key] = 0
    
    for i in range(len(data)):
        for key in keys:
            if set(key).issubset(set(data[i])):
                frequent_itemsets[key] += 1
    frequent_itemsets = {k:v for k,v in frequent_itemsets.items() if v >= min_support}
    
    return frequent_itemsets
            

def build_association_rules(frequent_itemsets, data, min_confidence):
    '''
    *@description: build association rules
    *@param: frequent_itemsets, data, min_confidence
    *@return: association_rules
    '''
    association_rules = []
    for k,v in frequent_itemsets.items():
        keys = list(k)
        keys = generate_components(keys,len(keys)-1)
        for key in keys:
            cnt = 0
            for i in range(len(data)):
                if set(key).issubset(set(data[i])):
                    cnt += 1
            confidence = v/cnt
            if confidence >= min_confidence:
                association_rules.append([key,k,confidence])
    return association_rules


def get_keys_from_frequent_itemsets(frequent_itemsets):
    '''
    *@description: get all distinct keys from frequent itemsets
    *@param: frequent_itemsets
    *@return: keys
    '''
    return list(set(chain(*[list(i) for i in frequent_itemsets.keys()])))



def main(args):
    '''
    *@description: main function
    *@param: args
    *@return: None
    '''
    data = load_dataset(args)
    n = len(data)
    print('Number of transactions:', n)
    
    if args.dataset:
        min_support = int(n * args.min_support)
        confidence = args.min_confidence
    else:
        min_support = int(n * 0.5)
        confidence = 0.7

    # get all keys from data
    keys = [(i,) for i in set(list(chain(*data)))]
    # record all frequent itemsets
    total_frequent_itemsets = {}
    id = 1
    
    frequent_itemsets = build_frequent_itemsets(keys, data, min_support)
    association_rules = []
    while True:
        total_frequent_itemsets[id] = frequent_itemsets
        id += 1
        keys = get_keys_from_frequent_itemsets(frequent_itemsets)
        keys = generate_components(keys,id)
        frequent_itemsets = build_frequent_itemsets(keys,data, min_support)
        if frequent_itemsets == {}:
            break
        else:
            association_rules.append(build_association_rules(frequent_itemsets, data, confidence))

    record(total_frequent_itemsets, association_rules,args.dataset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--dataset',action='store_true')
    parser.add_argument('-s','--min_support',type=float,default=0.03)
    parser.add_argument('-c','--min_confidence',type=float,default=0.7)
    args = parser.parse_args()
    main(args)