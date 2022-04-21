'''
*Copyright (c) 2022 All rights reserved
*@description: some utils function for naive bayes classifier
*@author: Zhixing Lu
*@date: 2022-04-21
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

# basic stop word set
stop_word_set = [',','.',':',';','(',')','[',']',
                     '{','}','<','>','/','\\','|','?'
                     ,'!','@','#','$','%','^','&','*',
                     '~','`','+','=','_','-','\n','\t','\r']

# chinese stop word set
stop_word_dir = 'dataset\\SogouC\\stopwords_cn.txt'
with open(stop_word_dir,'r',encoding='utf-8',errors='ignore') as f:
    stop_word_set_cn = f.read().split('\n')

def delete_stop_word(word,type='cn'):
    
    for stop_word in stop_word_set_cn:
        word = word.replace(stop_word,'')
    for number in ['0','1','2','3','4','5','6','7','8','9']:
        word = word.replace(number,'')
   
    
    # delete the english character in chinese text
    if type == 'cn':
        for i in range(26):
            word = word.replace(chr(ord('a')+i),'')
            word = word.replace(chr(ord('A')+i),'')
        word = word.replace(' ','')
        # remove chinese character
        for c in ['。','，','：','；','（','）','【','】',
              '{','}','<','>','/','\\','|','？','！',
              '@','#','$','%','^','&','*','~','`','+','=','_','-','、']:
            word = word.replace(c,'')
        
    return word

def load_text(file_path,file_type='en',total = False):

    with open(file_path,'r',encoding='utf-8',errors='ignore') as f:
        if total:
            return f.read()
        content = f.read().replace(' ','')
        
    return delete_stop_word(content,file_type)