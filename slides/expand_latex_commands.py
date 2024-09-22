#!/usr/bin/python

# import argparse

# parser = argparse.ArgumentParser(description = \
#   'Expand some LaTeX commands')
# parser.add_argument('string', \
#   help='The LaTeX string to expand')
# args = parser.parse_args()

import re

def sub(str):
    str = str.replace('&=&','=')
    str = str.replace('$','')
    # str = str.replace(r'\\','')
    # \newcommand{\uv}[1]{\ensuremath{\mathbf{\hat{#1}}}} % for unit vector
    str = re.sub('\\\\uv (\w)', 
                 lambda m: f'\\mathbf{{\\hat{{{m.group(1)}}}}}', str)
    str = re.sub('\\\\uv ([\\\\,\w]*)', 
                 lambda m: f'\\mathbf{{\\hat{{{m.group(1)}}}}}', str)
    str = re.sub('\\\\uv\{([\\\\,\w]*)\}', 
                 lambda m: f'\\mathbf{{\\hat{{{m.group(1)}}}}}', str)    
    # \let\vaccent=\v % rename builtin command \v{} to \vaccent{}
    str = re.sub('\\\\v ([\\\\,\w]*)', 
                 lambda m: f'\\mathbf{{{m.group(1)}}}', str)
    # \renewcommand{\d}[2]{\frac{d #1}{d #2}} % for derivatives
    # \newcommand{\dd}[2]{\frac{d^2 #1}{d #2^2}} % for double derivatives
    # \newcommand{\pd}[2]{\frac{\partial #1}{\partial #2}} % for partial derivatives
    # \newcommand{\pdd}[2]{\frac{\partial^2 #1}{\partial #2^2}} % for double partial derivatives
    frac = r"\frac"
    str = re.sub('\\\\d[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{d{m.group(1)}}}{{d{m.group(2)}}}', str)
    str = re.sub('\\\\dd[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{d^2{m.group(1)}}}{{d{m.group(2)}^2}}', str)
    str = re.sub('\\\\pd[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{\partial {m.group(1)}}}{{\partial {m.group(2)}}}', str)
    str = re.sub('\\\\pdd[\s,\{]([\\\\,\w]*)[\s,\}][\s,\{]([\\\\,\w]*)[\s,\}]', 
                 lambda m: f'{frac}{{\partial^2 {m.group(1)}}}{{\partial {m.group(2)}^2}}', str)
    # \newcommand{\bra}[1]{\left< #1 \right|} % for Dirac bras
    # \newcommand{\ket}[1]{\left| #1 \right>} % for Dirac kets
    left = r"\left"
    right = r"\right"
    str = re.sub('\\\\bra\{([\\\\,\w,\s,_,+,-]*)\}', lambda m: f'{left}<{m.group(1)}{right}|', str)
    str = re.sub('\\\\ket\{([\\\\,\w,\s,_,+,-]*)\}', lambda m: f'{left}|{m.group(1)}{right}>', str)
    return str

while True:
  str = input("Condensed string? ")
  print()
  print(sub(str))
  print()
