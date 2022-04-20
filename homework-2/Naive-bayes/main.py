'''
*Copyright (c) 2022 All rights reserved
*@description: naive bayes classifier
*@author: Zhixing Lu
*@date: 2022-04-20
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import argparse
from dataset import build_email_dataset,build_example_dataset


def main(args):
    
    if args.email:
        training_set, test_set = build_email_dataset()
    else:
        training_set, test_set = build_example_dataset()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', action="store_true", help='output file')
    args = parser.parse_args()
    main(args)