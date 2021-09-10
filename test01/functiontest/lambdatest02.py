import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4, 3), columns=list('abc'), index=['utah', 'ohio', 'texas', 'oregon'])


def apply_test01():
    f = lambda x: x.max() - x.min()
    t1 = df.apply(f)
    print(t1)
    t2 = df.apply(f, axis=1)
    print(t2)


def apply_test02(x):
    pass


if __name__ == '__main__':
    print(df)
    apply_test01()
