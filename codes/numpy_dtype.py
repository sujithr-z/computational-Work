class numpy_dtype:

    TYPE_MAP = {
        'float16' : ('f',2,float), # kind, itemsize, type
        'float32' : ('f',4,float),
        'float64' : ('f',8,float),
        'int8': ('i',1,int),
        'int16': ('i',2,int),
        'int32': ('i',4,int),   
        'int64': ('i',8,int),
        'uint8': ('u',1,int),
        'uint16': ('u',2,int),
        'uint32': ('u',4,int),
        'uint64': ('u',8,int),
        'bool': ('b',1,bool),
        'complex64': ('c',8,complex),
        'complex128': ('c',16,complex)
    }


    def __init__(self, dtype):
        self.dtype = dtype
        if dtype not in self.TYPE_MAP:
            raise ValueError(f"Unsupported dtype: {dtype}")
        self.kind, self.itemsize, self.type = self.TYPE_MAP[dtype]

    def __repr__(self):
        return f"numpy_dtype(dtype='{self.dtype}', kind='{self.kind}', itemsize={self.itemsize}, type={self.type.__name__})"
        
if __name__ == "__main__":
    dtype_info = numpy_dtype('int32')
    print(dtype_info)