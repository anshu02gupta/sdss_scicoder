#!/usr/bin/env python
import matplotlib.pyplot as plt

def plot(x, y, xlabel, ylabel, wheretosave= None, redshift=None ): #wheretosave includes path and name of the file
    if redshift is None: pass
    else   :
    
        #create the text to put in the textbox
        textstr = r'z = %.2f' % (redshift, )
    
        #textbox properties
        props = dict(boxstyle='round', facecolor='skyblue', alpha=0.5)
    
        #textbox position
        xtext = min(x)
        ytext = max(y)
    
        #let's plot the textbox!!
        plt.text(xtext, ytext, textstr, fontsize=14,
            verticalalignment='top', bbox=props)
    
    #axes parameters
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
    plt.rcParams["legend.fancybox"] = True
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    #plt.legend()
    plt.plot(x, y,c='skyblue',linestyle='-')

    plt.tick_params(axis='both', top=True, right=True, direction='in')  
    
    if wheretosave is not None:
        plt.savefig(wheretosave + '.pdf') #save the plot in pdf automatically, do we wnat to add the option to choose?
    plt.show()
    
