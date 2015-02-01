# -*- coding: utf-8 -*-
"""
Created on Sun Feb 01 15:51:59 2015

@author: WalkerLin
"""

import ystockquote as yq 

"""
查看国内沪深股市的股票，规则是：沪股代码末尾加.ss，深股代码末尾加.sz
"""
quo_price = yq.get_change('600887.SS')
print quo_price

quo_price = yq.get_historical_prices('600887.SS','2015-01-30','2015-02-01')
print quo_price
