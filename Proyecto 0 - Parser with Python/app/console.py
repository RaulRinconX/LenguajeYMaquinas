import re

txt = ' putCB(c, b)'# { drop(c);  free(b);  walk(n);  }'

def p_program(txt):
    '''program : statement_list'''
    x = re.findall(".+(.+)", txt)
    print(x)

p_program(txt)