# -*- coding: utf-8 -*-

"""
Generates Graphs

@author Luis Fonte
@date 20150620
"""

import numpy as np
import matplotlib.pyplot as p
	
def plotGraf(strTitlePlot, listNameX, ValueX, inListNameY, ValueY, labelY):
		
    ''' 
    Method that generates graph, from parameter values.	

    var strTitlePlot - Title
    var inListNameX -  xx's, years
    var inValueX - 0
    var inListNameY - 0
    var inValueY - yy, number
    var inLabelY - yy's label
    '''
    fig = p.figure()
    axisXY = fig.add_subplot(1,1,1)
    
    barQuant = len(ValueY)
    
    ind = range(barQuant)
    
    axisXY.bar(ind, ValueY, facecolor = '#777777', align = 'center')

    axisXY.set_ylabel(labelY)
    axisXY.set_title(strTitlePlot)
    axisXY.set_xticks(ind)
    axisXY.set_xticklabels(listNameX)
    fig.autofmt_xdate()
    p.show()
    pass

def makeGraf(in_data, column, title, label):
    """
    Builds graph, from array with information.

    var in_data - information array 
    var column - column
    var title - graph title
    var lable - axis legend
    """
    data = [x[column] for x in in_data]
    data_distint = list(set(data))
    counts = []
    for ip in data_distint:
        count = 0
        for x in data:
            if x == ip:
                count+=1
        counts.append(count)
            
    plotGraf(title, data_distint, 0, 0, counts, label)
    pass

