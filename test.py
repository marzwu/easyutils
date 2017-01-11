import tushare as ts
import numpy as np

hist = ts.get_stock_basics()
print(list(hist.index))
