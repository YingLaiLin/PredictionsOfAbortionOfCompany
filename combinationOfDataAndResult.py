import pandas as pd

result = 'train.csv'
suffix = '_with_result.csv'
prefix = 'Data/'

def combine(filename):
    df = pd.read_csv(filename+'.csv')
    df2 = pd.read_csv(result)
    pd.merge(df, df2, on='EID').to_csv(prefix + filename + suffix, sep=',', index=False)


if __name__ == '__main__':
    # filenames = ['1entbase','2alter','3branch','4invest','5right','6project','7lawsuit','8breakfaith','9recruit']
    filenames = ['2alter']
    for filename in filenames:
        combine(filename)

