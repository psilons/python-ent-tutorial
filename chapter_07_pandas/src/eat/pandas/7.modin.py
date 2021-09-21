import pandas
import time

begin = time.time()
df = pandas.read_csv('IMDb names.csv')  # 125MB in size
print(df.shape)
end = time.time()
dur = end - begin
print(f'time spend = {dur}')  # 3.13249

import modin.pandas as mpd

begin = time.time()
df = mpd.read_csv('IMDb names.csv')
print(df.shape)
end = time.time()
dur = end - begin
print(f'time spend = {dur}')  # 2.114016
