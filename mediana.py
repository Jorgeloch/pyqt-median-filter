import ctypes
import numpy as np
import numpy.ctypeslib as npct # interface do numpy com ctypes

# definicao de tipos array 1d e 2d de double
# este tipo de construcao eh incomum jah que Python eh tipada dinamicamente
# mas eh necessario faze-lo pois C nao eh

array_1d_int = npct.ndpointer(dtype=np.int, ndim=1, flags='CONTIGUOUS')
# carga da biblioteca compartilhada
# primeiro argumento -> nome do arquivo (.so, .dll ou .dylib)
# segundo argumento -> path para sua localizacao
libmediana = ctypes.cdll.LoadLibrary("./libmediana.so")
# Definicao dos tipos dos argumentos e retornos da funcao
libmediana.mediana.restype = None
libmediana.mediana.argtypes = [array_1d_int, ctypes.c_int, ctypes.c_int, array_1d_int]

def mediana (matrix):
    if not isinstance (matrix,np.ndarray):
        raise TypeError ('Use: mediana (numpy.ndarray)')
    if len (matrix.shape) != 2:
        raise TypeError ('Imagem de entrada deve possuir 2 dimensoes')
    if not matrix.dtype == 'int':
        matrix = matrix.astype('int')
    rows, columns = matrix.shape
    mediana = np.zeros ((rows,columns),dtype='int')
    libmediana.mediana (matrix.ravel(), rows, columns, mediana.ravel())
    return mediana