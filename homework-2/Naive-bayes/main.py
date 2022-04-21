'''
*Copyright (c) 2022 All rights reserved
*@description: naive bayes classifier
*@author: Zhixing Lu
*@date: 2022-04-21
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import argparse
from time import sleep
import math
from dataset import *

def main(args):
    
    LANGUAGE = 'en'
    
    if args.email:
        LANGUAGE = 'en'
        print('naive bayes classifier for email in english')
        # dataset construction:
        # ham_vocabulary, spam_vocabulary, test_set = build_email_dataset()
        dataset,test_set = build_email_dataset(language=LANGUAGE)
    elif args.sougou:
        LANGUAGE = 'cn'
        print('naive bayes classifier for sougou in chinese')
        dataset,test_set = build_sougou_dataset(language=LANGUAGE)
        
    else :
        print('please specify the dataset')
        return

    # test
    total = 0
    correct = 0

    for file_path in test_set:
        words = load_text(file_path,LANGUAGE,total=True)
        
        # print split line
        print('-'*50)
        print(words)
        print('-'*50)
        true_label = test_set[file_path]
        naive_bayes_label = calculate_naive_bayes(dataset,load_text(file_path,LANGUAGE))
        print('true label:',true_label)
        print('naive bayes label:',naive_bayes_label)
        if naive_bayes_label == true_label:
            correct += 1
        total += 1

    print(f'accuracy: {100*correct/total} %')



def calculate_naive_bayes(dataset,words):

    possibility = {}
    for class_name,category_cnt in dataset['category_cnt'].items():
        possibility[class_name] = math.log(category_cnt/dataset['total_cnt'])
    
    #print(possibility)
    
    class_names = dataset['category_cnt'].keys()
    
    for word in words:
        for class_name in class_names:
            total_word_number = sum(dataset[class_name].values())
            # print('total word number:',total_word_number)
            # print(word)
            # exit(0)
            if word in dataset[class_name].keys():
                #print("find word:",word)
                possibility[class_name] += math.log((dataset[class_name][word]+1)/(total_word_number+len(dataset[class_name])))
                #print('possibility:',possibility)
                #sleep(3)
            else:
                possibility[class_name] += math.log(1/(total_word_number+len(dataset[class_name])+1))
    
    #possibility = np.softmax(possibility)
    print(possibility)
    label = max(possibility,key=possibility.get)
    return label


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email',action='store_true')
    parser.add_argument('--sougou',action='store_true')
    args = parser.parse_args()
    main(args)