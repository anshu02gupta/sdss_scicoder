#!/usr/bin/env python

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt
from pylab import *

def plot(x, y, xlabel, ylabel, typeofplot, y_err, wheretosave= None, redshift=None):
    #xlabel, ylabel, typeofplot and wheretosave are strings
    #wheretosave includes path and name of the file
    
    #typeofplot can be either 'scatter' for a scatter plot or 'plot' for a lineplot
    #y_err is the error array for y
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
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.tick_params(axis='both', top=True, right=True, direction='in')
    #plt.legend()

    #actual plotting
    if typeofplot== 'scatter':
        fig=plt.figure()
        
        _ = plt.errorbar (x, y, yerr= y_err, marker = 'o', mfc = 'blue', mec ='black', mew=2, ls ='None', ecolor= 'blue', capsize = 4,markersize=5)
        return fig


    elif typeofplot== 'plot':
        plt.plot(x, y,c='blue',linestyle='-')
        plt.plot(x, y_err,c='grey',linestyle='-')
#        plt.show()

    
    if wheretosave is not None:
        plt.savefig(wheretosave + '.pdf') #save the plot in pdf automatically, do we wnat to add the option to choose?

    
