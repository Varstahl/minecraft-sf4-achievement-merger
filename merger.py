#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from codecs import open as co

FN1 = 'old.json'  # Oldest UUID achievement JSON file
FN2 = 'new.json'  # Newest UUID achievement JSON file
FNOUT = 'merged.json'  # Output


# Hic sunt dracones ###################
# There be dragons ####################

def Merge(o, n):
    for k in n.keys():
        if k not in o:
            o[k] = n[k]
        elif isinstance(n[k], dict):
            Merge(o[k], n[k])
        else:  # String/bool
            if 'done' == k:  # Bool
                o[k] = o[k] or n[k]
            # Strings are timestamps, so we keep the oldest

with co(FN1, 'r', 'utf-8') as f:
    data = json.load(f)

with co(FN2, 'r', 'utf-8') as f:
    Merge(data, json.load(f))

with co(FNOUT, 'w+', 'utf-8') as f:
    json.dump(data, f, indent=2, sort_keys=True)
