import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)


def job():
    a = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    pd_a = pd.DataFrame(a)
    print(pd_a.groupby(['b', 'c'])['a'])
    print(pd_a.sum(axis=1))
    print(pd_a)
    pass


def convert_grades_curve(exam_grades):
    return pd.qcut(exam_grades, [0, 0.1, 0.2, 0.5, 0.8, 1], labels=['E', 'D', 'C', 'B', 'A'])


if __name__ == '__main__':
    # job()
    print(grades_df)
    print (grades_df.apply(convert_grades_curve))
