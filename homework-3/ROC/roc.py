'''
*Copyright (c) 2022 All rights reserved
*@description: roc curve
*@author: Zhixing Lu
*@date: 2022-04-30
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

# ROC: https://zhuanlan.zhihu.com/p/53015815

def load_data():
    
    data = [
        ['P',0.96],
        ['P',0.50],
        ['N',0.7],
        ['P',0.6],
        ['P',0.55],
        ['N',0.63],
        ['N',0.53],
        ['P',0.51],
        ['N',0.3],
        ['N',0.4]
    ]
    return data

def draw_roc(data):
        
    # calculate the true positive rate and false positive rate
    tpr = []
    fpr = []
    
    for rate in range(1,100):
        rate = rate / 100
        tp = 0
        fp = 0
        fn = 0
        tn = 0
        for i in range(len(data)):
            if data[i][1] >= rate:
                if data[i][0] == 'P':
                    tp += 1
                else:
                    fp += 1
            else:
                if data[i][0] == 'P':
                    fn += 1
                else:
                    tn += 1
        tpr.append(tp / (tp + fn))
        fpr.append(fp / (fp + tn))

    roc_curve = []
    for i in range(len(tpr)):
        roc_curve.append([fpr[i],tpr[i]])
    # draw the roc curve
    draw_tree(roc_curve)


def draw_tree(roc_curve):
    
    import numpy as np
    roc_curve = np.array(roc_curve)
    # draw the roc curve
    import matplotlib.pyplot as plt
    plt.plot(roc_curve[:,0],roc_curve[:,1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.savefig('roc.png')
    plt.show()


def main():
    
    data = load_data()
    draw_roc(data)




if __name__ == '__main__':
    main()

