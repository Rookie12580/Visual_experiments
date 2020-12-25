import matplotlib.pyplot as plt
#from collection import Or


srcnn = [0.020, 30.48]
fsrcnn = [0.015, 30.71]
vdsr = [0.054, 31.45]
drcn = [0.735, 31.53]
lapsrn = [0.040, 31.54]
drrn = [4.450, 31.68]
idn = [0.0076, 31.82]
GIDNL = [0.0094,32.04]
GIDN = [0.0135,32.15]

method = {'SRCNN (57K)':srcnn, 'FSRCNN (12K)':fsrcnn, 'VDSR (665K)':vdsr, 'DRCN (1,774K)':drcn, 'DRRN (677K)':drrn, 'LapSRN (815K)':lapsrn, 'IDN (1,445K)':idn, 'GIDN (1,097K)':GIDN,'GIDNL (1,097K)':GIDNL}


speed = []
psnr = []
name = []
color = []

for item in method:
    speed.append(method[item][0])
    psnr.append(method[item][1])
    name.append(item)
    if item.find('DRRDN')>=0:
        color.append('r')
    else:
        color.append('b')

print(name)

fig, ax = plt.subplots(figsize=(10.5, 6))
#fig.figure(figsize=(12,5))
ax.scatter(speed, psnr, s=60, c=color)
ax.set_xlabel('Slow                       Running time (s)                       Fast', fontname='Times New Roman', fontsize=25)
ax.set_ylabel('PSNR (dB)', fontname='Times New Roman', fontsize=25)
#ax.annotate('1000',xy=(1000,30.2),color="g",size=19, fontname='Times New Roman')
ax.set_xscale('log')

labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontsize(25) for label in labels]
[label.set_fontname('Times New Roman') for label in labels]

diff = ((0,0.05),(0,0.05),(0,-0.15),(0,0.05),(0,0.05),(0,0.05),(0,-0.15),(0,-0.15),(0,0.05))#,(0,0.05)#,(0,0.05),(200,-0.10))
#ax.vlines(1000, 30, 33, color='g', linestyles='dashed')

#ax.set_xticklabels([i for i in ax.get_xticklabels()], fontsize=13)
#ax.set_yticklabels([i for i in ax.get_yticklabels()], fontsize=13)
for i,j in enumerate(name):
    (x, y) = (speed[i], psnr[i])
    #(dd, dl, r, dr, dp) = dash_style[i]
    (dx,dy) = diff[i]
    if (j == 'DRRDN'): #or (j=='DRRN'):
        t = ax.text(x+dx, y+dy, j, color=color[i], fontsize=25, fontname='Times New Roman')
    else:
        t = ax.text(x+dx, y+dy, j, color=color[i], fontsize=24, fontname='Times New Roman')

#ax.set_xticklabels(["0","5000","10000","15000","20000","25000","...","40000","45000"])

ax.grid(True, linestyle='-',linewidth=1)
ax.xaxis.grid(True, which='minor', linestyle='dotted',linewidth=1)
ax.yaxis.grid(True, linestyle='dotted',linewidth=1)


#plt.xlim([10,0.0008])
plt.ylim([30,32.5])
plt.gca().invert_xaxis()
plt.show()
fig.savefig('speed.pdf')

