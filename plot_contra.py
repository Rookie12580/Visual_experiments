import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Plot Logs')
    parser.add_argument('-path1', type=str, required=True, help="Path to '.csv' file.")
    parser.add_argument('-path2', type=str, required=True, help="Path to '.csv' file.")

    df1 = pd.read_csv(parser.parse_args().path1,nrows=400)
    df2 = pd.read_csv(parser.parse_args().path2,nrows=400)

    epoch = df1['epoch']
    # train_loss = df['train_loss']
    # val_loss = df['val_loss']
    psnr1 = df1['psnr']
    psnr2 = df2['psnr']
    x = np.linspace(0, 400,400)
    psnr3 = 0*x+31.35
    # ssim = df['ssim']

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(epoch, psnr1, 'r',lw = 1,label='WRFN_with_WFIB')
    ax.plot(epoch, psnr2, 'g',lw = 1,label='WRFN_with_WDSR-b')
    ax.plot(epoch, psnr3, '--b',lw = 1,label='VDSR')
    # plt.plot(epoch, psnr1, epoch, psnr2, epoch, psnr3, '--')

    ax.set(xlabel='Epoch', ylabel='PSNR (dB)',
               title='ablation of WFIB')
    ax.legend()

    # axs[1].plot(epoch, psnr)
    # axs[1].set(xlabel='Epoch', ylabel='PSNR (dB)',
    #            title='PSNR Analysis')
    #
    # axs[2].plot(epoch, ssim)
    # axs[2].set(xlabel='Epoch', ylabel='SSIM',
    #            title='SSIM Analysis')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
