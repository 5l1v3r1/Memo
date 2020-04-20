#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import OrderedDict


class Memo:
    def __init__(self, size=None):
        self.size = size
        self.l = list()
        self.cache = OrderedDict()

    def __call__(self, f):
        def func(*arg):
            if arg not in self.cache:
                self.cache[arg] = f(*arg)
                self.l.append(self.cache[arg])
                if self.size is not None and len(self.cache) > self.size:
                    x = self.cache.popitem(last=False)
            print(f"Cache: {self.l}")
            return self.cache[arg]
        return func

