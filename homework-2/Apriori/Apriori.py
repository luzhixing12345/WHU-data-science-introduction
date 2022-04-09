'''
*Copyright (c) 2022 All rights reserved
*@description: apriori algorithm
*@author: Zhixing Lu
*@date: 2022-04-09
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import argparse


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
        data.append(line.strip('\n').split(',')[1:])
    file.close()

    return data

def build_frequent_itemsets(data, min_support):
    '''
    *@description: build frequent itemsets
    *@param: data, min_support
    *@return: frequent_itemsets
    '''
    frequent_itemsets = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in frequent_itemsets:
                frequent_itemsets[data[i][j]] = 1
            else:
                frequent_itemsets[data[i][j]] += 1
    frequent_itemsets = {k:v for k,v in frequent_itemsets.items() if v >= min_support}
    return frequent_itemsets

def build_association_rules(frequent_itemsets, min_confidence):
    '''
    *@description: build association rules
    *@param: frequent_itemsets, min_confidence
    *@return: association_rules
    '''
    association_rules = {}
    for k,v in frequent_itemsets.items():
        for i in range(len(k)):
            for j in range(i+1, len(k)):
                antecedent = k[:i] + k[i+1:]
                consequent = k[i:j]
                confidence = v / frequent_itemsets[antecedent]
                if confidence >= min_confidence:
                    association_rules[(antecedent, consequent)] = confidence
    return association_rules

def print_association_rules(association_rules):
    '''
    *@description: print association rules
    *@param: association_rules
    *@return: None
    '''
    for k,v in association_rules.items():
        print(k,v)
        
        


def main(args):
    '''
    *@description: main function
    *@param: args
    *@return: None
    '''
    data = load_dataset(args)
    n = len(data)
    
    if args.dataset:
        min_support = int(n * args.min_support)
        confidence = args.min_confidence
    else:
        min_support = int(n * 0.5)
        confidence = 0.7
    
    frequent_itemsets = build_frequent_itemsets(data, min_support)
    print(frequent_itemsets)
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--dataset',action='store_true')
    parser.add_argument('-s','--min_support',type=float,default=0.03)
    parser.add_argument('-c','--min_confidence',type=float,default=0.7)
    args = parser.parse_args()
    main(args)