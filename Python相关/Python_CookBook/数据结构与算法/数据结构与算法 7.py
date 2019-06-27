print("数据结构与算法7")
import os
def trans_reduce():
    def path():
        nums = [1, 2, 3, 4, 5]
        s = sum(x * x for x in nums)
        print(s)
        files = os.listdir(path)
        if any(name.endswith('.py') for name in files):
            print('There be python!')
        else:
            print('Sorry, no python.')
        # Output a tuple as CSV
        s = ('ACME', 50, 123.45)
        print(','.join(str(x) for x in s))
        # Data reduction across fields of a data structure
        portfolio = [
            {'name':'GOOG', 'shares': 50},
            {'name':'YHOO', 'shares': 75},
            {'name':'AOL', 'shares': 20},
            {'name':'SCOX', 'shares': 65}
        ]
        min_shares = min(s['shares'] for s in portfolio)

        # Original: Returns 20
        min_shares = min(s['shares'] for s in portfolio)
        # Alternative: Returns {'name': 'AOL', 'shares': 20}
        min_shares = min(portfolio, key=lambda s: s['shares'])
    if __name__ == '__main__':
        trans_reduce()
    from collections import ChainMap


    def combine_map():
        a = {'x': 1, 'z': 3 }
        b = {'y': 2, 'z': 4 }
        c = ChainMap(a,b)
        print(c['x']) # Outputs 1 (from a)
        print(c['y']) # Outputs 2 (from b)
        print(c['z']) # Outputs 3 (from a)

        print(len(c))
        print(list(c.keys()))
        print(list(c.values()))

        c['z'] = 10
        c['w'] = 40
        del c['x']
        print(a)
        # del c['y']

        values = ChainMap()
        values['x'] = 1
        # Add a new mapping
        values = values.new_child()
        values['x'] = 2
        values['x'] = 3
        print(values)
        print(values['x'])
        print(values)


    if __name__ == '__main__':
        combine_map()