#CSVから読み込んでグラフを作成する
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample.csv', names=['num1', 'num2'])
plt.plot(range(0,92),df['num2'],marker="o")
#plt.subplots_adjust(wspace = 1.0, hspace = 1.0)
plt.show()
