class Bin ():
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        return 'Bin(sum=%s, items=%s)' % (self.sum, str(self.items))


def pack(vals, maxVal):
    """An implmentation of the first fit decreasing bin packing algorithm"""
    items = sorted(vals, reverse=True)
    bins = []
    for item in items:
        for bin in bins:
            if bin.sum + item <= maxVal:
                bin.append(item)
                break
        else:
            bin = Bin()
            bin.append(item)
            bins.append(bin)
    return bins


def packAndGenSolution(list, maxVal):
    print('An list with sum %s with max bin value of %s need a minimum of %s bins') % (
        sum(list), maxVal, (sum(list)/maxVal))
    bins = pack(list, maxVal)
    print('%s bins were needed') % format(len(bins))
    for bin in bins:
        print(bin)


packAndGenSolution([8, 7, 14, 9, 6, 9, 5, 15, 6, 7, 8], 20)
