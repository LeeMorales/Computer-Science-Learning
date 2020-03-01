#!/usr/bin/env python
# coding: utf-8

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python

import pandas as pd
import numpy as np
import math as m

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


import pandas as pd
filename = "/Users/leemiles/Computer-Science-Learning/Python_CSV_to_xls/1.csv"
data = pd.read_csv(filename, header = 9)

data.head(20)

data.drop(["Date"],axis = 1)

Mean=[data['Mkt-RF'].mean(),data['SMB'].mean(),data['HML'].mean(),data['RMW'].mean(),data['CMA'].mean(),data['RF'].mean(),data['MOM'].mean()]
SD=[np.std(data['Mkt-RF']),np.std(data['SMB']),np.std(data['HML']),np.std(data['RMW']),np.std(data['CMA']),np.std(data['RF']),np.std(data['MOM'])]

tstat1=Mean[0]* m.sqrt(678)/SD[0]; tstat2=Mean[1]* m.sqrt(678)/SD[1]; tstat3= Mean[2]* m.sqrt(678)/SD[2];tstat4=Mean[3]* m.sqrt(678)/SD[3];
tstat5=Mean[4]* m.sqrt(678)/SD[4];tstat6=Mean[5]* m.sqrt(678)/SD[5];tstat7=Mean[6]* m.sqrt(678)/SD[6]

data={'':['Mean','SD','t-statistic'],
      'RM-RF':[Mean[0],SD[0],tstat1],
      'SMB':[Mean[1],SD[1],tstat2],
      'HML':[Mean[2],SD[2],tstat3],
      'RMW':[Mean[3],SD[3],tstat4],
      'CMA':[Mean[4],SD[4],tstat5],
      'RF':[Mean[5],SD[5],tstat6],
      'MOM':[Mean[6],SD[6],tstat7]}


pd.DataFrame(data).to_excel('output.xlsx', header=False, index=False)

filename1 = "/Users/leemiles/Computer-Science-Learning/Python_CSV_to_xls/1.csv"
with open(filename1) as fd:
    reader=pd.read_csv(fd)
    interestingrows=[row for idx, row in enumerate(reader) if idx in (16,1379)]

filename1 = "/Users/leemiles/Computer-Science-Learning/Python_CSV_to_xls/1.csv"
with open(filename1) as fd:
    reader=pd.read_csv(fd)
def read(self, nrows=1400):
    data1 = self._reader.read(nrows)
    data1.head(8)

