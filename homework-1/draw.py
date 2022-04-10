'''
*Copyright (c) 2022 All rights reserved
*@description: draw the tree by Graphviz
*@author: Zhixing Lu
*@date: 2022-04-08
*@email: luzhixing12345@163.com
*@Github: luzhixing12345
'''

import textwrap
import os


def draw_tree(data,indexes, name):
    
    dot_header = [textwrap.dedent("""\
        digraph astgraph {
          node [shape=circle, fontsize=12, fontname="Courier", height=.1];
          ranksep=.3;
          edge [arrowsize=.5]
        """)]
    dot_body = build_tree(data,indexes)
    dot_footer = ['}']
    # return
    dot_file = open(name+'.dot', 'w',encoding='utf-8')
    dot_file.write(''.join(dot_header+dot_body+dot_footer))
    print('successfully write to file')
    dot_file.close()
    
    os.system(f"dot -Tpng -o images/{name}.png {name}.dot")
    print(f'successfully draw the tree in images/{name}.png')
    

def build_tree(data,indexes):
    
    dot_body = ""
    values = list(indexes.values())
    income_shreshold ,values[2] = values[2][0],values[2][1]
    keys = list(indexes.keys())


    node_id = 1
    while len(values)!=0:
        min_value = min(values)
        index = values.index(min_value)
        if keys[index]=='income':
            keys[index]+=f'<{income_shreshold}'
        
        dot_body+=f"  node{node_id} [label=\"{keys[index]}\"]\n"
        dot_body+=f"  node{node_id+1} [label=\"{keys[index]}\"]\n"
        dot_body+=f"  node{node_id+3} [label=\"not {keys[index]}\"]\n"
        dot_body+=f"  node{node_id} -> node{node_id+3} [label= \"no\"]\n"
        dot_body+=f"  node{node_id} -> node{node_id+1} [label= \"yes\"]\n"
        dot_body+=f"  node{node_id+2} [label=\"borrow\"]\n"
        dot_body+=f'  node{node_id+1} -> node{node_id+2} \n'
    
        node_id+=3
        values.remove(min_value)
        keys.remove(keys[index])
        
    dot_body+=f' node{node_id+1} [label="not borrow"]\n'
    dot_body+=f' node{node_id} -> node{node_id+1} [label= "yes"]\n'
    return [dot_body]

    
    
