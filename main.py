import pandas as pd
import scipy.io as sio
if __name__ == '__main__':
    mat = sio.loadmat('embedding.mat')
    print(mat['embedding'][0][0])