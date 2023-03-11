import ctypes
import numpy as np
import numpy.ctypeslib as npct # interface do numpy com ctypes

array_1d_uint8 = npct.ndpointer(dtype="uint8", ndim=1, flags='CONTIGUOUS')

libmediana = ctypes.cdll.LoadLibrary("./libmediana.so")
# Definicao dos tipos dos argumentos e retornos da funcao
libmediana.mediana.restype = None
libmediana.mediana.argtypes = [array_1d_uint8, ctypes.c_int, ctypes.c_int, array_1d_uint8]

def mediana (matrix):
    if not isinstance (matrix,np.ndarray):
        raise TypeError ('Use: mediana (numpy.ndarray)')
    if len (matrix.shape) != 2:
        raise TypeError ('Imagem de entrada deve possuir 2 dimensoes')
    if not matrix.dtype == 'uint8':
        matrix = matrix.astype('uint8')
    rows, columns = matrix.shape
    mediana = np.zeros ((rows,columns),dtype='uint8')
    libmediana.mediana (matrix.ravel(), rows, columns, mediana.ravel())
    return mediana