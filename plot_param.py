import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import pandas as pd
from matplotlib.pyplot import MultipleLocator
from matplotlib.ticker import FuncFormatter   ### 今天的主角
import numpy as np
sns.set_style('whitegrid')    ###可以设置白色网格风格使图形更漂亮

fig, ax = plt.subplots(figsize=(10, 6), sharey=True)
t = np.arange(0, 20, 4.5)
# ax.semilogx(t, np.exp(-t / 10.0))
plt.ylabel('PSNR(dB)')
plt.xlabel('Number of Parameters(10M)')




para = { 'FSRCNN': 0.001,'SRCNN': 0.006,'VDSR': 0.067, 'DRCN': 0.177, 'MSRN': 0.593, 'DBPN': 1, 'EDSR': 4.3,'DRRN': 0.03, 'Memmet': 0.068,'LapSRN': 0.081,'WRFN':0.31}
psnr = {'FSRCNN': 37,'SRCNN': 36.66,'VDSR': 37.53, 'DRCN': 37.63, 'MSRN': 38.07, 'DBPN': 38.09, 'EDSR': 38.11,'DRRN': 37.74, 'Memmet': 37.78, 'LapSRN': 37.52, 'WRFN': 38.16}
txt = ['FSRCNN','SRCNN','VDSR', 'DRCN', 'MSRN', 'DBPN', 'EDSR','DRRN', 'Memmet','LapSRN' ,'WRFN']
names = list(para.keys())
rt = list(para.values())
pr = list(psnr.values())



plt.grid(True,which="both",ls="-.")
ax.set_xlim([0,4.5])
ax.set_ylim([36.5,38.5])
# def formatnum(x, pos):
#     return '$10^{-}$' % (x/10000)
# formatter = FuncFormatter(formatnum)
# ax.xaxis.set_major_formatter(formatter)
# ax.axvline(x=1, color='#afafb5',linewidth=0.5)
# ax.axvline(x=0.1,color='#afafb5', linewidth=0.5);

# for i in txt:
#     ax.scatter(rt[i],pr[i],c='b')
ax.scatter(rt[0], pr[0],c='b',clip_on=False)
ax.scatter(rt[1], pr[1],c='b',clip_on=False)
ax.scatter(rt[2], pr[2],c='b')
ax.scatter(rt[3], pr[3],c='b')
ax.scatter(rt[4], pr[4],c='b')
ax.scatter(rt[5], pr[5],c='b')
ax.scatter(rt[6], pr[6],c='b')
ax.scatter(rt[7], pr[7],c='b')
ax.scatter(rt[8], pr[8],c='b')
ax.scatter(rt[9], pr[9],c='b')
ax.scatter(rt[10], pr[10],c='r')

for i in range(len(rt)):
    if i<=6:
        plt.annotate(txt[i], xy = (rt[i], pr[i]), xytext = (rt[i]+0.03, pr[i]+0.03), weight='light')
    if i==7:
        plt.annotate(txt[i], xy=(rt[i], pr[i]), xytext=(rt[i] + 0.05, pr[i] ), weight='light')#DRRN
    if i==8:
        plt.annotate(txt[i], xy=(rt[i], pr[i]), xytext=(rt[i] + 0.03, pr[i] + 0.06), weight='light')
    if i==9:
        plt.annotate(txt[i], xy=(rt[i], pr[i]), xytext=(rt[i] + 0.03, pr[i] - 0.06), weight='light')
    if i==10:
        plt.annotate(txt[i], xy=(rt[i], pr[i]), xytext=(rt[i] + 0.03, pr[i] + 0.03), weight='light')
fig.tight_layout()
plt.show()


