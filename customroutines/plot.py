#!/usr/bin/env python
import matplotlib.pyplot as plt

def plot(x, y, xlabel, ylabel, wheretosave, mag, redshift ): #wheretosave includes path and name of the file
    
    plt.axhline(0, color='k', linestyle=':')   
    plt.rcParams['axes.linewidth'] = 1.6
    plt.rc('font', weight = 'medium', family = 'serif', size = 10)
    plt.rcParams['xtick.major.size']  = 7
    plt.rcParams['xtick.major.width'] = 1.5
    plt.rcParams['xtick.minor.size']  = 3
    plt.rcParams['xtick.minor.width'] = 1
    plt.rcParams['ytick.major.size']  = 5
    plt.rcParams['ytick.major.width'] = 1.5
    plt.rcParams['ytick.minor.size']  = 4
    plt.rcParams['ytick.minor.width'] = 1
    #plt.rcParams['pdf.fonttype'] = 42
    #plt.rcParams['ps.fonttype'] = 42
    plt.rcParams["legend.fancybox"] = True
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend(['z = '], redshift
               ['mag = '], mag)
    
    plt.tick_params(axis='both', top=True, right=True, direction='in')  
    plt.savefig(wheretosave + '.pdf')
    plt.show()
    
