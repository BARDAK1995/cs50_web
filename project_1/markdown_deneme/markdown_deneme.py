# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:24:28 2022

@author: merts
"""

import markdown2
from markdown2 import markdown

with open('CSS.md', 'r') as f:
    text = f.read()
    html = markdown(text)

with open('Picnic.html', 'w') as f:
    f.write(html)
    