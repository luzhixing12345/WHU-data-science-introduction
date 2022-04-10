'''
*Copyright (c) 2022 All rights reserved
*@description: Rand & kappa
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

def RandIndex(k,groups):
    
    total_count = 0
    total_true_label = 0
    
    
    for group in groups:
        label_count = [0 for _ in range(k)]
        for data in group:
            label_count[data[1]] += 1
            total_count += 1
        total_true_label+=max(label_count)
        
    return total_true_label/total_count * 100



