#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import torch
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors

# from utility import *

FF_maps = torch.load('D:/map1.pth')
FB_maps = torch.load('D:/map1.pth')

assert len(FF_maps) == len(FB_maps), "len(FF_maps) ~= len(FB_maps)"
map_len = len(FF_maps)

fig, axs = plt.subplots(nrows=2, ncols=map_len)

images_FF = []
images_FB = []

for time_step in range(map_len):
    FF_map = FF_maps[time_step].squeeze().cpu().numpy()
    FB_map = FB_maps[time_step].squeeze().cpu().numpy()

    FF_map_avg = np.mean(FF_map, axis=0)
    FB_map_avg = np.mean(FB_map, axis=0)

    # images_FF.append(axs[0, time_step].imshow(FF_map_avg, cmap='hot'))
    # images_FB.append(axs[1, time_step].imshow(FB_map_avg, cmap='hot'))

    images_FF.append(axs[0].imshow(FF_map_avg))
    images_FB.append(axs[1].imshow(FB_map_avg))

    axs[0 ].axis('off')
    axs[1].axis('off')
    axs[0].set(title=r'$t=%d$'%(time_step+1))
    axs[1].set(title=r'$t=%d$'%(time_step+1))

    vmin_FF = min(image.get_array().min() for image in images_FF)
    vmax_FF = max(image.get_array().max() for image in images_FF)

    vmin_FB = min(image.get_array().min() for image in images_FB)
    vmax_FB = max(image.get_array().max() for image in images_FB)

    norm_FF = colors.Normalize(vmin=vmin_FF, vmax=vmax_FF)
    norm_FB = colors.Normalize(vmin=vmin_FB, vmax=vmax_FB)

    for im_ff, im_fb in zip(images_FF, images_FB):
        im_ff.set_norm(norm_FF)
        im_fb.set_norm(norm_FB)

plt.subplots_adjust(hspace = 0.02)
fig.colorbar(images_FF[0], ax=axs[0], orientation='vertical', shrink=0.72)
fig.colorbar(images_FB[0], ax=axs[1], orientation='vertical', shrink=0.72)
plt.show()
