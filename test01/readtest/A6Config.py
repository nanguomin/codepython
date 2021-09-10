import os
from enum import Enum
from collections import defaultdict

# 有保证金的市场

FUTUREMARKET = ['Z', 'D', 'H', 'F', 'I']
#
FUTURE_ENDS = ('CFE', 'CZC', 'SHF', 'DCE', 'INE')
# LS 多头/空投 direction
LONG = ['B']
SHORT = ['S']

# 固定参数
instrsno_modi = 0
serverid = 1


# tuple and bs_flag
def get_bsFlag(BS: int, LS: int, stkCode: str, market: str = '0'):
    """
    仅支持 股票和期货
    ai数据库中 BS与LS组成的组合与A6 bs_flag的映射关系
    '0B': '证券买入', '0S': '证券卖出', '1U': '买入开仓/多头开仓', '1V': '卖出平仓/多头平仓',
    '1W': '卖出开仓/空头开仓', '1X': '买入平仓/空头平仓', '0Q': "逆回购"
    """
    future = {
        (1, 1): '1U',
        (1, -1): '1W',
        (-1, 1): '1V',
        (-1, -1): '1X'

    }
    Ashare = {
        (1, 1): '0B',
        (-1, 1): '0S'
    }

    reverse_codes = ['204001', '131810']

    if stkCode in reverse_codes:
        return '0Q'
    if market in FUTUREMARKET:
        return future[(BS, LS)]
    else:
        return Ashare[(BS, LS)]


# a6 bs_flag to ai BS/LS
bsFlag2tuple = {
    '1U': (1, 1),
    '1W': (1, -1),
    '1V': (-1, 1),
    '1X': (-1, -1),
    '0B': (1, 1),
    '0S': (-1, 1),
    '0Q': (1, 1)
}


# windcodeends to ends

class windcodeEndsToMarket(Enum):
    """
    万得代码的后缀与a6系统中市场代码的映射关系
        '1': 'SH', '0': 'SZ', '8': 'GG', '9': 'TBZR', 'A': 'YHJ', 'Z': 'CZC', 'D': 'DCE', 'H': 'SHF',
        'F': 'CFE', 'G': 'SG', 'W': 'CW', 'I': 'INE'
    """
    SH = '1'  # 深A
    SZ = '0'  # 沪A
    GG = '8'  # 沪港通
    CZC = 'Z'  # 郑商所
    DCE = 'D'  # 大商所
    SHF = 'H'  # 上期所
    CFE = 'F'  # 中金所
    SG = 'G'  # 深港通
    YHJ = 'A'  # 银行间
    CW = 'W'  # 场外
    INE = 'I'  # 上海国际能源交易中心
    TBZR = '9'  # 特别转让


AShare_exp = '.*(SH|SZ)$'
Afuture_exp = '.*(CFE|SHF|DCE|CZC|INE)$'

acctType2CodeEnds = {
    'CASH': AShare_exp,
    'FUTURE': Afuture_exp
}

BS2str = {
    1: 'BUY',
    -1: 'SELL'
}

# A6系统字段名对应的字段类型
trans_data_type = defaultdict(lambda: 'str')
trans_data_type.update({
    'openprice': 'float',
    'upperlimitprice': 'float',
    'lowerlimitprice': 'float',
    'settleprice': 'float',
    'closeprice': 'float',
    'matchamt': 'float',
    'matchqty': 'float',
    'lastprice': 'float',
    'avgprice': 'float',
    'highprice': 'float',
    'lowprice': 'float',
})

# A6系统中算法代号
algo_id = {
    'AITWAP3': 32,
    'QMOC3': 38,
    'AITWAP': 39
}
# 算法可传参数
algo_param_names = {
    32: ['beginTime', 'endTime', 'participateRate', 'tradingStyle', 'minOrderAmt'],  # AITWAP3
    38: ['beginTime', 'tradingStyle', 'mocPartRate', 'prePartRate'],  # QMOC3
    39: ['beginTime', 'endTime', 'aggressiveLevel', 'maxOpenOrderQty', 'maxRate',
         'minCloseOrderQty', 'minAmount']  # AITWAP
}

# 算法参数默认值
algo_param_default_value = {
    'maxOpenOrderQty': 0,
    'minCloseOrderQty': 0,
    'minAmount': 0
}

GC001 = '204001.SH'
R001 = '131810.SZ'
if os.name == 'posix':
    # linux
    local_hardwareinfo_path = os.path.join(os.environ["HOME"], "hardware-a6")
elif os.name == 'nt':
    # windows
    local_hardwareinfo_path = "d:\\hardware-a6.txt"
else:
    raise Exception("not support os type!")
cloud_hardwareinfo_path = "/mnt/hardwareinfo/hardware-a6"

# 交易时间段

A_stock = dict(
    morning_open='093000',
    morning_close='113000',
    afternoon_open='130000',
    afternoon_close='150000')

F_stock = dict(
    morning_open='090000',
    rest_start='101500',
    rest_end='103000',
    morning_close='113000',
    afternoon_open='133001',
    afternoon_close='150000')

HK_stock = dict(
    morning_open='093000',
    morning_close='120000',
    afternoon_open='130000',
    afternoon_close='160000')

A_markets = ['0', '1', 'F']
HK_markets = ['8', 'G']
F_markets = ['Z', 'D', 'I', 'H']

