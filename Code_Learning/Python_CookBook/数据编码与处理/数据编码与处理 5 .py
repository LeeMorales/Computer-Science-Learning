from struct import Struct
from collections import namedtuple


def write_records(records, format, f):
    """
    Write a sequence of tuples to a binary file of structures.
    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)
from struct import Struct
def read_records(format, f):
        record_struct = Struct(format)
        chunks = iter(lambda: f.read(record_struct.size), b'')
        return (record_struct.unpack(chunk) for chunk in chunks)
    
        with open('data.b','rb') as f:
            for rec in read_records('<idd', f):
            # Process rec
                pass
from struct import Struct
def unpack_records(format, data):
        record_struct = Struct(format)
        return (record_struct.unpack_from(data, offset)
                for offset in range(0, len(data), record_struct.size))

        with open('data.b', 'rb') as f:
            data = f.read()
        for rec in unpack_records('<idd', data):
           # Process rec
            pass
polys = [ [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
          [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
          [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ], ]  
import struct 
import itertools 
def write_polys(filename, polys): 
    # Determine bounding box 
    flattened = list(itertools.chain(*polys)) 
    min_x = min(x for x, y in flattened) 
    max_x = max(x for x, y in flattened) 
    min_y = min(y for x, y in flattened) 
    max_y = max(y for x, y in flattened) 
    with open(filename, 'wb') as f: 
        f.write(struct.pack('<iddddi', 0x1234, 
                            min_x, min_y, 
                            max_x, max_y, 
                            len(polys))) 
        for poly in polys: 
            size = len(poly) * struct.calcsize('<dd') 
            f.write(struct.pack('<i', size + 4)) 
            for pt in poly: 
                f.write(struct.pack('<dd', *pt))
                def read_polys(filename): 
                    with open(filename, 'rb') as f: 
                        # Read the header 
                        header = f.read(40) 
                        file_code, min_x, min_y, max_x, max_y, num_polys = \
                        struct.unpack('<iddddi', header) 
                        polys = [] 
                        for n in range(num_polys): 
                            pbytes, = struct.unpack('<i', f.read(4)) 
                        poly = [] 
                        for m in range(pbytes // 16): 
                            pt = struct.unpack('<dd', f.read(16)) 
                            poly.append(pt) 
                        polys.append(poly)  
                return polys 
import struct 
class StructField: 
    '''    
    Descriptor representing a simple structure field     
    ''' 
    def __init__(self, format, offset): 
        self.format = format 
        self.offset = offset 
    def __get__(self, instance, cls): 
        if instance is None: 
            return self 
        else: 
            r = struct.unpack_from(self.format, instance._buffer, self.offset) 
            return r[0] if len(r) == 1 else r 
class Structure: 
    def __init__(self, bytedata): 
        self._buffer = memoryview(bytedata) 
        class PolyHeader(Structure): 
            file_code = StructField('<i', 0) 
            min_x = StructField('<d', 4) 
            min_y = StructField('<d', 12) 
            max_x = StructField('<d', 20) 
            max_y = StructField('<d', 28) 
            num_polys = StructField('<i', 36) 