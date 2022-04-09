'''
*Copyright (c) 2022 All rights reserved
*@description: configuration file 
*@author: Zhixing Lu
*@date: 2022-03-28
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''


import yaml

def ReadConfigFile(file_name = 'config.yaml'):
    '''
    open config.yaml and return configuration
    '''
    file = open(file_name, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data,Loader=yaml.FullLoader)
    return data

def WriteConfigFile(data,file_name = 'config.yaml'):
    file = open(file_name,'w',encoding='utf-8')
    yaml.dump(data,file)
    file.close()
    
