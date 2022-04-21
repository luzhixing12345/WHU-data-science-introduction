'''
*Copyright (c) 2022 All rights reserved
*@description: build dataset for email and sougou
*@author: Zhixing Lu
*@date: 2022-04-21
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import os

from utils import *
from collections import defaultdict

def build_email_dataset(language,root_dir = "dataset\\email"):
    
    dataset = {}
    category_cnt = {
        'ham':0,
        'spam':0
    }
    ham_dir = os.path.join(root_dir, 'ham')
    spam_dir = os.path.join(root_dir, 'spam')
    
    ham_vocabulary = defaultdict(int)
    spam_vocabulary = defaultdict(int)
    
    # use 20 ham + 20 spam as train dataset
    # use the rest as test dataset
    for file_name in os.listdir(ham_dir)[:-5]:
        #print('processing ham file:', file_name)
        category_cnt['ham'] += 1
        words = load_text(os.path.join(ham_dir,file_name),language)
        for word in words:
            if word.startswith('http') or word.startswith('www'):
                continue
            ham_vocabulary[word]+=1
    
    for file_name in os.listdir(spam_dir)[:-5]:
        #print('processing spam file:', file_name)
        category_cnt['spam'] += 1
        words = load_text(os.path.join(spam_dir,file_name),language)
        for word in words:
            if word.startswith('http') or word.startswith('www'):
                continue
            spam_vocabulary[word]+=1
    
    dataset['ham'] = ham_vocabulary
    dataset['spam'] = spam_vocabulary
    #print(ham_vocabulary)
    #print('ham vocabulary size:',len(ham_vocabulary)) # 421
    #print('spam vocabulary size:',len(spam_vocabulary))# 264
    dataset['category_cnt'] = category_cnt
    dataset['total_cnt'] = sum(category_cnt.values())
    
    test_set = {}
    for file_name in os.listdir(ham_dir)[-5:]:
        file_name = os.path.join(ham_dir,file_name)
        test_set[file_name] = 'ham'
    for file_name in os.listdir(spam_dir)[-5:]:
        file_name = os.path.join(spam_dir,file_name)
        test_set[file_name] = 'spam'
    
    #print(test_set)
    return dataset, test_set
       

def build_sougou_dataset(language, root_dir = "dataset\\SogouC"):
    
    dataset = {}
    category_cnt = {}
    
    test_set = {}
    
    classlist_path = os.path.join(root_dir, 'ClassList.txt')
    data_path = os.path.join(root_dir,'Sample')
    with open(classlist_path,'r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            class_dir, class_name = line.strip('\n').split('\t')
            dataset[class_name] = defaultdict(int)
            category_cnt[class_name] = 0
            for file_name in os.listdir(os.path.join(data_path,class_dir))[:-1]: # use the last file as test set
                category_cnt[class_name] += 1
                words = load_text(os.path.join(data_path,class_dir,file_name),language)
                for word in words:
                    dataset[class_name][word]+=1
    
            last_file = os.listdir(os.path.join(data_path,class_dir))[-1]
            last_file = os.path.join(data_path,class_dir,last_file)
            test_set[last_file] = class_name
    
    dataset['category_cnt'] = category_cnt
    #print(category_cnt)
    dataset['total_cnt'] = sum(category_cnt.values())
    
        
    return dataset, test_set
                
