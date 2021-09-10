import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def job(td_order, tar):
    if td_order.empty:
        print(type(td_order), '-----job------')
    if tar == None:
        print(type(tar), '-----tar------')


def job1(td_order):
    if td_order.empty:
        print(type(td_order), '-----job1------')


def run(td_order=pd.DataFrame(), tar: pd.DataFrame = None):
    job(td_order, tar)

    pass


if __name__ == '__main__':
    run()
    pass
