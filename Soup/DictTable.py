# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 19:56:04 2014

@author: alvin
"""

for tb1 in tables:
    typ = table_type(tb1)
    if typ in tables_by_type:
        tables_by_type[typ].append(table)
    else:
        tables_by_type[type]=table
        
        
can also be written as
because you defined
tables_by_type=defaultdict(list)

When you create a key inside the dict, it\'ll create an empty list


tables_by_type[table_type(typ)].append(tb1)


def table_type(tb1):
    ## extract table type
    return tb1('th')[1].content