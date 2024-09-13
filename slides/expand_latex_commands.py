#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description = \
  'Expand some LaTeX commands')
parser.add_argument('string', \
  help='The LaTeX string to expand')
args = parser.parse_args()

import re

def sub(str):
    str = str.replace('&=&','=')
    str = str.replace(r'\\','')
    str = re.sub('\\\\uv ([\\\\,\w]*)', 
                 lambda m: f'\\mathbf{{\\hat{{{m.group(1)}}}}}', str)
    frac = r"\frac"
    str = re.sub('\\\\d[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{d{m.group(1)}}}{{d{m.group(2)}}}', str)
    str = re.sub('\\\\dd[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{d^2{m.group(1)}}}{{d{m.group(2)}^2}}', str)
    str = re.sub('\\\\pd[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{\partial {m.group(1)}}}{{\partial {m.group(2)}}}', str)
    str = re.sub('\\\\pdd[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{\partial^2 {m.group(1)}}}{{\partial {m.group(2)}^2}}', str)        
    print(str)
#    return str

sub(args.string)